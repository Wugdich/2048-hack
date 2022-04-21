#! python3
# Program that winnig in the game named 2048
# Game addres in web - https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
import time
import random

logging.basicConfig(
    filename='logs.txt', level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

browser = webdriver.Firefox()
browser.get('https://play2048.co')

htmlElem = browser.find_element_by_tag_name('html')
# TODO: while not game over cycle
# random directions test
for _ in range(100):
    direction = random.randint(0, 3)
    if direction == 0:
        htmlElem.send_keys(Keys.UP)
    elif direction == 1:
        htmlElem.send_keys(Keys.DOWN)
    elif direction == 2:
        htmlElem.send_keys(Keys.LEFT)
    else:
        htmlElem.send_keys(Keys.RIGHT)
    time.sleep(0.4)