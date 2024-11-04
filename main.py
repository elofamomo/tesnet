import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

meta_mask_extension_download_link = "https://addons.mozilla.org/cs/firefox/addon/ether-metamask/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search"
password = 'songtien10'


def press_left_alt_p():
    pyautogui.hotkey('altleft', 'p')


def press_left_alt_o():
    pyautogui.hotkey('altleft', 'o')


def press_enter():
    pyautogui.press('enter')


def press_tab():
    pyautogui.press('tab')


def input_mnemonic(driver, word, index):
    input_id = f'import-srp__srp-word-{index}'
    input_element = driver.find_element(By.ID, input_id)
    input_element.send_keys(word)


def move_to_next_input(driver):
    for i in range(2):
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB)


def change_to_int(cash_value_text: str):
    cash_value_without_usdc = cash_value_text.strip().split()[0]
    cash_value_without_decimal_part = cash_value_without_usdc.strip().split('.')[0]
    cash_value_with_comma_split = cash_value_without_decimal_part.split(',')
    res = ""
    for cash in cash_value_with_comma_split:
        res += cash
    return int(res)


def open_firefox():
    options = Options()
    # options.add_argument("--headless=new")
    service = Service("geckodriver.exe")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    web_driver = webdriver.Firefox(service=service, options=options)
    web_driver.install_addon('webextension@metamask.io.xpi')
    return web_driver


def connect_metamask(driver, line_str, password):
    time.sleep(1)
    # Locate and click I Agree Checkbox button
    WebDriverWait(driver, 60).until(lambda driver: len(driver.window_handles) == 2)
    driver.switch_to.window(driver.window_handles[-1])
    button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding__terms-checkbox"]')))
    button.click()

    # Locate and click Import Existing Wallet button
    button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]'))
    )
    button.click()

    # Locate and click I Agree button
    button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/button[1]'))
    )
    button.click()

    # Locate and click First word button
    button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="import-srp__srp-word-0"]'))
    )
    button.click()
    for index, word in enumerate(line_str):
        input_mnemonic(driver, word, index)
        move_to_next_input(driver)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click()  # confirm
    time.sleep(1)
    # input password twice
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input'))).send_keys(password)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input'))).send_keys(password)
    # I understand
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input'))).click()
    # import my wallet
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button'))).click()
    # got it
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    # next
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    # done
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    # close
    # WebDriverWait(driver, 60).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div/button/span'))).click()
    time.sleep(1)


def take_first_element(value):
    return int(value.strip().split()[0][0])


