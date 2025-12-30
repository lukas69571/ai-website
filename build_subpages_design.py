from pathlib import Path

# ---------------- VERZEICHNISSE ----------------
ROOT = Path.cwd()  # Aktuelles Verzeichnis: C:\Users\lukas\website
IMG_DIR = ROOT / "assets/images"
CSS_FILE = ROOT / "assets/css/style.css"

# Unterseiten-Inhalt
SUBPAGES = {
    "index.html": {"headline": "Willkommen auf unserer Website", "text": "Dies ist die Startseite.", "image": "home.png"},
    "services.html": {"headline": "Unsere Leistungen", "text": "Webentwicklung, KI-Lösungen und mehr.", "image": "services.png"},
    "about.html": {"headline": "Über uns", "text": "Wir sind ein Team von Entwicklern.", "image": "about.png"},
    "contact.html": {"headline": "Kontakt", "text": "Hier kannst du uns erreichen.", "image": "contact.png"},
}

# Modernes CSS
CSS_CONTENT = """
body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f5f5f5;
    color: #111111;
}
header, footer {
    background: #ffffff;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
header h1, main h1, main h2 {
    color: #1e90ff;
}
main {
    padding: 40px;
}
nav a {
    color: #1e90ff;
    text-decoration: none;
    margin: 0 15px;
    font-weight: bold;
}
nav a:hover {
    text-decoration: underline;
}
section {
    background: #ffffff;
    margin: 20px 0;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 20px auto;
    border-radius: 8px;
}
"""

# ---------------- FUNKTIONEN ----------------
def update_css():
    CSS_FILE.parent.mkdir(parents=True, exist_ok=True)
    CSS_FILE.write_text(CSS_CONTENT, encoding="utf-8")

def add_images_and_content():
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    for page, content in SUBPAGES.items():
        html_path = ROOT / page
        html = f"""
<html>
<head>
    <meta charset='UTF-8'>
    <title>{content['headline']}</title>
    <link rel='stylesheet' href='assets/css/style.css'>
</head>
<body>
    <nav>
        <a href='index.html'>Home</a> |
        <a href='services.html'>Services</a> |
        <a href='about.html'>About</a> |
        <a href='contact.html'>Contact</a>
    </nav>
    <header>
        <h1>{content['headline']}</h1>
    </header>
    <main>
        <section>
            <p>{content['text']}</p>
            <img src='assets/images/{content['image']}' alt='{content['headline']}'>
        </section>
    </main>
    <footer>
        © 2025 Lukas
    </footer>
</body>
</html>
"""
        html_path.write_text(html, encoding="utf-8")
        # Platzhalterbild erzeugen
        img_path = IMG_DIR / content['image']
        if not img_path.exists():
            img_path.write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + b"\x00"*13 + b"\x00\x00\x00\x00IEND\xaeB`\x82")

# ---------------- MAIN ----------------
def main():
    print("=== BUILD MODERN SUBPAGES + DESIGN ===")
    update_css()
    add_images_and_content()
    print("✅ Unterseiten + Bilder + modernes Design aktualisiert")

if __name__ == "__main__":
    main()
