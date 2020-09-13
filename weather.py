from selenium import webdriver
import pandas
import time

browser = webdriver.Chrome('f:\\chromedriver.exe')
month="january"
#input("Enter the month")
year="2020" 
#input("Enter the year")
url = "https://www.accuweather.com/en/in/kolkata/206690/"+month+"-weather/206690?year="+year+"&view=list"

browser.get(url)

high=[]
for i in browser.find_elements_by_class_name("high"):
	j=i.get_attribute('textContent')
	high.append(int(j[:2]))
#print(high)

low=[]
for i in browser.find_elements_by_class_name("low"):
	j=i.get_attribute('textContent')
	low.append(int(j[3:5]))
#print(low)

precip=[]
for i in browser.find_elements_by_xpath('//div[@class="info precip"]/p[2]'):
	j=i.get_attribute('textContent')
	precip.append(j)
#print(precip)
date=[]
for i in range(len(high)):
	date.append(i+1)

calender = {"DATE":date, "HIGH TEMPERATURE":high, "LOW TEMPERATURE":low, "PRECIPITATION":precip}

df= pandas.DataFrame(calender)
print(df)
time.sleep(15)
#df.to_csv("e:\\"+month+".csv",index=False)
browser.quit()