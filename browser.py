from cookies_path import COOKIES_FILE_PATH
from pathlib import Path

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class Browser:

    DEBUGGING_PORT: str = "8797"

    def __init__(self):
        self.browser: webdriver.Chrome = None

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit()

    def __del__(self):
        self.exit()

    def setup(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument(f"--remote-debugging-port={Browser.DEBUGGING_PORT}")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-gpu")

        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), service_log_path=Path("NUL"), options=options)

    def go_to_website(self, website_url: str) -> None:
        self.browser.get(website_url if website_url.startswith("https://") else "https://" + website_url)

    def save_cookies(self) -> None:
        with open(COOKIES_FILE_PATH, "w", encoding="utf-8") as f:
            f.write(str(self.browser.get_cookies()))

    def exit(self) -> None:
        if self.browser is None:
            return
        self.browser.close()
        self.browser.quit()
        print("Closed browser and released all resources")
