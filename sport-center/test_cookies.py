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
