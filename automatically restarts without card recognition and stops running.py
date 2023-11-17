import time

start_time = time.time()
start_time_str = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(start_time))
start = f"开始时间：{start_time_str}"
print(start)
with open("reboot.txt", "w", encoding="utf-8") as f:
    f.write(f'{start}\n\n')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import sys
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

loop_count = int(input("请输入重启次数，如果为0则无限重启: "))
with open("reboot", "a", encoding="utf-8") as f:
    f.write(f'请输入重启次数，如果为0则无限重启: {loop_count}\n\n')
n = 0
def reboot(loop_count):
    driver = webdriver.Chrome()
    driver.get("http://192.168.100.1")
    driver.maximize_window()
    sleep(5)
    try:
        driver.find_element(By.XPATH, '//*[@id="ipt_admin_password"]').send_keys('admin')
        #WebDriverWait(driver, 5).until(presence_of_element_located((By.XPATH, '//*[@id="ipt_admin_password"]'))).send_keys('admin')
        sleep(2)
        driver.find_element(By.ID, 'login_ok').click()
        #WebDriverWait(driver, 5).until(presence_of_element_located((By.ID, 'login_ok'))).click()
        sleep(5)
    except NoSuchElementException:
        pass
    try:
        driver.switch_to.frame('mainframe') # 切换至iframe框架
        net = WebDriverWait(driver, 10).until(presence_of_element_located((By.ID, 'td_networkoperator_name_value'))).text
        net1 = f'第{n}次：\n当前运营商：{net}'
        net2 = f'第{n}次：\n当前网络连接失败'
        if net.strip() == "":
            print(net2)
            with open("reboot.txt", "a", encoding="utf-8") as f:
                f.write(f'{net2}\n')
        else:
            print(net1)
            with open("reboot.txt", "a", encoding="utf-8") as f:
                f.write(f'{net1}\n')

    except NoSuchElementException:
        net2 = f'第{n}次：\n页面未加载出来'
        print('net2')
        with open("reboot.txt", "a", encoding="utf-8") as f:
            f.write(f'{net2}\n')


    iccid = driver.find_element(By.XPATH,'//*[@id="td_iccid_value"]').text
    iccid1 = f'ICCID:{iccid}\n'
    Len = len(str(iccid))
    if Len == 20:
        print(f'{iccid1}\n')
        with open("reboot.txt", "a", encoding="utf-8") as f:
            f.write(f'{iccid1}\n')
    elif Len == 0:
        print(f"ICCID为空，未插卡\n")
        with open("reboot.txt", "a", encoding="utf-8") as f:
            f.write(f'ICCID为空，未插卡\n\n')
        sys.exit()
    else:
        print(f"ICCID长度错误，长度为{Len}\n")
        with open("reboot.txt", "a", encoding="utf-8") as f:
            f.write(f'ICCID长度错误，长度为{Len}\n')
        sys.exit()
    driver.switch_to.default_content()  # 切换回主文档
       # driver.quit()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'lg_adv_system'))).click()
    #driver.find_element(By.ID, 'lg_system_set').click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'lg_system_restart'))).click()

    driver.switch_to.frame('mainframe')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'sp_sys_restart'))).click()
    sleep(75)
    driver.quit()

if __name__ == '__main__':
    if loop_count == 0:
        while True:
            reboot(loop_count)
            n=n+1
    else:
        for _ in range(loop_count+1):
            reboot(loop_count)
            n=n+1

end_time = time.time()
end_time_str = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(end_time))
end = f"结束时间：{end_time_str}"
print(end)
with open("reboot.txt", "a", encoding="utf-8") as f:
    f.write(f'{end}\n\n')
