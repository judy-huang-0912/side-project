from playwright.sync_api import sync_playwright

def test_dog_image():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://localhost:3000/dog')
        title = page.text_content('h1')
        assert title == "Dog Images", f"Expected 'Dog Images', but got '{title}'"
        page.wait_for_selector('#dog-images img', timeout=10000)
        images = page.query_selector_all('#dog-images img')
        assert len(images) > 0, "No images found on the page."

        print(f"Found {len(images)} images on the page.")

        browser.close()

if __name__ == '__main__':
    test_dog_image()

