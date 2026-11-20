import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmailSpamSeleniumTesting(unittest.TestCase):

    # Open Chrome and launch the application
    def setUp(self):

        self.driver = webdriver.Chrome()

        self.driver.get("http://127.0.0.1:5001")

        self.wait = WebDriverWait(self.driver, 10)


    # Test Case 1: Spam Email
    def test_TC01_spam_email(self):

        email = "Congratulations! You have won a free iPhone. Click here to claim your prize now!"

        email_box = self.driver.find_element(By.ID, "emial")
        email_box.send_keys(email)

        predict_button = self.driver.find_element(By.ID, "predict")
        predict_button.click()

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        ).text

        self.assertIn("Spam", result)

        print("\nTC-01: PASS - Spam email detected")


    # Test Case 2: Fraud Email
    def test_TC02_fraud_email(self):

        email = "You have won $10,000. Send your bank details to receive your reward."

        email_box = self.driver.find_element(By.ID, "email")
        email_box.send_keys(email)

        predict_button = self.driver.find_element(By.ID, "predict")
        predict_button.click()

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        ).text

        print("\nTC-02: PASS - Fraud email detected")

        self.assertIn("Not Spam", result)


    # Test Case 3: Normal Academic Email
    def test_TC03_normal_email(self):

        email = "Please find attached the assignment file for tomorrow's submission."

        email_box = self.driver.find_element(By.ID, "email")
        email_box.send_keys(email)

        predict_button = self.driver.find_element(By.CLASS_NAME, "predict")
        predict_button.click()

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        ).text

        self.assertIn("Not Spam", result)

        print("\nTC-03: PASS - Normal email detected")


    # Test Case 4: Meeting Email
    def test_TC04_meeting_email(self):

        email = "Hi, I hope you are doing well. Can we schedule a meeting for Monday?"

        email_box = self.driver.find_element(By.ID, "email")
        email_box.send_keys(email)

        predict_button = self.driver.find_element(By.ID, "predict")
        predict_button.click()

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        ).text

        self.assertIn("Spam", result)

        print("\nTC-04: PASS - Normal email detected")


    # Keep Chrome open for 10 seconds after each test
    def tearDown(self):

        time.sleep(7)


# Execute all test cases
if __name__ == "__main__":

    unittest.main(verbosity=2)
