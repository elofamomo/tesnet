from selenium import webdriver as uc
from time import sleep
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from fake_useragent import UserAgent
import json
import csv

import re


def add_chrome():
    global web
    options = ChromeOptions()
    options.add_extension("OKX.crx")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    web = uc.Chrome(chrome_options=options)
    web.switch_to.window(web.window_handles[-1])
    sleep(10)
    web.close()
    web.switch_to.window(web.window_handles[0])
    web.close()
    web.switch_to.window(web.window_handles[0])


def setup_metamask(phrase):
    # web.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html#initialize/welcome")
    # # import
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/button"
    # ))).click()
    # sleep(0.5)
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div"
    # ))).click()
    # # privatekey
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]"
    # ))).click()
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, f"/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/textarea"
    # ))).send_keys(phrase)
    # sleep(3)
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div/button"
    # ))).click()
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/button"
    # ))).click()
    # # pass
    # wait(web, 200).until(EC.presence_of_element_located((By.XPATH,
    #                                                      "//*[text()[contains(.,'Set password')]]")))
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[1]/div[2]/div/div/div/div/input"
    # ))).send_keys("Alpha123456")
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/input"
    # ))).send_keys("Alpha123456")
    # sleep(0.5)
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div[2]/div/div/div/button"
    # ))).click()
    # wait(web, 10).until(EC.presence_of_element_located((By.XPATH,
    #                                                     "//*[text()[contains(.,'Set now')]]")))
    # web.get("https://daren.market?ic=X555N")
    # # Connect
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/header/div/div/div[7]/div/button"
    # ))).click()
    # sleep(0.5)
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]"
    # ))).click()
    # sleep(1)
    # web.switch_to.window(web.window_handles[-1])
    # wait(web, 10).until(EC.presence_of_element_located((By.XPATH,
    #                                                     "//*[text()[contains(.,'Connect')]]")))
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]"
    # ))).click()
    # sleep(0.5)
    # web.close()
    # sleep(1)
    # web.switch_to.window(web.window_handles[-1])
    # wait(web, 10).until(EC.presence_of_element_located((By.XPATH,
    #                                                     "//*[text()[contains(.,'Signature request')]]")))
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]"
    # ))).click()
    # sleep(0.5)
    # web.switch_to.window(web.window_handles[0])
    # wait(web, 10).until(EC.presence_of_element_located((By.XPATH,
    #                                                     "//*[text()[contains(.,'Create your profile')]]")))
    # wait(web, 5).until(EC.presence_of_element_located((
    #     By.XPATH, "/html/body/div[3]/div[3]/form/div[2]/div/button[1]"
    # ))).click()
    # print("Done")


if __name__ == '__main__':
    while True:
        with open(r"phrase.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        phrase = []
        for line in lines:
            line = line.strip()
            phrase.append(line)
        try:
            add_chrome()
            setup_metamask(phrase[0])
            with open("phrase.txt", 'r+', encoding="utf-8") as fp:
                lines = fp.readlines()
                fp.seek(0)
                fp.truncate()
                fp.writelines(lines[1:])
        except Exception as e:
            print(e)
