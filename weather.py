from selenium import webdriver

class Weather:

    def __init__(self):
        self.weather_url = 'https://google.com/'
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get(self.weather_url)

    def get_weather(self, city):

        try:
            self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('Погода {}'.format(city))
            self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(u'\ue007')
        except Exception:
            self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input').clear()
            self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input').send_keys('Погода {}'.format(city))
            self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input').send_keys(u'\ue007')

        return int(self.driver.find_element_by_id('wob_tm').text)
    
    def close_window(self):
        self.driver.close()
