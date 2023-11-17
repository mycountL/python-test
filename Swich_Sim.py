import time

start_time = time.time()
start_time_str = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(start_time))
start = f"开始时间：{start_time_str}"
print(start)
with open("swich.txt", "w", encoding="utf-8") as f:
    f.write(f'{start}\n\n')

import easygui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import serial


easygui.msgbox("该脚本实现：\n模拟用户UI手动选择SIM卡\n\n切卡次数: \n手动切换SIM卡次数\n\n选择当前版本：\n如果是双卡版本请输入2\n如果是三卡版本请输入3\n\n结果请查看swich.txt文件\n\n\n温馨提示：执行该脚本前请先准备好版本，恢复出厂")
user_input3 = easygui.enterbox("请输入切卡次数： ")
num = int(user_input3)
def sim3_version(num):
    a = f'三卡版本 切卡次数为：{num}'
    print(a)
    with open("swich.txt", "a", encoding="utf-8") as f:
        f.write(f'{a}\n\n')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.100.1")
    driver.implicitly_wait(5)

    try:
        driver.find_element(By.XPATH, '//*[@id="txtAdmin"]').send_keys('admin')
        sleep(2)
        login = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'btnLogin')))
        login.click()

    except NoSuchElementException:
        pass
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[3]/div[2]/div[1]/div[2]/label[2]'))
    )
    pwd = int(element.text) % 1000000 * 1000 + 999
    IMEI = f'当前单板的IMEI号为： {element.text}'
    print(IMEI)
    with open("swich.txt", "a", encoding="utf-8") as f:
        f.write(f'{IMEI}\n\n')
    # driver.find_element(By.XPATH,'//*[@id="esimForm"]/div/div[2]/input').click()
    WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/ul/li[5]/a'))).click()
    # ele = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/ul/li[5]/a')
    # ele.click()
    # sleep(3)
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, '其他'))).click()
    #ele1 = driver.find_element(By.LINK_TEXT, '其他')
    #ele1.click()
    #sleep(3)

    n = 0

    while n <= num:
        for index in range(3):
            #select = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="esim_slot_select"]')))
            select = driver.find_element(By.XPATH, '//*[@id="esim_slot_select"]')
            select_obj = Select(select)
            select_obj.select_by_index(index)
            sleep(5)
            b = f'切换至：{select_obj.first_selected_option.text}'
            print(b)
            with open("swich.txt", "a", encoding="utf-8") as f:
                f.write(f'{b}\n')
            # WebDriverWait(driver, 20).until(
            #     EC.element_to_be_clickable((By.XPATH, '//*[@id="esimForm"]/div/div[2]/input'))).click()
            driver.find_element(By.XPATH, '//*[@id="esimForm"]/div/div[2]/input').click()
            sleep(2)
            # WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'yesbtn'))).send_keys(Keys.ENTER)
            ele3 = driver.find_element(By.ID, 'yesbtn')
            ele3.send_keys(Keys.ENTER)
            sleep(20)
            n += 1
            if n > num:
                break
            c = f"当前切卡次数：{n}"
            print(c)
            with open("swich.txt", "a", encoding="utf-8") as f:
                f.write(f'{c}\n')

            port = 'COM6'
            baudrate = 115200
            # 使用串口打开设备
            ser = serial.Serial(port=port, baudrate=baudrate, timeout=1)
            # 发送 AT 命令
            command = b'AT+ziccid?\r\n'
            ser.write(command)
            # 等待设备返回
            response = ''
            while True:
                line = ser.readline().decode('ascii').strip()  # 去掉行尾的换行符和空格
                if line.upper() == 'OK':  # 过滤掉 "OK" 字符串
                    continue
                elif line:  # 如果行不为空，则添加到response中
                    response += line
                else:
                    break
            response += ser.readline().decode('ascii')
            # 输出设备返回结果
            print(response)
            # 关闭串口
            ser.close()
            with open("swich.txt", "a", encoding="utf-8") as f:
                f.write(f'at+ziccid?\n{response}\n')
    driver.quit()


