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

def loop1():
    driver.get("https://homedecoratione.com/")
    time.sleep(60) #Wait 1 min to complete gcaptcha
    driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(username)
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/button").click()
    time.sleep(2)
    print("Fans success delivered!")
    driver.refresh()
    time.sleep(250)
    loop1()

def loop2():
    driver.get("https://homedecoratione.com/")
    time.sleep(60)
    driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/main/div/div/div[2]/form/div/input").send_keys(vidUrl)
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/div/h5/button[2]").click()
    time.sleep(2)
    print("Views success delivered!")
    driver.refresh()
    time.sleep(250)
    loop2()

vidUrl = "YOUR_URL" #Change YOUR_URL to your Tik Tok video URL
username = "YOUR_USERNAME" #Change YOUR_USERNAME to your Tik Tok username

system("cls")
tiktod = pyfiglet.figlet_format("TIKTOD V2", font="slant")
print(tiktod)
print("Author: https://github.com/kangoka")
print("")

auto = 1 #Change 2 for Tik Tok views
if auto == 1:
    loop1()
else:
    loop2()
