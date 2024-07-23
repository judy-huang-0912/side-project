import json
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

# 获取环境变量
COOKIE_STRING = os.getenv('COOKIE_STRING')
cookies = []

for cookie in cookie_string.split('; '):
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
def login_with_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.add_cookies(cookies)

        page = context.new_page()
        page.goto('https://scr.cyc.org.tw/tp01.aspx')  # 替換成你的網站
        page.wait_for_load_state('networkidle')
        page.pause()

        # 在這裡你可以檢查是否成功登入，例如檢查用戶名是否顯示在頁面上
        print(page.title())

        # 關閉瀏覽器
        browser.close()

if __name__ == '__main__':
    login_with_cookies()

