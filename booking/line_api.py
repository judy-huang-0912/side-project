import unittest
from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import requests
import os
from dotenv import load_dotenv


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

def wait_until_target_time(target_time_str):
    target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
    while datetime.now() < target_time:
        print('waiting')
        time.sleep(1)

class TestFlyEndToEnd(unittest.TestCase):
    def setUp(self):
        """Set up the testing environment."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def tearDown(self):
        """Clean up the testing environment."""
        self.browser.close()
        self.playwright.stop()

    def test_end_to_end_booking(self):
        """End-to-end test for booking process."""
        try:
            wait_until_target_time("2024-07-03 09:50:00")
            self.page.goto('https://www.mandarin-airlines.com/b2c/bookingpaylater')
            expected_title = "華信航空 Mandarin Airlines"
            self.assertEqual(self.page.title(), expected_title, f"Expected title '{expected_title}' but got '{self.page.title()}'")
            self.assertTrue(self.page.is_visible('#trip_oneway'))
            self.assertTrue(self.page.is_visible('#departureCity1'))
            self.assertTrue(self.page.is_visible('#arrivalCity1'))
            self.assertTrue(self.page.is_visible('#deptDate4'))
            self.assertTrue(self.page.is_visible('button.indexbtn'))
            self.page.click('#trip_oneway')
            self.assertTrue(self.page.is_checked('#trip_oneway'))
            self.page.select_option('#departureCity1', 'TSA')
            self.page.select_option('#arrivalCity1', 'KNH')
            departure_city = self.page.locator('#departureCity1').input_value()
            arrival_city = self.page.locator('#arrivalCity1').input_value()
            self.assertEqual(departure_city, 'TSA')
            self.assertEqual(arrival_city, 'KNH')
            self.page.evaluate("""
                const deptDateInput = document.querySelector('#deptDate4');
                deptDateInput.removeAttribute('readonly');
                deptDateInput.value = '2024-09-30';
            """)
            dept_date = self.page.locator('#deptDate4').input_value()
            self.assertEqual(dept_date, '2024-09-30')
            self.page.click('button.indexbtn')
            self.assertTrue(self.page.locator('button.indexbtn').is_visible())
            flight_info_visible = self.page.is_visible('.flight-info-selector')
            self.assertTrue(flight_info_visible)
            flight_number = self.page.locator('.flight-number-selector').text_content()
            self.assertIsNotNone(flight_number)
            flight_class = self.page.locator('.flight-class-selector').text_content()
            departure_time = self.page.locator('.departure-time-selector').text_content()
            arrival_time = self.page.locator('.arrival-time-selector').text_content()
            self.assertIsNotNone(flight_class)
            self.assertIsNotNone(departure_time)
            self.assertIsNotNone(arrival_time)
            self.page.wait_for_selector('.booking-list .booking-box .bookingbt', timeout=10000)
            booking_button_visible = self.page.locator('.booking-list .booking-box .bookingbt').nth(1).is_visible()
            self.assertTrue(booking_button_visible)
            self.page.locator('.booking-list .booking-box .bookingbt').nth(1).click()
            self.page.locator('input#lastName1').fill('Manto')
            self.page.locator('input#firstName1').fill('Teacher')
            self.page.locator('select#PassengerIdx').select_option(value="1")
            self.page.locator('input#contactName').fill('Cookies Hsu')
            self.page.locator('input#mobile').fill('0912345678')
            self.page.locator('#email').fill('judy311170@gmail.com')
            self.page.locator('#phone').fill('0912345678')
            delay_payment_button = self.page.locator('div.btn.btn-go[onclick="CheckForm()"]')
            self.assertTrue(delay_payment_button.is_visible())
            delay_payment_button.click()
            flight_number = self.page.locator('.pnr-part > p').text_content()
            flight_class = self.page.locator('.pnr-type > p').text_content()
            departure_city = self.page.locator('.pnr-airport').nth(0).locator('p').text_content()
            arrival_city = self.page.locator('.pnr-airport').nth(1).locator('p').text_content()
            departure_time = self.page.locator('.pnr-time').nth(0).locator('p').text_content()
            arrival_time = self.page.locator('.pnr-time').nth(1).locator('p').text_content()
            booking_status = self.page.locator('.pnr-show01 > p').text_content()

            self.assertIsNotNone(flight_number)
            self.assertIsNotNone(flight_class)
            self.assertIsNotNone(departure_city)
            self.assertIsNotNone(arrival_city)
            self.assertIsNotNone(departure_time)
            self.assertIsNotNone(arrival_time)
            self.assertIsNotNone(booking_status)

            flight_info = (
                f"航班資訊:\n"
                f"航班號碼: {flight_number}\n"
                f"艙等: {flight_class}\n"
                f"出發地: {departure_city}\n"
                f"目的地: {arrival_city}\n"
                f"起飛時間: {departure_time}\n"
                f"抵達時間: {arrival_time}\n"
                f"訂位狀態: {booking_status}"
            )
            print(flight_info)

            line_notify(flight_info)
            print("訂票流程完成")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

if __name__ == "__main__":
    unittest.main()

