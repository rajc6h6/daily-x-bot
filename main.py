import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import os

username = os.environ.get("TWITTER_USERNAME")
password = os.environ.get("TWITTER_PASSWORD")

def post_tweet(text):
    options = uc.ChromeOptions()
    options.headless = True
    driver = uc.Chrome(options=options)

    try:
        driver.get("https://twitter.com/login")
        time.sleep(5)

        # Login
        driver.find_element(By.NAME, "text").send_keys(username)
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        time.sleep(3)

        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
        time.sleep(5)

        # Compose tweet
        tweet_box = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
        tweet_box.send_keys(text)
        time.sleep(2)

        driver.find_element(By.XPATH, '//span[text()="Post"]').click()
        print("Tweet posted successfully.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    post_tweet("Daily auto-tweet powered by ChatGPT 🚀")
