import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://automationexercise.com/")
    yield driver
    driver.quit()


#def close_popup_if_present(driver):
#    try:
#        driver.switch_to.frame("aswift_0")
#        driver.switch_to.frame("ad_iframe")
#        close_btn = driver.find_element(By.XPATH, "//div[@id='dismiss-button']")
#        close_btn.click()
#        driver.switch_to.default_content()
#        print(" Popup closed successfully!")
#    except Exception:
#        driver.switch_to.default_content()

def test_end_to_end_user_flow(driver):
    wait = WebDriverWait(driver, 15)

    # ====== Test Case 1: Register User ======
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")

    name_input.send_keys("Elahe Test")
    email = f"elahe{int(time.time())}@test.com"
    email_input.send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    # Enter Account Information
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_gender2']"))).click()
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "days").send_keys("01")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("1990")

    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    driver.find_element(By.ID, "first_name").send_keys("Elahe")
    driver.find_element(By.ID, "last_name").send_keys("Motlagh")
    driver.find_element(By.ID, "address1").send_keys("Tehran, Iran")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "state").send_keys("NewYork")
    driver.find_element(By.ID, "city").send_keys("NewYork")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("09120000000")

    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//b[text()='Account Created!']")))
    driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

    #close_popup_if_present(driver)

    # ====== Test Case 2: Login User with correct email and password ======
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-qa='login-email']"))).send_keys(email)
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("123456")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

    # Validate login
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as')]")))

    print("!LOGIN ANJAM SHOD!")
    #close_popup_if_present(driver)

    # ====== Test Case 12: Add Products in Cart ======
    actions = ActionChains(driver)
    driver.get("https://automationexercise.com/products")
    time.sleep(3)
        
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(3)

    #افزودن محصول اول
    first_product = driver.find_element(By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[1]")
    actions.move_to_element(first_product).perform
    first_product.click()
    time.sleep(2)

    # کلیک روی Continue Shopping
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Continue Shopping']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", continue_btn)
    continue_btn.click()
    time.sleep(2)

    #لفزودن محصول دوم
    second_product = driver.find_element(By.CSS_SELECTOR, 'a.add-to-cart[data-product-id="2"]')
    actions.move_to_element(second_product).perform
    second_product.click()
    time.sleep(2)

    # کلیک روی View Cart
    view_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='View Cart']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", view_cart_btn)
    view_cart_btn.click()
    time.sleep(2)



    # ====== Test Case 4: Logout User ======
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Logout").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-qa='login-button']")))

    print("\n End-to-End test flow completed successfully!")


if __name__ == "__main__":
    pytest.main(["-v", "tests/test_end_to_end.py"])