def sim2_version(num):

    a = f'双卡版本 切卡次数为：{num} '
    print(a)
    with open("swich.txt", "a", encoding="utf-8") as f:
        f.write(f'{a}\n')

    driver = webdriver.Chrome()
    driver.get("http://192.168.100.1")
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txtAdmin"]'))).send_keys('admin')
        driver.find_element(By.XPATH, '//*[@id="txtAdmin"]').send_keys('admin')
        sleep(2)
        # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, 'btnLogin'))).click()
        driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)
    except NoSuchElementException:
        pass
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[3]/div[2]/div[1]/div[2]/label[2]'))
    )
    pwd = int(element.text) % 1000000 * 1000 + 999
    IMEI = f'当前单板的IMEI号为： {element.text}'
    print(IMEI)
    with open("swich.txt", "a", encoding="utf-8") as f:
        f.write(f'{IMEI}\n\n')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/ul/li[5]/a'))).click()
    # ele = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/ul/li[5]/a')
    # ele.click()
    # sleep(3)
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, '其他'))).click()
    # ele1 = driver.find_element(By.LINK_TEXT, '其他')
    # ele1.click()
    # sleep(3)

    n = 0
    while n <= num:
        for index in range(2):
            select = driver.find_element(By.XPATH, '//*[@id="esim_slot_select"]')
            select_obj = Select(select)
            select_obj.select_by_index(index)
            b = f'切换至：{select_obj.first_selected_option.text}'
            print(b)
            with open("swich.txt", "a", encoding="utf-8") as f:
                f.write(f'{b}\n\n')
            driver.find_element(By.XPATH, '//*[@id="esimForm"]/div/div[2]/input').click()
            sleep(2)
            # WebDriverWait(driver,5).until(
            #     EC.element_to_be_clickable((By.XPATH, '//*[@id="esimForm"]/div/div[2]/input'))).click()
            if index == 0:
                driver.find_element(By.XPATH,'//*[@id="test"]').send_keys(pwd)
                driver.find_element(By.XPATH,'//*[@id="yesbtn"]').click()
                sleep(20)
                # WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, 'yesbtn'))).send_keys(Keys.ENTER)
            else:
                # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'yesbtn'))).send_keys(Keys.ENTER)
                ele3 = driver.find_element(By.ID, 'yesbtn')
                ele3.send_keys(Keys.ENTER)
                sleep(20)

            n += 1
            if n > num:
                break
            c = f'当前切卡次数：{n}'
            print(c)
            with open("swich.txt", "a", encoding="utf-8") as f:
                f.write(f'{c}\n\n')

            port = 'COM6'
            baudrate = 115200
            # 使用串口打开设备
            ser = serial.Serial(port=port, baudrate=baudrate, timeout=1)
            # 发送 AT 命令
            command = b'AT+ziccid?\r\n'
            ser.write(command)
            # 等待设备返回
            response = ''
            while True:
                line = ser.readline().decode('ascii').strip()  # 去掉行尾的换行符和空格
                if line.upper() == 'OK':  # 过滤掉 "OK" 字符串
                    continue
                elif line:  # 如果行不为空，则添加到response中
                    response += line
                else:
                    break
            response += ser.readline().decode('ascii')
            # 输出设备返回结果
            print(response)
            # 关闭串口
            ser.close()
            with open("swich.txt", "a", encoding="utf-8") as f:
                f.write(f'at+ziccid?\n{response}')

    driver.quit()

if __name__ == '__main__':

   # a = int(input("请输入当前版本 "))
    while True:
        user_input = easygui.enterbox("请输入当前版本 ")
        a = int(user_input)
        if a == 2:
            sim2_version(num)
            break
        elif a == 3:
            sim3_version(num)
            break
        else:
            user_input1 = easygui.enterbox('输入范围仅为2或3，请重新输入')
            #sleep(2)


end_time = time.time()
end_time_str = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(end_time))
end = f"结束时间：{end_time_str}"
print(end)
with open("swich.txt", "a", encoding="utf-8") as f:
    f.write(f'{end}\n\n')

duration = end_time - start_time
time_str = time.strftime("%H:%M:%S", time.gmtime(duration))
dur = f"总共用时：{time_str}"
print(dur)
with open("swich.txt", "a", encoding="utf-8") as f:
    f.write(f'{dur}\n\n')