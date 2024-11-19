from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver using WebDriverManager to auto-download the correct version of ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the OrangeHRM demo login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for the page to load
time.sleep(3)

# Locate username and password fields
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

# Input credentials
username_input.send_keys("Admin")
password_input.send_keys("admin123")

# Locate and click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the page to load after login
time.sleep(3)

# Validate the login was successful (e.g., check if the dashboard is loaded)
try:
    dashboard_element = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    print("Login successful!")
except Exception as e:
    print("Login failed:", str(e))

# Close the browser
driver.quit()
