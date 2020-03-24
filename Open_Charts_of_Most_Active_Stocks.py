from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from requests import get
#importing list
url='https://www.moneycontrol.com/stocks/fno/marketstats/futures/most_active/homebody.php?opttopic=&optinst=allfut&sel_mth=all&sort_order=0'
response=get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
trs=html_soup.find_all('b')
blist=trs[3:][:-2]
totalstocks=[]
for i in range(len(blist)):
    if blist[i].text not in totalstocks:
        totalstocks.append(blist[i].text)
#importing done
driver=webdriver.Chrome(executable_path='chromedriver.exe')
stocks=['NIFTY','RELIANCE']
for i in range(len(totalstocks)):
    print('getting page')
    driver.get('https://www.tradingview.com/')
    wait =WebDriverWait(driver,15)
    if(i%10==0 and i!=0):
        input('should i open next 10 stocks ')
    try:
        element=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[3]/form/label/tv-autocomplete/input")))
        element.send_keys(totalstocks[i])
        time.sleep(2)

        window=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="overlap-manager-root"]')))
        em=window.find_element_by_css_selector('tr')
        em.click()
        button=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="js-category-content"]/div/div/div/div/div[1]/div/div[1]/div')))
        button.click()
        # driver.execute_script("window.open('');") 
        driver.switch_to.window(driver.window_handles[0])
    except:
        print('error')