import time
from transformers import pipeline
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

USERNAME = os.environ['TWITTER_USERNAME']
PASSWORD = os.environ['TWITTER_PASSWORD']

def generate_tweet():
    print("Generating content...")
    generator = pipeline("text-generation", model="gpt2")
    prompt = "Give me a short motivational quote under 280 characters:"
    result = generator(prompt, max_length=60, num_return_sequences=1)
    content = result[0]["generated_text"].strip().replace("\n", " ")
    print("Generated tweet:", content)
    return content[:275]

def post_tweet(content):
    print("Posting to Twitter...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get("https://twitter.com/login")
    time.sleep(5)

    driver.find_element(By.NAME, "text").send_keys(USERNAME + Keys.RETURN)
    time.sleep(3)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(PASSWORD + Keys.RETURN)
    time.sleep(5)

    driver.get("https://twitter.com/compose/tweet")
    time.sleep(5)
    tweet_box = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Tweet text"]')
    tweet_box.send_keys(content)
    time.sleep(2)

    tweet_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
    tweet_button.click()
    print("Tweet posted!")

    driver.quit()

if __name__ == "__main__":
    tweet = generate_tweet()
    post_tweet(tweet)
