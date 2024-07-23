from playwright.sync_api import sync_playwright
#從 Playwright 中導入函式庫和類別
import time #導入time 模組，目的為控制程式執行速度，讓程式暫停一定的時間。
from datetime import datetime # 從 datetime 模組中引入 datetime 類，處理日期和時間。
from line_api import line_notify
target_time = "2024-07-03 9:50:00"  #目標時間：日期以及時間

def wait_until_target_time(target_time_str):
    target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
    while datetime.now() < target_time:
        print('waiting')
        time.sleep(1)


def test_fly():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://www.mandarin-airlines.com/b2c/bookingpaylater')
            page.click('#trip_oneway')
            page.select_option('#departureCity1','TSA')
            page.select_option('#arrivalCity1', 'KNH')
            page.evaluate("""
                const deptDateInput = document.querySelector('#deptDate4');
                deptDateInput.removeAttribute('readonly');
                deptDateInput.value = '2024-08-01';
            """)
            page.click('button.indexbtn')
            page.locator('.booking-list .booking-box .bookingbt').nth(1).click()
            page.locator('input#iagree').check()
            page.locator('div.btn.btn-go[onclick="javascript:doSubmit()"]').click()
            page.locator('input#lastName1').fill('Manto')
            page.locator('input#firstName1').fill('Teacher')
            page.locator('select#PassengerIdx').select_option(value="1")
            page.locator('input#contactName').fill('Cookies hsu')
            page.locator('input#mobile').fill('0912345678')
            email_field = page.locator("#email")
            email_field.fill("judy311170@gmail.com")
            phone_field = page.locator("#phone")
            phone_field.fill("0912345678")
            delay_payment_button = page.locator('div.btn.btn-go[onclick="CheckForm()"]')
            delay_payment_button.click()

            # 擷取航班資訊
            flight_number = page.locator('.pnr-part > p').text_content()
            flight_class = page.locator('.pnr-type > p').text_content()
            departure_city = page.locator('.pnr-airport').nth(0).locator('p').text_content()
            arrival_city = page.locator('.pnr-airport').nth(1).locator('p').text_content()
            departure_time = page.locator('.pnr-time').nth(0).locator('p').text_content()
            arrival_time = page.locator('.pnr-time').nth(1).locator('p').text_content()
            booking_status = page.locator('.pnr-show01 > p').text_content()

            flight_info = f"航班資訊:\n航班號碼: {flight_number}\n艙等: {flight_class}\n出發地: {departure_city}\n目的地: {arrival_city}\n起飛時間: {departure_time}\n抵達時間: {arrival_time}\n訂位狀態: {booking_status}"
            print("訂票流程完成")
            browser.close()
            return True, flight_info

    except Exception as e:
        print(f"自動化訂票失敗: {e}")
        return False, str(e)

if __name__ == '__main__':
    wait_until_target_time(target_time)
    success, message = test_fly()
    if success:
        line_notify(f'自動訂票成功\n{message}')
    else:
        line_notify(f'自動訂票失敗\n{message}')
