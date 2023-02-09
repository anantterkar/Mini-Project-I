from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv
import time
import pandas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


text = []
with open("test.txt") as file:
        for line in file:
            urls = re.findall('(?P<url>https?://[^\s]+)', line)
            if len(urls) != 0:
                text.append(urls[0])
print(text)

driver = webdriver.Chrome('chromedriver.exe')

final_data = []
headnote = []

fields = ["Decisions", "Headnote"]
filename = "dataset.csv"
rows = []
    


for i in range(0, len(text)):
    driver.get(text[i])
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)
    data = driver.find_elements(By.TAG_NAME, 'p')
    string = ""
    for d in data:
        string += d.text
    # with open ('writeme.txt', 'w') as file:  
    # file.write('writeme')  
    # print(string)
    sub1 = "HEADNOTE:"
    sub2 = "Held:"
    s=str(re.escape(sub1))
    e=str(re.escape(sub2))
    s= sub1
    e = sub2
    # print(string)
    res=re.findall(s+"(.*)"+e,string)
    if len(res) != 0:
        # print(res)
        rows.append([string, res[0]])


with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)


