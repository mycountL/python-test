import time

start_time = time.time()
start_time_str = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(start_time))
start = f"开始时间：{start_time_str}"
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f'{start}\n\n')

import easygui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import serial

easygui.msgbox("该脚本是模拟用户手动点击UI重启单板\n\n文档output.txt中\n当前网络连接正常是根据页面右上角无线宽带连接状态判断网络是否连接")
user_input = easygui.enterbox("请输入重启次数： ")
num = int(user_input)
def restar_num(num):
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f'设置重启次数为：{num}\n\n')

    driver = webdriver.Chrome()
    driver.get("http://192.168.100.1")
    driver.maximize_window()
    sleep(10)
    try:
        driver.find_element(By.XPATH, '//*[@id="ipt_admin_password"]').send_keys('admin')
        sleep(2)
        driver.find_element(By.ID, 'login_ok').click()
        sleep(5)
    except NoSuchElementException:
        pass
   # print(driver.find_element(By.XPATH, '//*[@id="td_networkoperator_name_value"]').text)



    try:
        net = driver.find_element(By.XPATH, '//*[@id="td_networkoperator_name_value"]').text
        #print(net.text)
        op = driver.find_element(By.XPATH,'//*[@id="td_iccid_value"]').text
        # net1 = net.get_attribute('class')
        # dv = driver.find_element(By.XPATH, '//*[@id="container"]/div[3]/div[2]/div[1]/div[1]/label[2]').text
        dv2 = f'当前运营商：{net}\nICCID:{op}\n'
        print(dv2)
        #print(net3)
    except NoSuchElementException:
        net3 = '重启前网络连接失败'
        #dv2 = f'{net3}\n当前运营商：{op}\nICCID:{dv}\n'
        print(net3)
if __name__ == '__main__':
    restar_num(num)

'''
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f'{dv2}\n\n')
    n = 0
    while n < num:
        try:
            driver.find_element(By.XPATH,'//*[@id="txtAdmin"]').send_keys('admin')
            sleep(2)
            driver.find_element(By.ID,'btnLogin').click()
            sleep(5)
        except NoSuchElementException:
            pass
        WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[1]/div/ul/li[5]/a'))).click()
        WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.LINK_TEXT,'其他'))).click()
        WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="frmRestoreReset"]/div/div[2]/div/input[1]'))).click()
        ele = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="yesbtn"]')))
        ele.send_keys(Keys.ENTER)
        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="okbtn"]'))).click()
        sleep(5)
        n += 1
        numbers = f'重启第{n}次'
        print(numbers)
        with open("output.txt", "a", encoding="utf-8") as f:
            f.write(f'{numbers}: ')
        try:
            driver.find_element(By.XPATH,'//*[@id="txtAdmin"]').send_keys('admin')
            sleep(2)
            driver.find_element(By.ID,'btnLogin').click()
            sleep(5)
        except NoSuchElementException:
            pass
        net = WebDriverWait(driver,20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="h_connect_btn"]')))
        net1 = net.get_attribute('class')
        if net1 == 'h_connect_on':
            # print(f'当前网络连接状态：{net1}')
            net2 = '当前网络连接正常，开关开启'
            op = driver.find_element(By.XPATH, '//*[@id="operator"]').text
            dv = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div[2]/div[1]/div[1]/label[2]').text
            dv1 = f'{net2}\n当前运营商：{op}\nICCID:{dv}\n'
            print(dv1)
        else:
            net2 = '当前网络连接失败，开关关闭'
            op = driver.find_element(By.XPATH, '//*[@id="operator"]').text
            dv = driver.find_element(By.XPATH, '//*[@id="container"]/div[3]/div[2]/div[1]/div[1]/label[2]').text
            dv1 = f'{net2}\n当前运营商：{op}\nICCID:{dv}\n'
            print(dv1)
        with open("output.txt", "a", encoding="utf-8") as f:
            f.write(f'{dv1}\n\n')
    driver.quit()
print(start)


if __name__ == '__main__':
    restar_num(num)

end_time = time.time()
end_time_str = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(end_time))
end = f"结束时间：{end_time_str}"
print(end)
with open("output.txt", "a", encoding="utf-8") as f:
    f.write(f'{end}\n\n')

duration = end_time - start_time
time_str = time.strftime("%H:%M:%S", time.gmtime(duration))
dur = f"总共用时：{time_str}"
print(dur)
with open("output.txt", "a", encoding="utf-8") as f:
    f.write(f'{dur}\n\n')
    
'''