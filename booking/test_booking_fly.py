import pytest
from playwright.sync_api import Page

@pytest.fixture
def browser(page: Page):
    # 可以在这里配置浏览器，例如启用或禁用 headless 模式
    page.goto('https://www.mandarin-airlines.com/b2c/bookingpaylater')
    return page

def test_fly(browser):
    """执行自动化订票测试"""
    page = browser

    # 点击单程票选项
    page.click('#trip_oneway')

    # 选择出发城市和到达城市
    page.select_option('#departureCity1', 'TSA')
    page.select_option('#arrivalCity1', 'KNH')
    departure_city = page.locator('#departureCity1').input_value()
    arrival_city = page.locator('#arrivalCity1').input_value()
    assert departure_city == 'TSA'
    assert arrival_city == 'KNH'

    # 设置出发日期
    page.evaluate("""
        const deptDateInput = document.querySelector('#deptDate4');
        deptDateInput.removeAttribute('readonly');
        deptDateInput.value = '2024-09-30';
    """)
    dept_date = page.locator('#deptDate4').input_value()
    assert dept_date == '2024-09-30'

    # 点击搜索按钮
    page.click('button.indexbtn')

    # 等待并验证预订按钮的可见性
    page.wait_for_selector('.booking-list .booking-box .bookingbt', timeout=10000)
    booking_button_visible = page.locator('.booking-list .booking-box .bookingbt').nth(1).is_visible()
    assert booking_button_visible

    # 点击预订按钮
    page.locator('.booking-list .booking-box .bookingbt').nth(1).click()

    # 确认乘客同意条款
    page.locator('input#iagree').check()
    assert page.is_checked('input#iagree')

    # 点击提交按钮
    page.locator('div.btn.btn-go[onclick="javascript:doSubmit()"]').click()

    # 填写乘客信息
    page.locator('input#lastName1').fill('Manto')
    page.locator('input#firstName1').fill('Teacher')
    page.locator('select#PassengerIdx').select_option(value="1")
    page.locator('input#contactName').fill('Cookies Hsu')
    page.locator('input#mobile').fill('0912345678')
    email_field = page.locator("#email")
    email_field.fill("judy311170@gmail.com")
    phone_field = page.locator("#phone")
    phone_field.fill("0912345678")

    # 点击延迟付款按钮
    delay_payment_button = page.locator('div.btn.btn-go[onclick="CheckForm()"]')
    assert delay_payment_button.is_visible()
    delay_payment_button.click()

    # 读取并验证航班信息
    flight_number = page.locator('.pnr-part > p').text_content()
    flight_class = page.locator('.pnr-type > p').text_content()
    departure_city = page.locator('.pnr-airport').nth(0).locator('p').text_content()
    arrival_city = page.locator('.pnr-airport').nth(1).locator('p').text_content()
    departure_time = page.locator('.pnr-time').nth(0).locator('p').text_content()
    arrival_time = page.locator('.pnr-time').nth(1).locator('p').text_content()
    booking_status = page.locator('.pnr-show01 > p').text_content()

    flight_info = (f"航班資訊:\n"
                   f"航班號碼: {flight_number}\n"
                   f"艙等: {flight_class}\n"
                   f"出發地: {departure_city}\n"
                   f"目的地: {arrival_city}\n"
                   f"起飛時間: {departure_time}\n"
                   f"抵達時間: {arrival_time}\n"
                   f"訂位狀態: {booking_status}")

    print("訂票流程完成")
    assert flight_number  # Ensure flight number is not empty
    assert flight_class  # Ensure flight class is not empty
    # Add more assertions as needed

