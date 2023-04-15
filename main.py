from browser import Browser

def main():
    website_url = input("Enter website url: ")
    with Browser() as browser:
        browser.go_to_website(website_url)
        input("Press enter when you have logged in")
        browser.save_cookies()
    print("Saved cookies!")
    input("Press enter to exit...")

if __name__ == "__main__":
    main()