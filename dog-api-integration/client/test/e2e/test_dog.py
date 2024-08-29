from playwright.sync_api import sync_playwright

def test_dog_image():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 啟動瀏覽器（chromium-屬性）可以看到實際頁面的操作。
        page = browser.new_page()  # 建立新頁面，可以透過page進行頁面上各種操作
        page.goto('http://127.0.0.1:3000/dog')

        # 確認標題存在且內容為 "Dog Images"
        title = page.text_content('h1')
        assert title == "Dog Images", f"Expected 'Dog Images', but got '{title}'"

        # 確認圖片載入
        page.wait_for_selector('#dog-images img', timeout=10000)  # 等待圖片元素載入，超時設為10秒

        # 確認是否有圖片元素
        images = page.query_selector_all('#dog-images img')
        assert len(images) > 0, "No images found on the page."

        print(f"Found {len(images)} images on the page.")

        page.pause()
        browser.close()

if __name__ == '__main__':
    test_dog_image()

