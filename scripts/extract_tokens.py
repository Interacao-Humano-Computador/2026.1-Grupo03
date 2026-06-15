"""
Extrai tokens de design (cores, tipografia, espaçamento) e CSS computado de
componentes de uma URL, emulando dispositivo móvel com Playwright.
"""
import json
import sys
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://www.procon.df.gov.br/"
OUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "procon-tokens"

MOBILE_DEVICE = {
    "viewport": {"width": 390, "height": 844},
    "device_scale_factor": 3,
    "is_mobile": True,
    "has_touch": True,
    "user_agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 "
        "Mobile/15E148 Safari/604.1"
    ),
}

COMPONENT_SELECTORS = {
    "button": "button, a.btn, [class*='btn'], [class*='button'], input[type='submit']",
    "input": "input[type='text'], input[type='search'], input[type='email'], textarea",
    "header_nav": "header, nav, [role='banner'], [role='navigation']",
    "footer": "footer, [role='contentinfo']",
    "card": (
        "[class*='card'], [class*='item'], article, "
        ".post, [class*='noticia'], [class*='news']"
    ),
}

CSS_PROPS = [
    "color", "background-color", "font-family", "font-size", "font-weight",
    "line-height", "letter-spacing", "padding", "padding-top", "padding-right",
    "padding-bottom", "padding-left", "margin", "margin-top", "margin-right",
    "margin-bottom", "margin-left", "border", "border-radius", "border-color",
    "box-shadow", "display", "gap", "max-width", "width",
]


def get_root_vars(page) -> dict:
    return page.evaluate("""() => {
        const styles = {};
        for (const sheet of document.styleSheets) {
            try {
                for (const rule of sheet.cssRules) {
                    if (rule.selectorText === ':root') {
                        const style = rule.style;
                        for (let i = 0; i < style.length; i++) {
                            const prop = style[i];
                            if (prop.startsWith('--')) {
                                styles[prop] = style.getPropertyValue(prop).trim();
                            }
                        }
                    }
                }
            } catch (e) {}
        }
        return styles;
    }""")


def get_computed_styles(page, selector: str, props: list) -> dict | None:
    return page.evaluate(
        """([selector, props]) => {
            const el = document.querySelector(selector);
            if (!el) return null;
            const computed = window.getComputedStyle(el);
            const result = { _tag: el.tagName, _class: el.className };
            for (const p of props) result[p] = computed.getPropertyValue(p).trim();
            return result;
        }""",
        [selector, props],
    )


def extract_palette(page) -> list:
    return page.evaluate("""() => {
        const colors = new Set();
        const all = document.querySelectorAll('*');
        const limit = Math.min(all.length, 300);
        for (let i = 0; i < limit; i++) {
            const s = window.getComputedStyle(all[i]);
            ['color','background-color','border-color'].forEach(p => {
                const v = s.getPropertyValue(p);
                if (v && v !== 'rgba(0, 0, 0, 0)' && v !== 'rgb(0, 0, 0)'
                    && v !== 'transparent') colors.add(v);
            });
        }
        return [...colors].slice(0, 40);
    }""")


def extract_spacing(page) -> list:
    return page.evaluate("""() => {
        const vals = new Map();
        const all = document.querySelectorAll('*');
        const limit = Math.min(all.length, 200);
        for (let i = 0; i < limit; i++) {
            const s = window.getComputedStyle(all[i]);
            ['padding','margin','gap'].forEach(p => {
                const v = s.getPropertyValue(p);
                if (v && v !== '0px') {
                    vals.set(v, (vals.get(v) || 0) + 1);
                }
            });
        }
        return [...vals.entries()]
            .sort((a, b) => b[1] - a[1])
            .slice(0, 20)
            .map(([v, c]) => ({ value: v, count: c }));
    }""")


def extract_typography(page) -> list:
    return page.evaluate("""() => {
        const fonts = new Map();
        const tags = ['h1','h2','h3','h4','p','a','button','label','span'];
        for (const tag of tags) {
            const el = document.querySelector(tag);
            if (!el) continue;
            const s = window.getComputedStyle(el);
            fonts.set(tag, {
                fontFamily: s.fontFamily,
                fontSize: s.fontSize,
                fontWeight: s.fontWeight,
                lineHeight: s.lineHeight,
                letterSpacing: s.letterSpacing,
            });
        }
        return Object.fromEntries(fonts);
    }""")


def main(url: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(**{
            "viewport": MOBILE_DEVICE["viewport"],
            "device_scale_factor": MOBILE_DEVICE["device_scale_factor"],
            "is_mobile": MOBILE_DEVICE["is_mobile"],
            "has_touch": MOBILE_DEVICE["has_touch"],
            "user_agent": MOBILE_DEVICE["user_agent"],
        })
        page = context.new_page()

        print(f"Carregando {url} em modo mobile (390x844)…")
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(2000)

        # Screenshot full-page mobile
        screenshot_path = out_dir / "screenshot_mobile_fullpage.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        print(f"Screenshot salvo: {screenshot_path}")

        # CSS variables de :root
        root_vars = get_root_vars(page)

        # Paleta de cores
        palette = extract_palette(page)

        # Tipografia
        typography = extract_typography(page)

        # Espaçamento
        spacing = extract_spacing(page)

        # CSS computado por componente
        components = {}
        for name, selector in COMPONENT_SELECTORS.items():
            styles = get_computed_styles(page, selector, CSS_PROPS)
            components[name] = styles
            if styles:
                print(f"  Componente '{name}' capturado ({styles.get('_tag','')})")
            else:
                print(f"  Componente '{name}' não encontrado com seletor: {selector}")

        browser.close()

    tokens = {
        "url": url,
        "device": "iPhone12-390x844",
        "root_css_variables": root_vars,
        "palette": palette,
        "typography": typography,
        "spacing_rhythm": spacing,
        "components": components,
    }

    tokens_path = out_dir / "tokens.json"
    tokens_path.write_text(json.dumps(tokens, indent=2, ensure_ascii=False))
    print(f"\nTokens salvos: {tokens_path}")
    return tokens


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrai design tokens via Playwright")
    parser.add_argument("url", nargs="?", default=URL)
    parser.add_argument("--out", default=str(OUT_DIR))
    args = parser.parse_args()
    main(args.url, Path(args.out))
