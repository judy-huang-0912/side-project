import json
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import re

load_dotenv()

# 获取环境变量
COOKIE_STRING = os.getenv('COOKIE_STRING')
cookies = []

for cookie in COOKIE_STRING.split('; '):
    name, value = cookie.split('=', 1)
    cookies.append({
        'name': name,
        'value': value,
        'domain': 'scr.cyc.org.tw',  # 替換成你的域名
        'path': '/',
        'httpOnly': False,
        'secure': False,
    })

# 使用 Playwright 加載 cookies 登入網站
def test_login_with_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.add_cookies(cookies)
        page = context.new_page()
        page.goto('https://scr.cyc.org.tw/tp01.aspx')  # 替換成你的網站
        page.wait_for_load_state('networkidle')
        element_selector = '#lab_Name'
        page.wait_for_selector(element_selector)
            # 取得目標元素的文本內容
        element_text = page.text_content(element_selector)
            # 使用正則表達式來檢查文本內容
        pattern = re.compile(r'\w+ 您好')  # 示例正則表達式，可以根據實際情況進行調整
        match = pattern.search(element_text)
            # 進行斷言驗證
        assert match is not None, f"Expected text pattern not found in {element_text}"
        print("Element verified successfully with regex pattern.")

def test_cookies_in_headers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.add_cookies(cookies)

        # 設置頁面，並在頁面加載完成後捕獲響應
        page = context.new_page()

        # 設置響應監聽器
        def response_callback(response):
            nonlocal response_headers
            if 'set-cookie' in response.headers:
                response_headers = response.headers

        response_headers = None
        page.on('response', response_callback)

        page.goto('https://scr.cyc.org.tw/tp01.aspx')  # 替換成你的網站
        page.wait_for_load_state('networkidle')

        # 等待並確認捕獲到響應
        if response_headers:
            # 檢查 headers 是否包含 cookies
            cookie_found = any(
                cookie in response_headers.get('set-cookie', '')
                for cookie in (cookie['name'] + '=' + cookie['value'] for cookie in cookies)
            )

            assert cookie_found, "Cookies not found in response headers"
            print("Cookies found in response headers.")
        else:
            print("No response with 'set-cookie' headers found.")

