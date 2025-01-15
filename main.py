from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import yaml
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

with open("configuration.yaml","r") as file:
    data = yaml.safe_load(file)
    print(data)
    print()
    print(type(data))
    print(data['test_url'])
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    if data["Environment"] == "test":
        driver.get(data['test_url'])
        driver.maximize_window()
        time.sleep(7)
        # res = driver.find_element(By.XPATH,"//img[@class='-dOa_b XdYXbi']")
        # fi=Select(res)
        # # for i in fi.options():
        # #     print(i.text)
        driver.execute_script("alert('hello hi');")
        time.sleep(8)
        alert=driver.switch_to.alert
        print(alert.text)
        alert.accept()
        de = driver.find_element(By.XPATH,"//select[@id='searchDropdownBox']")
        select = Select(de)
        for i in select.options:
            print(i.text)
        time.sleep(8)
        win = driver.window_handles
        driver.execute_script("window.open('https://flipkart.in','_blank');")
        time.sleep(5)
        driver.switch_to.window(win[0])
        time.sleep(10)
    else:
        print("it's a prod environment")