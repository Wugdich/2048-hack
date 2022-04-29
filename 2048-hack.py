#! python3
# Program that winnig in the game named 2048
# Game addres in web - https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
import time
import random


def get_field(browser: object) -> list:
    # get info about tiles
    fieldElem = browser.find_elements(By.CLASS_NAME, 'tile')
    tiles = [obj.get_attribute('class') for obj in fieldElem]

    field = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for tile in tiles:
        # TODO: more elegant unpacking
        tile_data = tile.split()
        tile_value = int(tile_data[1].split('-')[1])
        x = int(tile_data[2].split('-')[2])
        y = int(tile_data[2].split('-')[3])
        
        # add tile to field data
        field[y - 1][x - 1] = tile_value 
        
    return field


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
    status = 'Game on'
    
    # random directions test
    for _ in range(10):
    #while 'Game over!' not in status:
        # print('*        *       *')
        # for line in get_field(browser):
        #     print('|', end='')
        #     for value in line:
        #         print(value, end=' ')
        #     print('|', end='\n')
        # print('*        *       *')

        direction = random.randint(0, 3)
        if direction == 0:
            htmlElem.send_keys(Keys.UP)
        elif direction == 1:
            htmlElem.send_keys(Keys.DOWN)
        elif direction == 2:
            htmlElem.send_keys(Keys.LEFT)
        else:
            htmlElem.send_keys(Keys.RIGHT)
        time.sleep(0.15)
    
        # find element with class name game-message
        try:
            statusElem = browser.find_element(By.CLASS_NAME, 'game-message')
            status = statusElem.text
        except:
            pass
    
    # get total score in the end of the game
    score = browser.find_element(By.CLASS_NAME, 'scores-container').text
    score = score[:score.find('\n')]
    print(f'Game over. Total score - {score}')
    browser.close()


if __name__=='__main__':
    main()
    