
from pathlib import Path
from html.parser import HTMLParser
import re

ROOT = Path(__file__).parent
INDEX = ROOT / "index.html"

CONTENT = """
<!-- ZOHO MAIL CONTENT START -->

<section class="zoho-extra-content">

<style>
.zoho-extra-content {
    max-width: 1180px;
    margin: 45px auto;
    padding: 0 24px 45px;
    font-family: 'DM Sans', Arial, sans-serif;
    color: #1b2540;
}

.zoho-extra-content .content-heading {
    text-align: center;
    margin-bottom: 30px;
}

.zoho-extra-content .content-heading span {
    color: #526cf5;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.zoho-extra-content h2 {
    color: #17213c;
    font-family: 'Manrope', Arial, sans-serif;
    font-size: 29px;
    line-height: 1.3;
    margin: 10px 0;
    letter-spacing: -1px;
}

.zoho-extra-content p {
    color: #69748b;
    font-size: 14px;
    line-height: 1.85;
}

.zoho-intro-card {
    background: #ffffff;
    border: 1px solid #e5e9f2;
    border-radius: 15px;
    padding: 30px;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px #18264a08;
}

.zoho-extra-content .content-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 25px 0 35px;
}

.zoho-extra-content .content-card {
    background: #ffffff;
    border: 1px solid #e5e9f2;
    border-radius: 13px;
    padding: 23px;
    transition: .2s;
}

.zoho-extra-content .content-card:hover {
    transform: translateY(-4px);
    border-color: #bfc9ff;
    box-shadow: 0 12px 25px #263a7710;
}

.zoho-extra-content .content-icon {
    width: 43px;
    height: 43px;
    display: grid;
    place-items: center;
    background: #eef0ff;
    color: #526cf5;
    border-radius: 11px;
    font-size: 20px;
    margin-bottom: 15px;
}

.zoho-extra-content h3 {
    color: #263454;
    font-family: 'Manrope', Arial, sans-serif;
    font-size: 16px;
    margin: 8px 0;
}

.zoho-info-section {
    padding: 28px;
    background: #ffffff;
    border: 1px solid #e5e9f2;
    border-radius: 14px;
    margin: 22px 0;
}

.zoho-info-section h2 {
    font-size: 23px;
}

.zoho-feature-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-top: 20px;
}

.zoho-feature {
    padding: 14px;
    background: #f5f7fc;
    border-radius: 9px;
    color: #475675;
    font-size: 13px;
    font-weight: 600;
}

.zoho-faq-item {
    padding: 18px 0;
    border-bottom: 1px solid #e8ebf2;
}

.zoho-faq-item h3 {
    font-size: 15px;
}

.zoho-final-banner {
    margin-top: 30px;
    padding: 30px;
    border-radius: 15px;
    color: white;
    background: linear-gradient(
        115deg, #101a35, #263a77
    );
}

.zoho-final-banner h2 {
    color: white;
}

.zoho-final-banner p {
    color: #c3cce2;
}

@media(max-width:750px) {
    .zoho-extra-content .content-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media(max-width:500px) {
    .zoho-extra-content .content-grid,
    .zoho-feature-list {
        grid-template-columns: 1fr;
    }

    .zoho-intro-card,
    .zoho-info-section {
        padding: 20px;
    }

    .zoho-extra-content h2 {
        font-size: 24px;
    }
}
</style>

<div class="zoho-intro-card">
    <div class="content-heading">
        <span>WELCOME TO ZOHO MAIL GUIDE</span>
        <h2>Discover Professional Email Solutions</h2>
    </div>

    <p>
        Zoho Mail is an email platform designed to support
        personal and professional communication. Businesses
        can explore professional email hosting, custom domain
        addresses, mailbox management and productivity tools
        for their everyday communication requirements.
    </p>

    <p>
        This website provides informational resources about
        Zoho Mail features, account access, business email
        configuration, security practices and common
        troubleshooting topics. Explore our guides to
        understand different email management options.
    </p>
</div>

<div class="content-heading">
    <span>EXPLORE OUR RESOURCES</span>
    <h2>Explore Zoho Mail Features and Services</h2>
    <p>Learn about important tools and services for managing
    your professional email communication.</p>
</div>

<div class="content-grid">

    <div class="content-card">
        <div class="content-icon">✉</div>
        <h3>Business Email Hosting</h3>
        <p>
            Understand professional email hosting,
            custom domain addresses and mailbox
            management for businesses.
        </p>
    </div>

    <div class="content-card">
        <div class="content-icon">⚙</div>
        <h3>Email Configuration</h3>
        <p>
            Explore email settings, domain verification,
            DNS configuration and supported email
            application setup.
        </p>
    </div>

    <div class="content-card">
        <div class="content-icon">🔒</div>
        <h3>Email Security</h3>
        <p>
            Learn about password protection, spam
            filtering, phishing awareness and
            account security practices.
        </p>
    </div>

    <div class="content-card">
        <div class="content-icon">📱</div>
        <h3>Mobile Email Access</h3>
        <p>
            Understand mobile email access, account
            synchronization and mailbox management
            on compatible devices.
        </p>
    </div>

    <div class="content-card">
        <div class="content-icon">📅</div>
        <h3>Productivity Tools</h3>
        <p>
            Discover calendar, contacts, tasks,
            folders and other email productivity
            features.
        </p>
    </div>

    <div class="content-card">
        <div class="content-icon">🏢</div>
        <h3>Business Administration</h3>
        <p>
            Learn about administrative settings,
            user management, domain configuration
            and business email organization.
        </p>
    </div>

</div>

<div class="zoho-info-section">
    <h2>Why Explore Zoho Mail for Business?</h2>

    <p>
        Professional email communication is an important
        part of business operations. A business email
        platform can help organizations manage internal
        and external communication using professional
        email addresses.
    </p>

    <div class="zoho-feature-list">
        <div class="zoho-feature">✓ Custom Domain Email</div>
        <div class="zoho-feature">✓ Organized Email Management</div>
        <div class="zoho-feature">✓ Calendar and Contacts</div>
        <div class="zoho-feature">✓ Email Security Features</div>
        <div class="zoho-feature">✓ Business Communication</div>
        <div class="zoho-feature">✓ Mobile Email Access</div>
    </div>
</div>

<div class="zoho-info-section">
    <h2>Zoho Mail Account Setup and Management</h2>

    <p>
        Getting started with a business email service
        involves understanding account registration,
        domain configuration and mailbox settings.
        Users can explore informational guides covering
        account creation, sign-in, inbox access,
        email forwarding, filters and account recovery.
    </p>

    <h3>Managing Your Email Inbox</h3>
    <p>
        An organized inbox makes everyday communication
        easier to manage. Email folders, filters,
        search options and attachment management can
        help users organize important messages.
    </p>

    <h3>Configuring a Custom Business Domain</h3>
    <p>
        Custom domain email configuration generally
        involves domain ownership verification and
        appropriate DNS records. Correct configuration
        helps route email messages to the intended
        mail service.
    </p>
</div>

<div class="zoho-info-section">
    <h2>Email Security and Privacy</h2>

    <p>
        Protecting business communication requires
        good account security practices. Users should
        create strong passwords, enable available
        two-factor authentication, review suspicious
        messages and avoid sharing confidential
        account information.
    </p>

    <p>
        Understanding spam protection, phishing
        prevention and account recovery procedures
        can help users maintain safer email usage.
    </p>
</div>

<div class="zoho-info-section">
    <h2>Frequently Asked Questions</h2>

    <div class="zoho-faq-item">
        <h3>What is Zoho Mail used for?</h3>
        <p>
            Zoho Mail is used for email communication,
            mailbox organization and professional
            business email management.
        </p>
    </div>

    <div class="zoho-faq-item">
        <h3>Does Zoho Mail support custom domains?</h3>
        <p>
            Zoho Mail provides custom domain email
            options on supported business plans.
        </p>
    </div>

    <div class="zoho-faq-item">
        <h3>Can I access Zoho Mail on mobile?</h3>
        <p>
            Users can access supported mobile
            applications and compatible devices
            to manage their email.
        </p>
    </div>

    <div class="zoho-faq-item">
        <h3>Where can I find Zoho Mail guides?</h3>
        <p>
            Explore the article collection on this
            website for informational resources
            about email setup, account access,
            security and troubleshooting.
        </p>
    </div>
</div>

<div class="zoho-final-banner">
    <h2>Explore More Zoho Mail Resources</h2>
    <p>
        Browse our collection of informational articles
        to learn about business email hosting, account
        management, email configuration, security and
        productivity features.
    </p>
</div>

</section>

<!-- ZOHO MAIL CONTENT END -->
"""


