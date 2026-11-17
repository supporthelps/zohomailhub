
from pathlib import Path
from datetime import date
from urllib.parse import quote
import xml.etree.ElementTree as ET

# =====================================
# ZOHO MAIL XML SITEMAP GENERATOR
# =====================================

ROOT = Path(__file__).parent

# IMPORTANT:
# Replace this with your actual GitHub Pages URL.
BASE_URL ="https://supporthelps.github.io/zohomailhub/"

SITEMAP_FILE = ROOT / "sitemap.xml"

EXCLUDED = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules"
}

def generate_sitemap():

    if "YOUR-USERNAME" in BASE_URL:
        print("ERROR: Please add your actual website URL!")
        return

    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"

    ET.register_namespace("", namespace)

    urlset = ET.Element(
        f"{{{namespace}}}urlset"
    )

    today = date.today().isoformat()

    html_files = [
        file for file in ROOT.rglob("*.html")
        if not any(
            part in EXCLUDED
            for part in file.relative_to(ROOT).parts
        )
    ]

    for file in html_files:

        relative_path = file.relative_to(ROOT).as_posix()

        if relative_path == "index.html":
            url = BASE_URL.rstrip("/") + "/"

        elif relative_path.endswith("/index.html"):
            folder = relative_path.rsplit("/", 1)[0]
            url = BASE_URL.rstrip("/") + "/" + quote(folder, safe="/") + "/"

        else:
            url = (
                BASE_URL.rstrip("/")
                + "/"
                + quote(relative_path, safe="/")
            )

        url_element = ET.SubElement(
            urlset,
            f"{{{namespace}}}url"
        )

        loc = ET.SubElement(
            url_element,
            f"{{{namespace}}}loc"
        )

        loc.text = url

        lastmod = ET.SubElement(
            url_element,
            f"{{{namespace}}}lastmod"
        )

        lastmod.text = today

    tree = ET.ElementTree(urlset)

    ET.indent(tree, space="    ")

    tree.write(
        SITEMAP_FILE,
        encoding="utf-8",
        xml_declaration=True
    )

    print("\nSITEMAP GENERATED SUCCESSFULLY!")
    print("Total HTML pages:", len(html_files))
    print("File location:", SITEMAP_FILE)
    print("Sitemap URL:", BASE_URL.rstrip("/") + "/sitemap.xml")


if __name__ == "__main__":
    generate_sitemap()
