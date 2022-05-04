#! python3 2048-hack.py
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


def grid_move(field: list) -> str:
    # each non-empty cell
    for y in range(4):
        for x in range(4):
            if field[y][x] != 0:
                cur_value = field[y][x]
                direction = ''
                biggest_value = 0
                # left side
                for step in range(1, 4):
                    try:
                        comp_value = field[y][x - step]
                    except:
                        break
                    if comp_value == 0:
                        continue
                    elif comp_value != cur_value:
                        break
                    if cur_value * 2 > biggest_value:
                        biggest_value = cur_value * 2
                        direction = 'left'

                # up side
                for step in range(1, 4):
                    try:
                        comp_value = field[y + step][x]
                    except:
                        break
                    if comp_value == 0:
                        continue
                    elif comp_value != cur_value:
                        break
                    if cur_value * 2 > biggest_value:
                        biggest_value = cur_value * 2
                        direction = 'up'

                # right side
                for step in range(1, 4):
                    try:
                        comp_value = field[y][x + step]
                    except:
                        break
                    if comp_value == 0:
                        continue
                    elif comp_value != cur_value:
                        break 
                    if cur_value * 2 > biggest_value:
                            biggest_value = cur_value * 2
                            direction = 'right'

                # down side
                for step in range(1, 4):
                    try:
                        comp_value = field[y - step][x]
                    except:
                        break
                    if comp_value == 0:
                        continue
                    elif comp_value != cur_value:
                        break
                    if cur_value * 2 > biggest_value:
                        biggest_value = cur_value * 2
                        direction = 'down'
                
                if direction == '':
                    direction = random.choice(['left', 'right', 'up', 'down'])
    
    return direction



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
    
    # for _ in range(10):
    while 'Game over!' not in status:
        # print('*        *       *')
        # for line in get_field(browser):
        #     print('|', end='')
        #     for value in line:
        #         print(value, end=' ')
        #     print('|', end='\n')
        # print('*        *       *')

        direction = grid_move(get_field(browser=browser))
        if direction == 'up':
            htmlElem.send_keys(Keys.UP)
        elif direction == 'down':
            htmlElem.send_keys(Keys.DOWN)
        elif direction == 'left':
            htmlElem.send_keys(Keys.LEFT)
        elif direction == 'right':
            htmlElem.send_keys(Keys.RIGHT)
        else:
            print('Something went wrong!')
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
