from playwright.sync_api import sync_playwright

def test_get_request():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser in non-headless mode
        context = browser.new_context()
        page = context.new_page()

        # 设置网络请求拦截器
        def handle_request(route, request):
            if request.method == 'GET' and 'search' in request.url and 'q=%E5%92%96%E6%B3%A2' in request.url:
                print(f"GET Request URL: {request.url}")
                print("GET request parameter is correct!")
            route.continue_()

        page.route('**/*', handle_request)

        # 打开 Google 搜索页面
        page.goto('https://www.google.com')

        # 输入搜索关键词并提交
        search_box = page.locator('input#input.truncate')
        search_box.fill('咖波')
        search_box.press('Enter')

        # 等待搜索结果加载
        page.wait_for_selector('#search')

        # 关闭浏览器
        browser.close()

if __name__ == "__main__":
    test_get_request()


