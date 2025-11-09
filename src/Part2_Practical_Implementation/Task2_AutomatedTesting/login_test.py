from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time, sys

def run_tests(base_url="https://example.com"):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as e:
        print("❌ ChromeDriver failed to start:", e)
        print("Check that Chrome and ChromeDriver versions match.")
        sys.exit(1)

    results = {"valid": False, "invalid": False}

    try:
        # ✅ Valid login test
        driver.get(base_url + "/login")
        time.sleep(1)
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("correctpass")
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(1)
        results["valid"] = "Dashboard" in driver.page_source

        # ❌ Invalid login test
        driver.get(base_url + "/login")
        time.sleep(1)
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(1)
        results["invalid"] = "Invalid credentials" in driver.page_source or "login" in driver.current_url

        print("✅ Test results:", results)
    finally:
        driver.quit()

    return results


if __name__ == "__main__":
    run_tests()
