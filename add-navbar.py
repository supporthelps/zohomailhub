
from pathlib import Path
import re
from html import escape
import os

# ==========================================
# WEBSITE NAVBAR MANAGER
# ==========================================

ROOT = Path(__file__).parent

DEFAULT_LINKS = {
    "Home": "index.html",
    "TrollFree No.": "index.html#guides",
    "Login": "#",
    "Support": "#"
}

NAVBAR_CLASS = "zoho-navbar"


def get_html_files():
    excluded = {
        ".git", ".venv", "venv",
        "__pycache__", "node_modules"
    }

    return [
        p for p in ROOT.rglob("*.html")
        if not any(
            part in excluded
            for part in p.relative_to(ROOT).parts
        )
    ]


def get_links():
    print("\nEnter Navbar Links")
    print("Press Enter to keep default link.\n")

    links = {}

    for label, default in DEFAULT_LINKS.items():
        value = input(
            f"{label} URL [{default}]: "
        ).strip()

        links[label] = value or default

    return links


def relative_target(page, target):

    if target.startswith((
        "http://", "https://",
        "mailto:", "tel:", "#"
    )):
        return target

    if target.startswith("/"):
        return target

    destination = ROOT / target.split("#")[0]

    relative = Path(
        os.path.relpath(destination, page.parent)
    ).as_posix()

    if "#" in target:
        relative += "#" + target.split("#", 1)[1]

    return relative


def make_navbar(page, links):

    items = []

    for label, target in links.items():

        href = escape(
            relative_target(page, target),
            quote=True
        )

        safe_label = escape(label)

        css_class = (
            ' class="support-btn"'
            if label.lower() == "support"
            else ""
        )

        items.append(
            f'<a{css_class} href="{href}">'
            f'{safe_label}</a>'
        )

    home = escape(
        relative_target(page, "index.html"),
        quote=True
    )

    return f"""
<nav class="{NAVBAR_CLASS}">
    <a class="zoho-brand" href="{home}">
        <span class="zoho-logo">Z</span>
        <span>Zoho Mail Guide</span>
    </a>

    <div class="zoho-nav-links">
        {"".join(items)}
    </div>
</nav>
"""


def remove_navbar_from_html(html):

    pattern = (
        r'<nav\b(?=[^>]*\bclass=["\']'
        r'[^"\']*\bzoho-navbar\b[^"\']*["\'])'
        r'[^>]*>.*?</nav\s*>'
    )

    return re.sub(
        pattern,
        "",
        html,
        flags=re.I | re.S
    )


def add_or_update_navbar():

    links = get_links()
    files = get_html_files()

    changed = 0

    for page in files:

        html = page.read_text(encoding="utf-8")

        navbar = make_navbar(page, links)

        pattern = (
            r'<nav\b(?=[^>]*\bclass=["\']'
            r'[^"\']*\bzoho-navbar\b[^"\']*["\'])'
            r'[^>]*>.*?</nav\s*>'
        )

        if re.search(pattern, html, flags=re.I | re.S):

            new_html = re.sub(
                pattern,
                lambda match: navbar,
                html,
                count=1,
                flags=re.I | re.S
            )

        else:

            body = re.search(
                r'<body\b[^>]*>',
                html,
                flags=re.I
            )

            if body:

                new_html = (
                    html[:body.end()]
                    + "\n"
                    + navbar
                    + html[body.end():]
                )

            else:

                new_html = navbar + html

        if new_html != html:

            page.write_text(
                new_html,
                encoding="utf-8"
            )

            changed += 1

    print(
        f"\nNavbar added/updated in {changed} HTML files."
    )


def remove_navbar():

    files = get_html_files()
    changed = 0

    for page in files:

        html = page.read_text(encoding="utf-8")

        new_html = remove_navbar_from_html(html)

        if new_html != html:

            page.write_text(
                new_html,
                encoding="utf-8"
            )

            changed += 1

    print(
        f"\nNavbar removed from {changed} HTML files."
    )


def update_links_only():

    links = get_links()
    files = get_html_files()

    changed = 0

    for page in files:

        html = page.read_text(encoding="utf-8")

        new_html = html

        for label, target in links.items():

            href = escape(
                relative_target(page, target),
                quote=True
            )

            pattern = (
                r'(<nav\b[^>]*\bclass=["\']'
                r'[^"\']*\bzoho-navbar\b[^"\']*["\']'
                r'[^>]*>.*?<a\b)([^>]*)(>\s*'
                + re.escape(label)
                + r'\s*</a>)'
            )

            def replace_link(match):

                attrs = match.group(2)

                if re.search(
                    r'\bhref\s*=',
                    attrs,
                    flags=re.I
                ):

                    attrs = re.sub(
                        r'\bhref\s*=\s*(["\']).*?\1',
                        f'href="{href}"',
                        attrs,
                        count=1,
                        flags=re.I
                    )

                else:

                    attrs += f' href="{href}"'

                return (
                    match.group(1)
                    + attrs
                    + match.group(3)
                )

            new_html = re.sub(
                pattern,
                replace_link,
                new_html,
                count=1,
                flags=re.I | re.S
            )

        if new_html != html:

            page.write_text(
                new_html,
                encoding="utf-8"
            )

            changed += 1

    print(
        f"\nLinks updated in {changed} HTML files."
    )


def main():

    print("\n================================")
    print("       NAVBAR MANAGER")
    print("================================")

    print("\n1. Add Navbar / Update Navbar")
    print("2. Remove Navbar")
    print("3. Update Navbar Links")
    print("4. Exit")

    choice = input(
        "\nSelect Option (1-4): "
    ).strip()

    if choice == "1":

        add_or_update_navbar()

    elif choice == "2":

        confirm = input(
            "Remove navbar from all HTML files? (y/n): "
        ).lower()

        if confirm == "y":
            remove_navbar()
        else:
            print("Cancelled.")

    elif choice == "3":

        update_links_only()

    elif choice == "4":

        print("Exited.")

    else:

        print("Invalid Option!")


if __name__ == "__main__":
    main()
