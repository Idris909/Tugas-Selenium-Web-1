from selenium import webdriver
from time import sleep
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

#Title dari alamat-alamat berikut.


driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://www.tiket.com')
title = driver.title
print(title)
driver.close()

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://www.tokopedia.com')
title = driver.title
print(title)
driver.close()

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://www.orangsiber.com')
title = driver.title
print(title)
driver.close()

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://idejongkok.com')
title = driver.title
print(title)
driver.close()

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://kelasotomesyen.com')
title = driver.title
print(title)
driver.close()

#chrome

driver1 = webdriver.Chrome(options=option)
driver1.maximize_window()
driver1.get('https://www.tiket.com')
sleep(2)
driver1.get('https://www.tokopedia.com')
sleep(2) 
driver1.get('https://www.orangsiber.com')
sleep(2)
driver1.get('https://idejongkok.com')
sleep(2)
driver1.get('https://kelasotomesyen.com')
sleep(2)
driver1.back()
sleep(2)