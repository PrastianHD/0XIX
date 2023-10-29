import pandas as pd
from selenium                           import webdriver
from selenium.webdriver.chrome.service  import Service
import time

URL = "https://www.oxix.network/signup?refid=d65d77a101" #Ganti Link Google Form
chrome_driver_path = r"C:\Script Bot/chromedriver.exe" #Ganti folder ChromeDriver Berada

def fill_form():
    data = pd.read_csv('C:\Script Bot\Bahasa Python\Form Otomatis\data2.csv', skipinitialspace=True) #Ganti file data.csv Berada
    recycle = data.shape[0]
    for i in range(recycle):
        driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
        driver.get(URL)
        driver.maximize_window()
        time.sleep(10)
        
        name = data.iloc[i]['name']
        inputName = driver.find_element("xpath",'/html/body/section/div/div/form/a[1]/input')
        for j in name:
            inputName.send_keys(j)
            time.sleep(0.05)

        email = data.iloc[i]['email']
        inputEmail = driver.find_element("xpath",'/html/body/section/div/div/form/a[2]/input')
        for j in email:
            inputEmail.send_keys(j)
            time.sleep(0.05)

        address = data.iloc[i]['address']
        inputAddress = driver.find_element("xpath",'/html/body/section/div/div/form/a[3]/input')
        for j in address:
            inputAddress.send_keys(j)
            time.sleep(0.05)
        
        password = data.iloc[i]['password']
        inputPassword = driver.find_element("xpath",'/html/body/section/div/div/form/a[4]/input')
        for j in password:
            inputPassword.send_keys(j)
            time.sleep(0.1)


        submit = driver.find_element("xpath",'/html/body/section/div/div/form/div/button')
        submit.click()
        time.sleep(2)

        print("Data " + str(i) + " Berhasil Dikirim")
        
fill_form()
time.sleep(5) 
