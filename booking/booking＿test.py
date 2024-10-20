from playwright.sync_api import sync_playwright
import time
from datetime import datetime
from dotenv import load_dotenv
import os
import requests

load_dotenv()
LINE_TOKEN = os.getenv('LINE_TOKEN')

def line_notify(msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + LINE_TOKEN
    }
    data = {
        'message': msg,
        "stickerPackageId": 6370,
        "stickerId": 11088018
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Line Notify 成功")
    else:
        print(f"Line Notify 失敗: {response.status_code}, {response.text}")

target_time = "2024-07-31 22:01:00"

def wait_until_target_time(target_time_str):
    target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
    while datetime.now() < target_time:
        print('waiting')
        time.sleep(1)

def run_page_one(page):
    page.goto('https://www.mandarin-airlines.com/b2c/bookingpaylater')
    assert page.url == 'https://www.mandarin-airlines.com/b2c/bookingpaylater'
    page.wait_for_load_state('networkidle')
    assert page.evaluate("document.readyState") == "complete"
    page.click('#trip_oneway')
    page.select_option('#departureCity1', 'TSA')
    page.select_option('#arrivalCity1', 'KNH')
    departure_city = page.locator('#departureCity1').input_value()
    arrival_city = page.locator('#arrivalCity1').input_value()
    assert departure_city == 'TSA'
    assert arrival_city == 'KNH'
    page.evaluate("""
        const deptDateInput = document.querySelector('#deptDate4');
        deptDateInput.removeAttribute('readonly');
        deptDateInput.value = '2024-09-30';
    """)
    dept_date = page.locator('#deptDate4').input_value()
    assert dept_date == '2024-09-30'
    page.click('button.indexbtn')

def run_page_two(page):
    page.wait_for_selector('.booking-list .booking-box .bookingbt', timeout=10000)
    booking_button_visible = page.locator('.booking-list .booking-box .bookingbt').nth(1).is_visible()#改寫用for迴圈判斷
    assert booking_button_visible
    page.locator('.booking-list .booking-box .bookingbt').nth(1).click()
    page.locator('input#iagree').check()
    assert page.is_checked('input#iagree')
    page.locator('div.btn.btn-go[onclick="javascript:doSubmit()"]').click()

def run_page_three(page):
    page.locator('input#lastName1').fill('Manto')
    page.locator('input#firstName1').fill('Teacher')
    page.locator('select#PassengerIdx').select_option(value="1")
    page.locator('input#contactName').fill('Cookies Hsu')
    page.locator('input#mobile').fill('0912345678')
    email_field = page.locator("#email")
    email_field.fill("judy311170@gmail.com")
    phone_field = page.locator("#phone")
    phone_field.fill("0912345678")

    delay_payment_button = page.locator('div.btn.btn-go[onclick="CheckForm()"]')
    assert delay_payment_button.is_visible()
    delay_payment_button.click()
    flight_number = page.locator('.pnr-part > p').text_content()
    flight_class = page.locator('.pnr-type > p').text_content()
    departure_city = page.locator('.pnr-airport').nth(0).locator('p').text_content()
    arrival_city = page.locator('.pnr-airport').nth(1).locator('p').text_content()
    departure_time = page.locator('.pnr-time').nth(0).locator('p').text_content()
    arrival_time = page.locator('.pnr-time').nth(1).locator('p').text_content()
    booking_status = page.locator('.pnr-show01 > p').text_content()

    flight_info = f"航班資訊:\n航班號碼: {flight_number}\n艙等: {flight_class}\n出發地: {departure_city}\n目的地: {arrival_city}\n起飛時間: {departure_time}\n抵達時間: {arrival_time}\n訂位狀態: {booking_status}"
    print("訂票完成")
    return flight_info

def test_fly():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            assert browser

            page = browser.new_page()
            assert page

            run_page_one(page)
            run_page_two(page)
            flight_info = run_page_three(page)

            browser.close()
            return True, flight_info

    except Exception as e:
        print(f"訂票失敗: {e}")
        return False, str(e)

if __name__ == '__main__':
    wait_until_target_time(target_time)
    success, message = test_fly()
    if success:
        line_notify(f'訂票成功\n{message}')
    else:
        line_notify(f'訂票失敗\n{message}')
