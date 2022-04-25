#! python3
# Program that winnig in the game named 2048
# Game addres in web - https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import time
import random


def get_field() -> list:
    # class='tile-container'
    pass


def next_move() -> str:
    pass


def main():
    logging.basicConfig(
        filename='logs.txt', level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s'
        )

    browser = webdriver.Firefox()
    browser.get('https://play2048.co')
    browser.maximize_window()

    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    status = None
    # TODO: while not game over cycle
    # random directions test
    for _ in range(100):
        logging.info(f'{status} - iteration {_}')
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
    
        # find element with class name game-message
        try:
            statusElem = browser.find_element(By.CLASS_NAME, 'game-message')
            status = statusElem.text
        except:
            pass
        
    # get total score in the end of the game
    score = 0
    print(f'Game over. Result - {score}')
    browser.close()


if __name__=='__main__':
    main()
