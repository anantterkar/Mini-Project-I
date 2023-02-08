from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv


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
    data = driver.find_elements(By.TAG_NAME, 'p')
    string = ""

    for d in data:
        string += d.text

    sub1 = "HEADNOTE:"
    sub2 = "Held:"
    string=string.replace(sub1,"*")
    string=string.replace(sub2,"*")
    re=string.split("*")
    if len(re) != 0:
        res=re[1]
        rows.append([string, res])




with open(filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)
