def run(self):
    self.driver.get("https://www.huxiu.com/")  # 打开浏览器

    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="js-register"]')))

    reg_element = self.driver.find_element_by_xpath('//*[@class="js-register"]')
    reg_element.click()

    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="gt_slider_knob gt_show"]')))

    # 模拟拖动
    self.analog_drag()
