# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import pandas as pd

# driver = webdriver.Chrome()
# url = 'https://www.basketball-reference.com/'
# driver.get(url)

import unittest
from wsgiref.headers import Headers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
import pandas as pd

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\kevin\Documents\Python\chromedriver\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.basketball-reference.com/")
        elem = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[3]/form/div/div/input[2]")
        elem.send_keys("jeremy lin")
        elem.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/strong/a").click()
        parser = soup(driver.page_source, 'html.parser')
        table = parser.find('div', attrs = {'class': 'table_container current is_setup'})
        headers = table.findAll('th')
        headers = [h.text.strip() for h in headers[1:]]
        headerlist = []
        x = 0
        for i in headers:
            headerlist.append(i)
            x += 1
            if x == 29:
                break
        body = table.find('tbody')
        rows = body.findAll('tr')
        
        playerstats = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
        # stats = pd.DataFrame(playerstats, columns = headerlist)
        print(headers)

        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
