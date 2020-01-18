from selenium import webdriver
import string
import csv
import pandas as pd
import string
import numpy as np
import time
from time import sleep
import scipy
from scipy import stats

with open('result.csv', 'w') as f:
    f.write('prices \n')

driver = webdriver.Chrome(r'C:\Users\<user>\Downloads\<file>\chromedriver')
driver.get('https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=211&SortBy=LastSeen&Order=desc')

prices = []
max_pages = 5
max_pag_digits = 1


for l in range(1, max_pages+1):
    page_num = (max_pag_digits - len(str(l))) * "0" + str(l)
    url_num = "https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=211&SortBy=LastSeen&Order=desc&page=" + page_num
    driver.get(url_num)
    with open('results.csv', 'a') as f:
        for i in range(1, 10):
            elem = driver.find_element_by_xpath("(//td[@class='gold-amount bold'])[%d]" % (i)).get_attribute("innerText")
            f.write(elem + "\n")
            prices.append(elem)


driver.close()


def Datacleansing():
    defprice = []
    fh = open('results.csv', 'r')
    for line in fh:
        defprice.append(line.strip().split(' '))

    defprice = defprice[0::5]

    defprice = np.asarray(defprice)

    cdefprice = np.char.replace(defprice, ',', '')

    cleanedprice = cdefprice.astype(float)

    print(cleanedprice)
    print(stats.describe(cleanedprice))
    print(np.std(cleanedprice))



Datacleansing()




