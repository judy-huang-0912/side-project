from playwright.sync_api import sync_playwright

def run(playwright):
    # 啟動瀏覽器（虛擬模式）
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # 打開新頁面
    page = context.new_page()

    # 瀏覽到指定的 URL
    page.goto("https://www.momoshop.com.tw/main/Main.jsp")

    page.pause()
    # 關閉瀏覽器
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