class HeroFinder(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=False)
        self.html = html
        self.stack = []
        self.hero_end = None
        self.offsets = [0]

        for line in html.splitlines(keepends=True):
            self.offsets.append(
                self.offsets[-1] + len(line)
            )

    def get_offset(self):
        line, col = self.getpos()
        return self.offsets[line - 1] + col

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = attributes.get("class", "").split()

        is_hero = "hero" in classes

        self.stack.append((tag, is_hero))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                matched = self.stack[i:]

                if any(item[1] for item in matched):
                    if self.hero_end is None:
                        self.hero_end = self.get_offset()

                self.stack = self.stack[:i]
                break


def main():

    if not INDEX.exists():
        print("ERROR: index.html not found!")
        return

    html = INDEX.read_text(encoding="utf-8")

    if "ZOHO MAIL CONTENT START" in html:
        print("Content already exists!")
        return

    finder = HeroFinder(html)
    finder.feed(html)

    if finder.hero_end is None:
        print("Hero section not found!")
        print('Check that your HTML has class="hero".')
        return

    close_tag = re.match(
        r"</\s*(section|div)\s*>",
        html[finder.hero_end:],
        flags=re.I
    )

    if not close_tag:
        print("Could not locate hero closing tag.")
        return

    insert_position = (
        finder.hero_end + close_tag.end()
    )

    new_html = (
        html[:insert_position]
        + "\n"
        + CONTENT
        + "\n"
        + html[insert_position:]
    )

    INDEX.write_text(
        new_html,
        encoding="utf-8"
    )

    print("Zoho Mail homepage content added!")
    print("Position: Immediately below hero section.")
    print("Existing article section preserved.")


if __name__ == "__main__":
    main()
