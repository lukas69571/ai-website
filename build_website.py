# =====================================================
# build_website.py – KOMPLETTER EFFIZIENTER BUILD
# =====================================================

import os
import shutil
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR / "dist"
SUBPAGES = {
    "ai-solutions": ["index.html", "services.html", "contact.html"]
}
CSS_FILE = BASE_DIR / "style.css"
IMG_DIR = BASE_DIR / "images"

# ----------------------------
# UTILITY
# ----------------------------
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def copy_css(target_dir: Path):
    if CSS_FILE.exists():
        shutil.copy(CSS_FILE, target_dir / CSS_FILE.name)

def copy_images(target_dir: Path):
    if IMG_DIR.exists():
        shutil.copytree(IMG_DIR, target_dir / "images", dirs_exist_ok=True)

def log(msg: str):
    print(f"✅ {msg}")

# ----------------------------
# PAGE GENERATOR
# ----------------------------
def build_page(content: str, target_file: Path):
    ensure_dir(target_file.parent)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)
    log(f"Seite gebaut: {target_file}")

# ----------------------------
# TEMPLATES
# ----------------------------
def get_template(page_name: str, subpage: str = None) -> str:
    title = page_name.replace("-", " ").title()
    css_link = f'<link rel="stylesheet" href="style.css">'
    subpath_prefix = "" if subpage is None else "./"
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {css_link}
</head>
<body>
    <header><h1>{title}</h1></header>
    <main>
        <p>Willkommen auf der Seite {title}.</p>
    </main>
    <footer><p>&copy; 2026 Lukas</p></footer>
</body>
</html>"""
    return html

# ----------------------------
# BUILD LOGIC
# ----------------------------
def build_main_site():
    ensure_dir(DIST_DIR)
    copy_css(DIST_DIR)
    copy_images(DIST_DIR)
    
    for page in ["index", "services", "contact"]:
        target_file = DIST_DIR / f"{page}.html"
        content = get_template(page)
        build_page(content, target_file)
    
    log(f"Website komplett gebaut inkl. CSS → {DIST_DIR}")

def build_subpages():
    for subpage, pages in SUBPAGES.items():
        sub_dir = BASE_DIR / subpage / "dist"
        ensure_dir(sub_dir)
        copy_css(sub_dir)
        copy_images(sub_dir)
        
        for page in pages:
            page_name = page.split(".")[0]
            target_file = sub_dir / page
            content = get_template(page_name, subpage=subpage)
            build_page(content, target_file)
        
        log(f"Website '{BASE_DIR / subpage}' fertig inkl. CSS → {sub_dir}")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    build_main_site()
    build_subpages()
# =====================================================
# build_website.py – KOMPLETTE FERTIGE WEBSITE
# =====================================================

import os
import shutil
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR / "dist"
SUBPAGES = {
    "ai-solutions": ["index.html", "services.html", "contact.html"]
}
CSS_FILE = BASE_DIR / "style.css"
IMG_DIR = BASE_DIR / "images"

# ----------------------------
# UTILITY
# ----------------------------
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def copy_css(target_dir: Path):
    if CSS_FILE.exists():
        shutil.copy(CSS_FILE, target_dir / CSS_FILE.name)

def copy_images(target_dir: Path):
    if IMG_DIR.exists():
        shutil.copytree(IMG_DIR, target_dir / "images", dirs_exist_ok=True)

def log(msg: str):
    print(f"✅ {msg}")

# ----------------------------
# PAGE GENERATOR
# ----------------------------
def build_page(content: str, target_file: Path):
    ensure_dir(target_file.parent)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)
    log(f"Seite gebaut: {target_file}")

# ----------------------------
# TEMPLATES
# ----------------------------
def get_template(page_name: str, subpage: str = None) -> str:
    title = page_name.replace("-", " ").title()
    css_link = f'<link rel="stylesheet" href="style.css">'
    
    # Modernes Layout mit Header, Main, Sections, Footer
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Professionelle AI Services – {title}">
    {css_link}
</head>
<body>
    <header style="padding:20px; text-align:center; background:#1e1e1e; color:white;">
        <h1>{title}</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="services.html">Services</a> |
            <a href="contact.html">Kontakt</a>
        </nav>
    </header>
    
    <main style="padding:20px;">
        <section style="margin-bottom:40px;">
            <h2>Willkommen auf der Seite {title}</h2>
            <p>Wir bieten professionelle Lösungen rund um AI, Automatisierung und Web-Services an.</p>
        </section>
        
        <section style="margin-bottom:40px;">
            <h3>Unsere Services</h3>
            <ul>
                <li>AI-gestützte Videoerstellung</li>
                <li>Website-Building & Automatisierung</li>
                <li>Voice Agents & SaaS-Lösungen</li>
            </ul>
        </section>
        
        <section style="margin-bottom:40px;">
            <h3>Kontakt</h3>
            <p>Schreiben Sie uns: <a href="mailto:info@lukawebsite.de">info@lukawebsite.de</a></p>
        </section>
    </main>
    
    <footer style="padding:20px; text-align:center; background:#1e1e1e; color:white;">
        <p>&copy; 2026 Lukas – Alle Rechte vorbehalten</p>
    </footer>
</body>
</html>"""
    return html

