from selenium import webdriver
from tkinter import Tk
from time import sleep
r=Tk()
r.withdraw()
browser = webdriver.Firefox(executable_path='C:/Users/ASUS/Downloads/geckodriver-v0.26.0-win64/geckodriver.exe')
browser.get('https://www.google.com/search?q=google+translate&oq=goo&aqs=chrome.0.69i59j69i57j35i39j0l2j69i60l3.2202j0j7&sourceid=chrome&ie=UTF-8')
sleep(1)
browser.find_element_by_xpath('//*[@id="tw-tl"]').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="tw-container"]/g-expandable-container/div/div/div[6]/g-expandable-container/div/g-expandable-content/span/div/div[2]/div[1]/div/div[2]/div[38]').click()
#browser.find_element_by_xpath('//*[@id="tw-container"]/g-expandable-container/div/div/div[6]/g-expandable-container/div/g-expandable-content/span/div/div[2]/div[1]/div/div[2]/div[89]').click();
sleep(1)
searchbox= browser.find_element_by_xpath('//*[@id="tw-source-text-ta"]')
with open('hindi.txt','w',encoding='utf-8') as file:
    with open('english.txt','r') as f:
        for x in f:
            searchbox.send_keys(x);
            sleep(5)
            #getdata=browser.find_element_by_xpath('//*[@id="tw-target-text"]/span');
            browser.find_element_by_xpath('//*[@id="tw-cpy-btn"]/span').click()
            result=r.clipboard_get()
            file.write(result+'\n');
            browser.find_element_by_xpath('//*[@id="tw-cst"]/span').click()
        f.close();
    file.close()
