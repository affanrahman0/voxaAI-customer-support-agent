from playwright.sync_api import sync_playwright
from pathlib import Path

HELP_URLS = [
    "https://www.amazon.in/gp/help/customer/display.html?nodeId=201889410",
    "https://www.amazon.in/gp/help/customer/display.html?nodeId=202111910",
    "https://www.amazon.in/gp/help/customer/display.html?nodeId=200545940",
]

OUT_DIR = Path("backend/data/raw/amazon")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def scrape_amazon_help():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for url in HELP_URLS:
            print(f"[+] Loading {url}")
            page.goto(url, timeout=60000)
            page.wait_for_timeout(5000)

            text = page.inner_text("body")

            node_id = url.split("nodeId=")[-1]
            file = OUT_DIR / f"amazon_{node_id}.txt"
            file.write_text(text, encoding="utf-8")

            print(f"[✓] Saved {file.name}")

        browser.close()

if __name__ == "__main__":
    scrape_amazon_help()