def connect_to_predicthub(driver, ind, threshold: int):
    url = 'https://testnet.predicthub.io/'
    driver.get(url)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/header/div/div[2]/button'))).click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/ul/li[2]/button'))).click()
    WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(3))
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(lambda driver: len(driver.window_handles) == 3)
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[3]/button[2]'))).click()
    # chuyển mạng
    time.sleep(3)
    button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]')))

    ActionChains(driver).move_to_element(button).click().perform()
    # yêu cầu đăng nhập
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(3))
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[5]/footer/button[2]'))).click()
    print(f"Connect metamask done for phrase in line {ind + 1}")
    # faucet
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])
    faucet_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/header/div/div[2]/a')))
    faucet_button.click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/section/div[2]/div[3]/button'))).click()
    time.sleep(1)
    driver.get("https://testnet.predicthub.io/event/when-will-dogs-dogs-reach-a-market-cap-of-1b")
    buy_tab_button = '/html/body/div[1]/div/main/div/div[2]/div/div/div[2]/button[1]'
    sell_tab_button = '/html/body/div[1]/div/main/div/div[2]/div/div/div[2]/button[2]'
    max_button = '/html/body/div[1]/div/main/div/div[2]/div/div/div[5]/div[1]/div/button'
    buy_sell_button = '/html/body/div[1]/div/main/div/div[2]/div/div/div[7]/button'
    cash_location = '/html/body/div[1]/div/header/div/div[2]/div[2]/a[2]/p[2]'
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, cash_location)))
    time.sleep(3)
    text_cash_value = driver.find_element(By.XPATH, cash_location).text
    cash_value = change_to_int(text_cash_value)
    print(cash_value)
    if cash_value >= threshold:
        time.sleep(3)
        driver.find_element(By.XPATH, buy_tab_button).click()
        time.sleep(4)
        driver.find_element(By.XPATH, max_button).click()
        time.sleep(3.5)
        driver.find_element(By.XPATH, buy_sell_button).click()
        # I fully agree
        time.sleep(5)
        tickbox_location = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[4]/div[2]/section/div[2]/div/label/span[1]/input')))
        ActionChains(driver).move_to_element_with_offset(tickbox_location, 0, 0).click().perform()
        # Got it
        time.sleep(4)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/section/div[2]/div/button'))).click()
        time.sleep(3)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div/div/button'))).click()
        time.sleep(3.5)
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[-1])
        # scroll down
        time.sleep(3)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/button'))).click()
        time.sleep(3.6)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/button[2]'))).click()
        time.sleep(4.6)
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3.7)
        # change to sell tab
        sell_tab = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, sell_tab_button)))
        driver.execute_script("arguments[0].click();", sell_tab)
        time.sleep(5.2)
        # wait to update cash value and sell
        WebDriverWait(driver, 60).until(
            lambda driver: take_first_element(driver.find_element(By.XPATH, cash_location).text) == 0)
        driver.find_element(By.XPATH, max_button).click()
        # Click sell
        time.sleep(3.7)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div/div/button').click()
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[-1])
        # scroll down
        time.sleep(3)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/button'))).click()
        time.sleep(4.4)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/button[2]'))).click()
        time.sleep(2)
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 60).until(
            lambda driver: change_to_int(driver.find_element(By.XPATH, cash_location).text) != 0)
        cash_value = change_to_int(driver.find_element(By.XPATH, cash_location).text)
    else:
        print(f"Cash in phrase {ind + 1} is below {threshold}. Move to next phrase")
    #
    # Loop until cash run below 1000
    while cash_value >= threshold:
        buy_tab = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, buy_tab_button)))
        driver.execute_script("arguments[0].click();", buy_tab)
        driver.find_element(By.XPATH, max_button).click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div/div/button'))).click()
        # I fully agree
        # tickbox_location = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        #     (By.XPATH, '/html/body/div[4]/div[2]/section/div[2]/div/label/span[1]/input')))
        # ActionChains(driver).move_to_element_with_offset(tickbox_location, 0, 0).click().perform()
        # Got it
        # WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/section/div[2]/div/button'))).click()
        # WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div/div/button'))).click()
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[-1])
        # scroll down
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/button'))).click()
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/button[2]'))).click()
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        # change to sell tab
        sell_tab = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, sell_tab_button)))
        driver.execute_script("arguments[0].click();", sell_tab)
        # wait to update cash value and sell
        WebDriverWait(driver, 60).until(
            lambda driver: take_first_element(driver.find_element(By.XPATH, cash_location).text) == 0)
        driver.find_element(By.XPATH, max_button).click()
        # Click sell
        driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div/div/button').click()
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[-1])
        # scroll down
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/button'))).click()
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/button[2]'))).click()
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 60).until(
            lambda driver: change_to_int(driver.find_element(By.XPATH, cash_location).text) != 0)
        cash_value = change_to_int(driver.find_element(By.XPATH, cash_location).text)
    print(f"Cash in phrase {ind + 1} run below {threshold}. Move to next phrase")


if __name__ == '__main__':
    phrases = []
    passwords = []
    with open("phrase.txt", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line_str_and_pass = line.strip().split(',')
        line_str = line.strip().split()
        threshold = random.randint(2000,7000)
        driver = open_firefox()
        connect_metamask(driver, line_str, password)
        connect_to_predicthub(driver, i, threshold)
        driver.quit()