# ----------------------------
# BUILD LOGIC
# ----------------------------
def build_main_site():
    ensure_dir(DIST_DIR)
    copy_css(DIST_DIR)
    copy_images(DIST_DIR)
    
    for page in ["index", "services", "contact"]:
        target_file = DIST_DIR / f"{page}.html"
        content = get_template(page)
        build_page(content, target_file)
    
    log(f"Website komplett gebaut inkl. CSS → {DIST_DIR}")

def build_subpages():
    for subpage, pages in SUBPAGES.items():
        sub_dir = BASE_DIR / subpage / "dist"
        ensure_dir(sub_dir)
        copy_css(sub_dir)
        copy_images(sub_dir)
        
        for page in pages:
            page_name = page.split(".")[0]
            target_file = sub_dir / page
            content = get_template(page_name, subpage=subpage)
            build_page(content, target_file)
        
        log(f"Website '{BASE_DIR / subpage}' fertig inkl. CSS → {sub_dir}")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    build_main_site()
    build_subpages()
# =====================================================
# build_website.py – Single-Page Website
# =====================================================

import os
import shutil
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR / "dist"
CSS_FILE = BASE_DIR / "style.css"
IMG_DIR = BASE_DIR / "images"

# ----------------------------
# UTILITY
# ----------------------------
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def copy_css(target_dir: Path):
    if CSS_FILE.exists():
        shutil.copy(CSS_FILE, target_dir / CSS_FILE.name)

def copy_images(target_dir: Path):
    if IMG_DIR.exists():
        shutil.copytree(IMG_DIR, target_dir / "images", dirs_exist_ok=True)

def log(msg: str):
    print(f"✅ {msg}")

