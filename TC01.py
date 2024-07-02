import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Fixture to set up the browser
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_automation_exercise(browser):
    # Step 2: Navigate to URL 'http://automationexercise.com'
    browser.get('http://automationexercise.com')

    # Step 3: Verify that the home page is visible successfully
    assert 'Automation Exercise' in browser.title

    # Step 4: Add products to the cart
    browser.find_element(By.XPATH, "//a[text()='Products']").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='features_items']/div[1]//a[contains(text(),'Add to cart')]"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue Shopping')]"))
    ).click()

    # Step 5: Click the 'Cart' button
    browser.find_element(By.XPATH, "//ul[contains(@class, 'nav navbar-nav')]//a[contains(@href,'view_cart')]").click()

    # Step 6: Verify that the cart page is displayed
    assert 'Shopping Cart' in browser.page_source

    # Step 7: Click Proceed To Checkout
    browser.find_element(By.XPATH, "//a[text()='Proceed To Checkout']").click()

    # Step 8: Click the 'Register / Login' button
    browser.find_element(By.XPATH, "//u[text()='Register / Login']").click()

    # Step 9: Fill all details in Sign up and create an account
    browser.find_element(By.NAME, 'name').send_keys('Forhad Hossain')
    browser.find_element(By.NAME, 'email').send_keys('forhad2097@gmail.com')
    browser.find_element(By.XPATH, "//button[text()='Signup']").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'id_gender1'))
    ).click()
    browser.find_element(By.ID, 'password').send_keys('password')
    browser.find_element(By.ID, 'days').send_keys('1')
    browser.find_element(By.ID, 'months').send_keys('January')
    browser.find_element(By.ID, 'years').send_keys('2020')
    browser.find_element(By.ID, 'newsletter').click()
    browser.find_element(By.ID, 'optin').click()
    browser.find_element(By.NAME, 'first_name').send_keys('Forhad')
    browser.find_element(By.NAME, 'last_name').send_keys('Hossain')
    browser.find_element(By.NAME, 'company').send_keys('KAZ Software')
    browser.find_element(By.NAME, 'address1').send_keys('Adabor')
    browser.find_element(By.NAME, 'address2').send_keys('Dhaka')
    browser.find_element(By.NAME, 'country').send_keys('United States')
    browser.find_element(By.NAME, 'state').send_keys('Dhaka')
    browser.find_element(By.NAME, 'city').send_keys('Dhaka')
    browser.find_element(By.NAME, 'zipcode').send_keys('1207')
    browser.find_element(By.NAME, 'mobile_number').send_keys('01684022052')
    browser.find_element(By.XPATH, "//button[text()='Create Account']").click()

    # Step 10: Verify 'ACCOUNT CREATED!' and click the 'Continue' button
    assert 'ACCOUNT CREATED!' in browser.page_source
    browser.find_element(By.XPATH, "//a[text()='Continue']").click()

    # Step 11: Verify 'Logged in as username' at top
    assert 'Logged in as Test User' in browser.page_source

    # Step 12: Click the 'Cart' button
    browser.find_element(By.XPATH, "//a[text()='Cart']").click()

    # Step 13: Click the 'Proceed To Checkout' button
    browser.find_element(By.XPATH, "//a[text()='Proceed To Checkout']").click()

    # Step 14: Verify Address Details and Review Your Order
    assert 'Address Details' in browser.page_source
    assert 'Review Your Order' in browser.page_source

    # Step 15: Enter the description in a comment text area and click 'Place Order'
    browser.find_element(By.NAME, 'message').send_keys('Please deliver between 9 AM to 5 PM')
    browser.find_element(By.XPATH, "//a[text()='Place Order']").click()

    # Step 16: Enter payment details: Name on Card, Card Number, CVC, Expiration date
    browser.find_element(By.NAME, 'name_on_card').send_keys('Forhad Hossain')
    browser.find_element(By.NAME, 'card_number').send_keys('4111111111111111')
    browser.find_element(By.NAME, 'cvc').send_keys('123')
    browser.find_element(By.NAME, 'expiry_month').send_keys('01')
    browser.find_element(By.NAME, 'expiry_year').send_keys('2025')

    # Step 17: Click the 'Pay and Confirm Order' button
    browser.find_element(By.XPATH, "//button[text()='Pay and Confirm Order']").click()

    # Step 18: Verify the success message 'Your order has been placed successfully!'
    assert 'Your order has been placed successfully!' in browser.page_source
