import json
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import re

load_dotenv()
COOKIE_STRING = os.getenv('COOKIE_STRING')
cookies = []

for cookie in COOKIE_STRING.split('; '):
    name, value = cookie.split('=', 1)
    cookies.append({
        'name': name,
        'value': value,
        'domain': 'scr.cyc.org.tw',
        'path': '/',
        'httpOnly': False,
        'secure': False,
    })
def test_login_with_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.add_cookies(cookies)
        page = context.new_page()
        page.goto('https://scr.cyc.org.tw/tp01.aspx')
        page.wait_for_load_state('networkidle')
        element_selector = '#lab_Name'
        page.wait_for_selector(element_selector)
        element_text = page.text_content(element_selector)
        pattern = re.compile(r'\w+ 您好')
        match = pattern.search(element_text)
        assert match is not None, f"Expected text pattern not found in {element_text}"
        print("Element verified successfully with regex pattern.")
