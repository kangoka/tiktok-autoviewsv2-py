from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(1024, 650)

"""
def loop1():
    time.sleep(60)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
    except:
        print("You didn't solve the captcha yet")
        loop1()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(username)
    except:
        print("Delay")
        driver.refresh()
        loop1()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/button").click()
    except:
        print("Either failed to input or can't find the button. Need to retry")
        driver.refresh()
        loop1()
    time.sleep(2)
    print("Fans success delivered!")
    driver.refresh()
    time.sleep(250)
    loop1()
"""
    
def loop2():
    time.sleep(60)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
    except:
        print("You didn't solve the captcha yet")
        loop2()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(vidUrl)
    except:
        print("Delay")
        driver.refresh()
        loop2()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/div/h5/button[2]").click()
    except:
        print("Either failed to input or can't find the button. Need to retry")
        driver.refresh()
        loop2()
    time.sleep(2)
    print("Views success delivered!")
    driver.refresh()
    time.sleep(250)
    loop2()

"""
def loop3():
    time.sleep(60)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
    except:
        print("You didn't solve the captcha yet")
        loop3()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(vidUrl)
    except:
        print("Delay")
        driver.refresh()
        loop3()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/div/h5/button[1]").click()
    except:
        print("Either failed to input or can't find the button. Need to retry")
        driver.refresh()
        loop3()
    time.sleep(2)
    print("Hearts success delivered!")
    driver.refresh()
    time.sleep(250)
    loop3()
"""

vidUrl = "https://vm.tiktok.com/ZSJshJpLw/" #Change YOUR_URL to your Tik Tok video URL
username = "bd.799" #Change YOUR_USERNAME to your Tik Tok username

system("cls")
tiktod = pyfiglet.figlet_format("TIKTOD V2", font="slant")
print(tiktod)
print("Author: https://github.com/kangoka")
print("")

"""
You can change auto value below
auto = 1 for auto fans (NEW UPDATE: They removed auto fans for now)
auto = 2 for auto views
auto = 3 for auto hearts (NEW UPDATE: They removed auto hearts for now)
"""
auto = 3

if auto == 5000:
    driver.get("https://homedecoratione.com/")
    loop1()
elif auto == 5000:
    driver.get("https://homedecoratione.com/")
    loop2()
else:
    driver.get("https://homedecoratione.com/")
    loop3()
