from selenium import webdriver
import time 
import re 

path_to_driver = "/Users/rijinmk/Desktop/Programming/Programming/Practice/SELENIUM/chromedriver"
driver = webdriver.Chrome(path_to_driver)

driver.get('https://www.instagram.com/accounts/login/')

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login = driver.find_element_by_class_name('_njrw0')

username.send_keys('rijin.js')
password.send_keys('1fb10a2048')
login.click()

base_url = 'https://www.instagram.com/explore/tags/'
hashtags = ['programming', 'programmers', 'technology', 'developers']

for i in range(len(hashtags)): 
    time.sleep(5)
    driver.get(base_url + hashtags[i])

    first_image = driver.find_element_by_class_name('_si7dy')
    first_image.click()  
    for i in range(5000):
        try:   
            nxt = driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
            nxt.click()
            
            like = driver.find_element_by_class_name('coreSpriteHeartOpen')
            like.click() 
            time.sleep(2)       
        except: 
            try:
                nxt = driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                nxt.click()
            except:
                continue 