# ----------------------------
# PAGE GENERATOR
# ----------------------------
def build_single_page():
    ensure_dir(DIST_DIR)
    copy_css(DIST_DIR)
    copy_images(DIST_DIR)

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lukas AI Solutions</title>
    <meta name="description" content="Professionelle AI-Services und Automatisierungslösungen">
    <link rel="stylesheet" href="style.css">
    <style>
        body {{ font-family: Arial, sans-serif; margin:0; }}
        header {{ background:#1e1e1e; color:white; padding:20px; text-align:center; position:sticky; top:0; }}
        nav a {{ color:white; margin:0 15px; text-decoration:none; }}
        section {{ padding:60px 20px; }}
        footer {{ background:#1e1e1e; color:white; text-align:center; padding:20px; }}
    </style>
</head>
<body>
    <header>
        <h1>Lukas AI Solutions</h1>
        <nav>
            <a href="#home">Home</a>
            <a href="#services">Services</a>
            <a href="#contact">Kontakt</a>
        </nav>
    </header>

    <section id="home" style="background:#f4f4f4;">
        <h2>Willkommen</h2>
        <p>Wir bieten professionelle Lösungen rund um AI, Automatisierung und Web-Services an.</p>
    </section>

    <section id="services">
        <h2>Unsere Services</h2>
        <ul>
            <li>AI-gestützte Videoerstellung</li>
            <li>Website-Building & Automatisierung</li>
            <li>Voice Agents & SaaS-Lösungen</li>
        </ul>
    </section>

    <section id="contact" style="background:#f4f4f4;">
        <h2>Kontakt</h2>
        <p>Schreiben Sie uns: <a href="mailto:info@lukawebsite.de">info@lukawebsite.de</a></p>
    </section>

    <footer>
        <p>&copy; 2026 Lukas – Alle Rechte vorbehalten</p>
    </footer>
</body>
</html>"""

    target_file = DIST_DIR / "index.html"
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html)
    log(f"Single-Page Website gebaut → {target_file}")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    build_single_page()
# =====================================================
# build_website.py – Multi-Page Website mit Unterseiten
# =====================================================

import os
import shutil
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR / "dist"
CSS_FILE = BASE_DIR / "style.css"
IMG_DIR = BASE_DIR / "images"

PAGES = {
    "index.html": {"title": "Home", "content": "Willkommen auf unserer Home-Seite."},
    "services.html": {"title": "Services", "content": "Unsere AI-gestützten Services."},
    "contact.html": {"title": "Kontakt", "content": "Schreiben Sie uns eine Nachricht."}
}

# ----------------------------
# UTILITY
# ----------------------------
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def copy_css(target_dir: Path):
    if CSS_FILE.exists():
        shutil.copy(CSS_FILE, target_dir / CSS_FILE.name)

def copy_images(target_dir: Path):
    if IMG_DIR.exists():
        shutil.copytree(IMG_DIR, target_dir / "images", dirs_exist_ok=True)

def log(msg: str):
    print(f"✅ {msg}")

# ----------------------------
# PAGE GENERATOR
# ----------------------------
def build_page(filename: str, title: str, content_text: str):
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{title} - Professionelle AI-Lösungen">
    <link rel="stylesheet" href="style.css">
    <style>
        body {{ font-family: Arial, sans-serif; margin:0; padding:0; }}
        header {{ background:#1e1e1e; color:white; padding:20px; text-align:center; }}
        nav a {{ color:white; margin:0 15px; text-decoration:none; }}
        main {{ padding:40px 20px; }}
        footer {{ background:#1e1e1e; color:white; text-align:center; padding:20px; }}
    </style>
</head>
<body>
    <header>
        <h1>Lukas AI Solutions</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="services.html">Services</a> |
            <a href="contact.html">Kontakt</a>
        </nav>
    </header>
    <main>
        <h2>{title}</h2>
        <p>{content_text}</p>
    </main>
    <footer>
        <p>&copy; 2026 Lukas – Alle Rechte vorbehalten</p>
    </footer>
</body>
</html>"""
    target_file = DIST_DIR / filename
    ensure_dir(DIST_DIR)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html)
    log(f"Seite gebaut: {target_file}")

# ----------------------------
# BUILD ALL PAGES
# ----------------------------
def build_website():
    ensure_dir(DIST_DIR)
    copy_css(DIST_DIR)
    copy_images(DIST_DIR)

    for filename, page in PAGES.items():
        build_page(filename, page["title"], page["content"])
    
    log(f"Website komplett gebaut inkl. CSS → {DIST_DIR}")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    build_website()
# =====================================================
# build_website.py – Professionelle Multi-Page Website
# =====================================================

import os
import shutil
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR / "dist"
CSS_FILE = BASE_DIR / "style.css"
IMG_DIR = BASE_DIR / "images"

PAGES = {
    "index.html": {
        "title": "Home",
        "heading": "Willkommen bei Lukas AI Solutions",
        "content": "Wir bieten professionelle AI-Lösungen, Automatisierung und Web-Services für Ihr Business."
    },
    "services.html": {
        "title": "Services",
        "heading": "Unsere Services",
        "content": "<ul><li>AI-gestützte Videoerstellung</li><li>Website-Building & Automatisierung</li><li>Voice Agents & SaaS-Lösungen</li></ul>"
    },
    "contact.html": {
        "title": "Kontakt",
        "heading": "Kontakt",
        "content": "Schreiben Sie uns: <a href='mailto:info@lukawebsite.de'>info@lukawebsite.de</a>"
    }
}

# ----------------------------
# UTILITY
# ----------------------------
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def copy_css(target_dir: Path):
    if CSS_FILE.exists():
        shutil.copy(CSS_FILE, target_dir / CSS_FILE.name)

def copy_images(target_dir: Path):
    if IMG_DIR.exists():
        shutil.copytree(IMG_DIR, target_dir / "images", dirs_exist_ok=True)

def log(msg: str):
    print(f"✅ {msg}")

# ----------------------------
# PAGE GENERATOR
# ----------------------------
def build_page(filename: str, title: str, heading: str, content_html: str):
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} – Lukas AI Solutions</title>
    <meta name="description" content="{heading} – Professionelle AI-Lösungen">
    <link rel="stylesheet" href="style.css">
    <style>
        body {{ font-family: Arial, Helvetica, sans-serif; margin:0; padding:0; line-height:1.6; }}
        header {{ background:#1e1e1e; color:white; padding:20px; text-align:center; position:sticky; top:0; z-index:100; }}
        nav a {{ color:white; margin:0 15px; text-decoration:none; font-weight:bold; }}
        nav a:hover {{ text-decoration:underline; }}
        main {{ padding:40px 20px; max-width:1000px; margin:auto; }}
        section {{ padding:60px 0; }}
        h1, h2 {{ margin-bottom:20px; }}
        footer {{ background:#1e1e1e; color:white; text-align:center; padding:20px; margin-top:40px; }}
        a.button {{ display:inline-block; padding:10px 20px; background:#ff6600; color:white; text-decoration:none; border-radius:5px; }}
        a.button:hover {{ background:#ff8533; }}
    </style>
    <script>
        // Smooth Scrolling
        document.addEventListener('DOMContentLoaded', function() {{
            const links = document.querySelectorAll('nav a[href^="#"], nav a[href$=".html"]');
            links.forEach(link => {{
                link.addEventListener('click', function(e) {{
                    if(this.hash) {{
                        e.preventDefault();
                        document.querySelector(this.hash).scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }});
            }});
        }});
    </script>
</head>
<body>
    <header>
        <h1>Lukas AI Solutions</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="services.html">Services</a> |
            <a href="contact.html">Kontakt</a>
        </nav>
    </header>
    <main>
        <section>
            <h2>{heading}</h2>
            {content_html}
        </section>
    </main>
    <footer>
        <p>&copy; 2026 Lukas – Alle Rechte vorbehalten</p>
    </footer>
</body>
</html>"""
    target_file = DIST_DIR / filename
    ensure_dir(DIST_DIR)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html)
    log(f"Seite gebaut: {target_file}")

# ----------------------------
# BUILD ALL PAGES
# ----------------------------
def build_website():
    ensure_dir(DIST_DIR)
    copy_css(DIST_DIR)
    copy_images(DIST_DIR)

    # QA Checks
    if not CSS_FILE.exists():
        log("❌ WARNUNG: style.css fehlt!")
    if not IMG_DIR.exists():
        log("⚠️ WARNUNG: images Ordner fehlt!")

    for filename, page in PAGES.items():
        build_page(filename, page["title"], page["heading"], page["content"])
    
    log(f"Website komplett gebaut inkl. CSS und Bilder → {DIST_DIR}")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    build_website()
# =====================================================
# build_website.py – Profi Multi-Page Website + SEO/Accessibility
# =====================================================

import os
import shutil
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR / "dist"
CSS_FILE = BASE_DIR / "style.css"
IMG_DIR = BASE_DIR / "images"

PAGES = {
    "index.html": {
        "title": "Home",
        "heading": "Willkommen bei Lukas AI Solutions",
        "content": "Wir bieten professionelle AI-Lösungen, Automatisierung und Web-Services für Ihr Business.",
        "image": "home.jpg"
    },
    "services.html": {
        "title": "Services",
        "heading": "Unsere Services",
        "content": "<ul><li>AI-gestützte Videoerstellung</li><li>Website-Building & Automatisierung</li><li>Voice Agents & SaaS-Lösungen</li></ul>",
        "image": "services.jpg"
    },
    "contact.html": {
        "title": "Kontakt",
        "heading": "Kontakt",
        "content": "Schreiben Sie uns: <a href='mailto:info@lukawebsite.de'>info@lukawebsite.de</a>",
        "image": "contact.jpg"
    }
}

# ----------------------------
# UTILITY
# ----------------------------
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def copy_css(target_dir: Path):
    if CSS_FILE.exists():
        shutil.copy(CSS_FILE, target_dir / CSS_FILE.name)

def copy_images(target_dir: Path):
    if IMG_DIR.exists():
        shutil.copytree(IMG_DIR, target_dir / "images", dirs_exist_ok=True)

def log(msg: str):
    print(f"✅ {msg}")

# ----------------------------
# PAGE GENERATOR
# ----------------------------
def build_page(filename: str, page: dict):
    img_tag = f"<img src='images/{page['image']}' alt='{page['heading']}' style='max-width:100%; height:auto;' />" if 'image' in page else ""
    
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page['title']} – Lukas AI Solutions</title>
    <meta name="description" content="{page['heading']} – Professionelle AI-Lösungen">
    <link rel="stylesheet" href="style.css">
    
    <!-- Open Graph / Social -->
    <meta property="og:title" content="{page['title']} – Lukas AI Solutions">
    <meta property="og:description" content="{page['heading']} – Professionelle AI-Lösungen">
    <meta property="og:type" content="website">
    <meta property="og:image" content="images/{page.get('image','') }">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{page['title']} – Lukas AI Solutions">
    <meta name="twitter:description" content="{page['heading']} – Professionelle AI-Lösungen">
    <meta name="twitter:image" content="images/{page.get('image','')}">

    <style>
        body {{ font-family: Arial, Helvetica, sans-serif; margin:0; padding:0; line-height:1.6; }}
        header {{ background:#1e1e1e; color:white; padding:20px; text-align:center; position:sticky; top:0; z-index:100; }}
        nav a {{ color:white; margin:0 15px; text-decoration:none; font-weight:bold; }}
        nav a:hover {{ text-decoration:underline; }}
        main {{ padding:40px 20px; max-width:1000px; margin:auto; }}
        section {{ padding:60px 0; }}
        h1, h2 {{ margin-bottom:20px; }}
        footer {{ background:#1e1e1e; color:white; text-align:center; padding:20px; margin-top:40px; }}
        a.button {{ display:inline-block; padding:10px 20px; background:#ff6600; color:white; text-decoration:none; border-radius:5px; }}
        a.button:hover {{ background:#ff8533; }}
    </style>
</head>
<body>
    <header>
        <h1>Lukas AI Solutions</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="services.html">Services</a> |
            <a href="contact.html">Kontakt</a>
        </nav>
    </header>
    <main>
        <section>
            <h2>{page['heading']}</h2>
            {img_tag}
            <p>{page['content']}</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 Lukas – Alle Rechte vorbehalten</p>
    </footer>
</body>
</html>"""
    
    target_file = DIST_DIR / filename
    ensure_dir(DIST_DIR)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html)
    log(f"Seite gebaut: {target_file}")

# ----------------------------
# SITEMAP GENERATOR
# ----------------------------
def build_sitemap():
    urls = [f"<url><loc>http://example.com/{filename}</loc></url>" for filename in PAGES.keys()]
    sitemap_content = f"<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>{''.join(urls)}</urlset>"
    sitemap_file = DIST_DIR / "sitemap.xml"
    with open(sitemap_file, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    log(f"Sitemap erstellt → {sitemap_file}")

# ----------------------------
# BUILD WEBSITE
# ----------------------------
def build_website():
    ensure_dir(DIST_DIR)
    copy_css(DIST_DIR)
    copy_images(DIST_DIR)
    
    if not CSS_FILE.exists():
        log("❌ WARNUNG: style.css fehlt!")
    if not IMG_DIR.exists():
        log("⚠️ WARNUNG: images Ordner fehlt!")

    for filename, page in PAGES.items():
        build_page(filename, page)
    
    build_sitemap()
    log(f"Website komplett gebaut inkl. SEO, Bilder und Sitemap → {DIST_DIR}")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    build_website()
# =====================================================
# build_website.py – Profi Multi-Page Website + Automatische Bilder
# =====================================================

import os
import shutil
from pathlib import Path
import random

# ----------------------------
# CONFIG
# ----------------------------
BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR / "dist"
CSS_FILE = BASE_DIR / "style.css"
IMAGES_DIR = BASE_DIR / "images"  # Die Fabrik sucht hier automatisch alle Bilder

PAGES = {
    "index.html": {
        "title": "Home",
        "heading": "Willkommen bei Lukas AI Solutions",
        "content": "Automatisierte AI-Lösungen für moderne Unternehmen – Video, Website, Voice Agents."
    },
    "services.html": {
        "title": "Services",
        "heading": "Unsere Services",
        "content": [
            {"title": "AI-Video-Erstellung", "desc": "Automatisch generierte Videos auf Knopfdruck."},
            {"title": "Website & Automation", "desc": "Websites bauen & Prozesse automatisieren."},
            {"title": "Voice Agents & SaaS", "desc": "Individuelle Sprachagenten für Kundenlösungen."}
        ]
    },
    "contact.html": {
        "title": "Kontakt",
        "heading": "Kontakt",
        "content": "Jetzt anfragen: <a href='mailto:info@lukawebsite.de'>info@lukawebsite.de</a>"
    }
}

# ----------------------------
# UTILITY
# ----------------------------
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def get_all_images():
    """Alle Bilder im Images-Ordner finden (jpg, png, webp)"""
    ensure_dir(IMAGES_DIR)
    return [f for f in IMAGES_DIR.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']]

def log(msg: str):
    print(f"✅ {msg}")

# ----------------------------
# PAGE GENERATOR
# ----------------------------
def build_page(filename: str, page: dict, images: list):
    # Bild automatisch wählen
    img_file = random.choice(images) if images else None
    img_tag = f"<img src='images/{img_file.name}' alt='{page['heading']}' style='max-width:100%; height:auto;' />" if img_file else ""

    if filename == "services.html":
        # Services als Card-Layout
        cards_html = ""
        for service in page['content']:
            service_img = random.choice(images) if images else None
            service_img_tag = f"<img src='images/{service_img.name}' alt='{service['title']}' style='max-width:100%; height:auto;' />" if service_img else ""
            cards_html += f"""
            <div class='card'>
                {service_img_tag}
                <h3>{service['title']}</h3>
                <p>{service['desc']}</p>
            </div>"""
        content_html = f"<div class='cards'>{cards_html}</div>"
    else:
        content_html = f"{img_tag}<p>{page['content']}</p>"

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page['title']} – Lukas AI Solutions</title>
    <meta name="description" content="{page['heading']} – Professionelle AI-Lösungen">
    <link rel="stylesheet" href="style.css">

    <!-- Open Graph / Social -->
    <meta property="og:title" content="{page['title']} – Lukas AI Solutions">
    <meta property="og:description" content="{page['heading']} – Professionelle AI-Lösungen">
    <meta property="og:type" content="website">
    <meta property="og:image" content="images/{img_file.name if img_file else ''}">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{page['title']} – Lukas AI Solutions">
    <meta name="twitter:description" content="{page['heading']} – Professionelle AI-Lösungen">
    <meta name="twitter:image" content="images/{img_file.name if img_file else ''}">

    <style>
        body {{ font-family: Arial, Helvetica, sans-serif; margin:0; padding:0; line-height:1.6; }}
        header {{ background:#1e1e1e; color:white; padding:20px; text-align:center; position:sticky; top:0; z-index:100; }}
        nav a {{ color:white; margin:0 15px; text-decoration:none; font-weight:bold; }}
        nav a:hover {{ text-decoration:underline; }}
        main {{ padding:40px 20px; max-width:1000px; margin:auto; }}
        section {{ padding:60px 0; }}
        h1, h2 {{ margin-bottom:20px; }}
        footer {{ background:#1e1e1e; color:white; text-align:center; padding:20px; margin-top:40px; }}
        a.button {{ display:inline-block; padding:10px 20px; background:#ff6600; color:white; text-decoration:none; border-radius:5px; }}
        a.button:hover {{ background:#ff8533; }}
        /* Services Cards */
        .cards {{ display:flex; flex-wrap:wrap; gap:20px; justify-content:center; }}
        .card {{ flex:1 1 300px; padding:20px; border:1px solid #ddd; border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center; }}
        .card img {{ max-width:100%; height:auto; border-radius:5px; }}
        .card h3 {{ margin-top:15px; }}
        .card p {{ margin-top:10px; }}
    </style>
</head>
<body>
    <header>
        <h1>Lukas AI Solutions</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="services.html">Services</a> |
            <a href="contact.html">Kontakt</a>
        </nav>
    </header>
    <main>
        <section>
            <h2>{page['heading']}</h2>
            {content_html}
        </section>
    </main>
    <footer>
        <p>&copy; 2026 Lukas – Alle Rechte vorbehalten</p>
    </footer>
</body>
</html>"""

    target_file = DIST_DIR / filename
    ensure_dir(DIST_DIR)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html)
    log(f"Seite gebaut: {target_file}")

# ----------------------------
# SITEMAP GENERATOR
# ----------------------------
def build_sitemap():
    urls = [f"<url><loc>http://example.com/{filename}</loc></url>" for filename in PAGES.keys()]
    sitemap_content = f"<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>{''.join(urls)}</urlset>"
    sitemap_file = DIST_DIR / "sitemap.xml"
    with open(sitemap_file, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    log(f"Sitemap erstellt → {sitemap_file}")

# ----------------------------
# BUILD WEBSITE
# ----------------------------
def build_website():
    ensure_dir(DIST_DIR)
    copy_css(DIST_DIR)
    copy_images(DIST_DIR)

    images = get_all_images()
    if not images:
        log("⚠️ WARNUNG: Keine Bilder gefunden, Seiten werden ohne Bilder gebaut!")

    for filename, page in PAGES.items():
        build_page(filename, page, images)
    
    build_sitemap()
    log(f"Website komplett gebaut inkl. Bilder, Cards, SEO und Sitemap → {DIST_DIR}")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    build_website()
def render_landingpage(slug, data):
    return f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <title>{data['title']}</title>
    <meta name="description" content="{data['hero']['headline']}">
</head>
<body>

<section class="hero">
    <h1>{data['hero']['headline']}</h1>
    <p>{data['hero']['subline']}</p>
    <a class="cta">{data['hero']['cta']}</a>
</section>

<section class="problems">
    <ul>
        {''.join(f"<li>{p}</li>" for p in data['problems'])}
    </ul>
</section>

<section class="solution">
    <h2>{data['solution']['headline']}</h2>
    <p>{data['solution']['text']}</p>
</section>

<section class="benefits">
    <ul>
        {''.join(f"<li>{b}</li>" for b in data['benefits'])}
    </ul>
</section>

<section class="process">
    <ol>
        {''.join(f"<li>{step}</li>" for step in data['process'])}
    </ol>
</section>

<section class="trust">
    <p>{data['trust']}</p>
</section>

<section class="cta-final">
    <a class="cta">{data['cta_final']}</a>
</section>

</body>
</html>
"""
def build_landingpages(base_path):
    for slug, data in LANDINGPAGES.items():
        html = render_landingpage(slug, data)
        path = base_path / slug
        path.mkdir(parents=True, exist_ok=True)
        (path / "index.html").write_text(html, encoding="utf-8")
SEO_KEYWORDS = {
    "ki-automatisierung": {
        "base_title": "KI Automatisierung",
        "intents": [
            "für Unternehmen",
            "für KMU",
            "Prozesse automatisieren",
            "Workflows automatisieren",
            "KI Agenten einsetzen"
        ],
        "description_template": "Professionelle {kw} – Prozesse automatisieren, Kosten senken, skalieren."
    }
}
def render_seo_landingpage(base_slug, base_data, keyword, description_tpl):
    title = f"{base_data['base_title']} {keyword}"
    description = description_tpl.format(kw=title)

    data = LANDINGPAGES["ai-automation"].copy()

    data["title"] = title
    data["hero"] = {
        "headline": title,
        "subline": description,
        "cta": "Kostenlose Analyse anfragen"
    }

    return render_landingpage(f"{base_slug}-{keyword}", data), title, description
def build_seo_pages(base_path):
    for base_slug, seo in SEO_KEYWORDS.items():
        for intent in seo["intents"]:
            slug = f"{base_slug}-{intent.lower().replace(' ', '-')}"
            html, title, description = render_seo_landingpage(
                base_slug,
                seo,
                intent,
                seo["description_template"]
            )

            path = base_path / slug
            path.mkdir(parents=True, exist_ok=True)
            (path / "index.html").write_text(html, encoding="utf-8")
<section class="internal-links">
    <h3>Weitere Lösungen</h3>
    <ul>
        <li><a href="/ki-automatisierung-fuer-unternehmen/">KI Automatisierung für Unternehmen</a></li>
        <li><a href="/ki-automatisierung-prozesse-automatisieren/">Prozesse automatisieren</a></li>
    </ul>
</section>
if __name__ == "__main__":
    BASE_PATH = Path("dist")

    build_landingpages(BASE_PATH)
    build_seo_pages(BASE_PATH)
PRICING_PLANS = [
    {
        "name": "Starter",
        "price": "ab 499€",
        "features": [
            "Prozessanalyse",
            "1 KI-Automatisierung",
            "Basis-Monitoring"
        ],
        "cta": "Anfrage starten"
    },
    {
        "name": "Pro",
        "price": "ab 1.499€",
        "features": [
            "Mehrere Automatisierungen",
            "Individuelle Agenten",
            "Monitoring & Wartung"
        ],
        "cta": "Strategie-Call buchen"
    },
    {
        "name": "Enterprise",
        "price": "Custom",
        "features": [
            "End-to-End Automatisierung",
            "SLA & Support",
            "Skalierbare Infrastruktur"
        ],
        "cta": "Kontakt aufnehmen"
    }
]
def render_pricing_page():
    plans_html = ""
    for plan in PRICING_PLANS:
        plans_html += f"""
        <div class="plan">
            <h2>{plan['name']}</h2>
            <p class="price">{plan['price']}</p>
            <ul>
                {''.join(f"<li>{f}</li>" for f in plan['features'])}
            </ul>
            <a class="cta">{plan['cta']}</a>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Preise & Pakete</title>
    <meta name="description" content="Klare Pakete für KI-Automatisierung und skalierbare Systeme.">
</head>
<body>
<section class="pricing">
    <h1>Preise & Pakete</h1>
    <div class="plans">
        {plans_html}
    </div>
</section>
</body>
</html>
"""
def build_pricing_page(base_path):
    path = base_path / "preise"
    path.mkdir(parents=True, exist_ok=True)
    (path / "index.html").write_text(render_pricing_page(), encoding="utf-8")
def build_saas_placeholders(base_path):
    pages = {
        "login": "Login – demnächst verfügbar",
        "dashboard": "Dashboard – SaaS in Vorbereitung",
        "api": "API – bald verfügbar"
    }

    for slug, headline in pages.items():
        path = base_path / slug
        path.mkdir(parents=True, exist_ok=True)
        (path / "index.html").write_text(f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <title>{headline}</title>
</head>
<body>
<h1>{headline}</h1>
<p>Dieses Produkt befindet sich aktuell im Aufbau.</p>
</body>
</html>
""", encoding="utf-8")
if __name__ == "__main__":
    BASE_PATH = Path("dist")

    build_landingpages(BASE_PATH)
    build_seo_pages(BASE_PATH)
    build_pricing_page(BASE_PATH)
    build_saas_placeholders(BASE_PATH)
from bs4 import BeautifulSoup

def scan_html_files(base_path):
    html_files = list(base_path.rglob("index.html"))
    pages = []

    for file in html_files:
        content = file.read_text(encoding="utf-8")
        soup = BeautifulSoup(content, "html.parser")

        title = soup.title.string.strip() if soup.title else ""
        description_tag = soup.find("meta", attrs={"name": "description"})
        description = description_tag["content"].strip() if description_tag else ""

        links = [a.get("href") for a in soup.find_all("a") if a.get("href")]

        pages.append({
            "file": file,
            "title": title,
            "description": description,
            "links": links,
            "content_length": len(soup.get_text(strip=True))
        })

    return pages
def check_broken_links(pages, base_path):
    existing_paths = {"/" + str(p["file"].parent.relative_to(base_path)).replace("\\", "/") + "/" for p in pages}
    broken = []

    for page in pages:
        for link in page["links"]:
            if link.startswith("/") and link not in existing_paths:
                broken.append((page["file"], link))

    return broken
def check_duplicates(pages):
    titles = {}
    descriptions = {}

    duplicate_titles = []
    duplicate_descriptions = []

    for p in pages:
        if p["title"]:
            if p["title"] in titles:
                duplicate_titles.append(p["title"])
            titles[p["title"]] = True

        if p["description"]:
            if p["description"] in descriptions:
                duplicate_descriptions.append(p["description"])
            descriptions[p["description"]] = True

    return duplicate_titles, duplicate_descriptions
def check_empty_pages(pages, min_length=200):
    return [p["file"] for p in pages if p["content_length"] < min_length]
def generate_build_report(pages, broken_links, dup_titles, dup_desc, empty_pages):
    report = []
    report.append(f"Gesamtseiten: {len(pages)}")
    report.append(f"Broken Links: {len(broken_links)}")
    report.append(f"Duplicate Titles: {len(set(dup_titles))}")
    report.append(f"Duplicate Descriptions: {len(set(dup_desc))}")
    report.append(f"Leere Seiten: {len(empty_pages)}")

    return "\n".join(report)
def run_qa(base_path):
    pages = scan_html_files(base_path)

    broken_links = check_broken_links(pages, base_path)
    dup_titles, dup_desc = check_duplicates(pages)
    empty_pages = check_empty_pages(pages)

    report = generate_build_report(
        pages,
        broken_links,
        dup_titles,
        dup_desc,
        empty_pages
    )

    report_path = base_path / "build_report.txt"
    report_path.write_text(report, encoding="utf-8")

    print("QA abgeschlossen")
    print(report)
if __name__ == "__main__":
    BASE_PATH = Path("dist")

    build_landingpages(BASE_PATH)
    build_seo_pages(BASE_PATH)
    build_pricing_page(BASE_PATH)
    build_saas_placeholders(BASE_PATH)

    run_qa(BASE_PATH)
<form method="POST" action="/lead">
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="E-Mail" required>

    <!-- Tracking -->
    <input type="hidden" name="source_page" value="{{PAGE_SLUG}}">
    <input type="hidden" name="campaign" value="{{CAMPAIGN}}">
    <input type="hidden" name="timestamp" value="{{TIMESTAMP}}">

    <button type="submit">Anfrage senden</button>
</form>
from datetime import datetime

def render_form(slug):
    return f"""
<form method="POST" action="/lead">
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="E-Mail" required>

    <input type="hidden" name="source_page" value="{slug}">
    <input type="hidden" name="campaign" value="organic">
    <input type="hidden" name="timestamp" value="{datetime.utcnow().isoformat()}">

    <button class="cta" type="submit">Anfrage senden</button>
</form>
"""
<section class="cta-final">
    {render_form(slug)}
</section>
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from pathlib import Path
import json
import csv
from datetime import datetime

BASE = Path("leads")
BASE.mkdir(exist_ok=True)

CSV_FILE = BASE / "leads.csv"
JSON_FILE = BASE / "leads.json"

class LeadHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/lead":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode()
        data = {k: v[0] for k, v in parse_qs(body).items()}
        data["received_at"] = datetime.utcnow().isoformat()

        # CSV
        file_exists = CSV_FILE.exists()
        with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        # JSON
        leads = []
        if JSON_FILE.exists():
            leads = json.loads(JSON_FILE.read_text(encoding="utf-8"))
        leads.append(data)
        JSON_FILE.write_text(json.dumps(leads, indent=2), encoding="utf-8")

        self.send_response(302)
        self.send_header("Location", "/danke")
        self.end_headers()

if __name__ == "__main__":
    HTTPServer(("localhost", 8000), LeadHandler).serve_forever()
def build_thankyou_page(base_path):
    path = base_path / "danke"
    path.mkdir(parents=True, exist_ok=True)
    (path / "index.html").write_text("""
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Danke für deine Anfrage</title>
</head>
<body>
<h1>Anfrage erhalten</h1>
<p>Wir melden uns zeitnah.</p>
</body>
</html>
""", encoding="utf-8")
import json
import csv
import smtplib
from email.message import EmailMessage
from pathlib import Path
import requests

# Basisordner für Leads
LEAD_PATH = Path("leads")
LEAD_PATH.mkdir(exist_ok=True)
CSV_FILE = LEAD_PATH / "leads.csv"
JSON_FILE = LEAD_PATH / "leads.json"

# Beispiel: Mail-Benachrichtigung
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "dein@email.com"
SMTP_PASS = "PASSWORT"

def send_email_notification(lead):
    msg = EmailMessage()
    msg['Subject'] = f"Neuer Lead: {lead['name']}"
    msg['From'] = SMTP_USER
    msg['To'] = "sales@deinefirma.de"
    msg.set_content(f"Neuer Lead:\nName: {lead['name']}\nEmail: {lead['email']}\nSeite: {lead['source_page']}\nZeit: {lead['received_at']}")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)

# Beispiel: Push in CRM via API (hier Pseudo-Code)
CRM_API_URL = "https://api.mailerlite.com/api/v2/subscribers"
CRM_API_KEY = "DEIN_API_KEY"

def push_to_crm(lead):
    headers = {"Content-Type": "application/json", "X-MailerLite-ApiKey": CRM_API_KEY}
    data = {"email": lead["email"], "name": lead["name"], "fields": {"source_page": lead["source_page"]}}
    response = requests.post(CRM_API_URL, headers=headers, json=data)
    return response.status_code

# Lead verarbeiten
def process_new_leads():
    if not JSON_FILE.exists():
        return

    leads = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    for lead in leads:
        try:
            send_email_notification(lead)
        except Exception as e:
            print(f"⚠️ E-Mail-Benachrichtigung fehlgeschlagen: {e}")
        try:
            status = push_to_crm(lead)
            if status == 200 or status == 201:
                print(f"✅ Lead {lead['email']} an CRM gesendet.")
            else:
                print(f"⚠️ CRM Push fehlgeschlagen: {status}")
        except Exception as e:
            print(f"⚠️ CRM Push Exception: {e}")
# In lead_server.py nach Speicherung
process_new_leads()
# =====================================================
# AI-FABRIK – Lead Server + CRM + E-Mail Automation
# Phase 5 + 7 kombiniert
# =====================================================

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from pathlib import Path
import json
import csv
from datetime import datetime
import smtplib
from email.message import EmailMessage
import requests

# ================== Konfiguration ==================
BASE = Path("leads")
BASE.mkdir(exist_ok=True)

CSV_FILE = BASE / "leads.csv"
JSON_FILE = BASE / "leads.json"

# E-Mail
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "dein@email.com"
SMTP_PASS = "PASSWORT"
EMAIL_TARGET = "sales@deinefirma.de"

# CRM
CRM_API_URL = "https://api.mailerlite.com/api/v2/subscribers"
CRM_API_KEY = "DEIN_API_KEY"

# ================== Helper-Funktionen ==================
def send_email_notification(lead):
    msg = EmailMessage()
    msg['Subject'] = f"Neuer Lead: {lead['name']}"
    msg['From'] = SMTP_USER
    msg['To'] = EMAIL_TARGET
    msg.set_content(
        f"Neuer Lead:\n"
        f"Name: {lead['name']}\n"
        f"Email: {lead['email']}\n"
        f"Seite: {lead['source_page']}\n"
        f"Zeit: {lead['received_at']}"
    )
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)

def push_to_crm(lead):
    headers = {"Content-Type": "application/json", "X-MailerLite-ApiKey": CRM_API_KEY}
    data = {"email": lead["email"], "name": lead["name"], "fields": {"source_page": lead["source_page"]}}
    response = requests.post(CRM_API_URL, headers=headers, json=data)
    return response.status_code

def process_new_lead(lead):
    # CSV speichern
    file_exists = CSV_FILE.exists()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=lead.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(lead)

    # JSON speichern
    leads = []
    if JSON_FILE.exists():
        leads = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    leads.append(lead)
    JSON_FILE.write_text(json.dumps(leads, indent=2), encoding="utf-8")

    # E-Mail & CRM
    try:
        send_email_notification(lead)
        print(f"✅ E-Mail an {EMAIL_TARGET} gesendet.")
    except Exception as e:
        print(f"⚠️ E-Mail Versand fehlgeschlagen: {e}")

    try:
        status = push_to_crm(lead)
        if status in [200, 201]:
            print(f"✅ Lead {lead['email']} an CRM gesendet.")
        else:
            print(f"⚠️ CRM Push fehlgeschlagen: Status {status}")
    except Exception as e:
        print(f"⚠️ CRM Push Exception: {e}")

# ================== HTTP Server ==================
class LeadHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/lead":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode()
        data = {k: v[0] for k, v in parse_qs(body).items()}
        data["received_at"] = datetime.utcnow().isoformat()

        # Lead verarbeiten
        process_new_lead(data)

        # Weiterleitung zur Danke-Seite
        self.send_response(302)
        self.send_header("Location", "/danke")
        self.end_headers()

# ================== Server starten ==================
if __name__ == "__main__":
    print("🚀 Lead Server läuft auf http://localhost:8000")
    HTTPServer(("localhost", 8000), LeadHandler).serve_forever()
