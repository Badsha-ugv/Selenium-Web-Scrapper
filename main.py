from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 

import pandas as pd  
from selenium.webdriver.chrome.options import Options 
from datetime import datetime 
import os 
import sys  

# select the chrome driver path from your pc 
path = "C:/Users/BADSHA/Downloads/Compressed/chromedriver_win32"
service = Service(exercutable_path=path) 
# create the process headless 
options = Options() 
options.headless = True 


driver = webdriver.Chrome(service=service, options=options) 




website = "https://www.thesun.co.uk/" # copy the website link 

# get the website by selenium 
driver.get(website) 

container = driver.find_elements(by='xpath', value="//div[@class='teaser__copy-container']") 

title_list = []
subtitle_list = []
link_list = []

for item in container:
    subtitle = item.find_element(by='xpath', value= ".//span").text 
    title = item.find_element(by='xpath', value=".//h3").text 
    link = item.find_element(by='xpath', value="./a").get_attribute('href') 

    title_list.append(title) 
    subtitle_list.append(subtitle)
    link_list.append(link) 


dict = {
    'Title': title_list,
    'Subtitle': subtitle_list,
    'Link': link_list
}

news_head = pd.DataFrame(dict)
fiel_path = os.path.dirname(sys.executable) 
now = datetime.now() 
time_format = now.strftime("%d-%m-%Y") 
file_name = f"news_head{time_format}.csv" 

file = os.path.join(fiel_path, file_name) 

news_head.to_csv(file)  

driver.quit() 


