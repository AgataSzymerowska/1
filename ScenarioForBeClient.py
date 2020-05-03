from environment import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestKlientBiznesowy(Driver):


    def navigate_to_form_view(self):
        form_view = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "main-content__header__title")))
        return form_view.location_once_scrolled_into_view

    def radio_button(self):
        radio_button_klient_biznesowy = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                         "div.grids-wrapper.mg-b-5 > div:nth-child(2)")))
        time.sleep(2)
        return radio_button_klient_biznesowy.click()

    def name_field(self):
        name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
        return name.send_keys("BlueServices Test")

    def email_field(self):
        email_address = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "email_c")))
        return email_address.send_keys("bs@blueservices.pl")

    def phone_field(self):
        phone_number = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "phone")))
        return phone_number.send_keys("+48 123 123 123")

    def subject_select_list(self):
        select_subject = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "subject"))))
        return select_subject.select_by_visible_text("Przelewy natychmiastowe")

    def form_input_field(self):
        additional_contents = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#body")))
        return additional_contents.send_keys("automat test Blueservices")

    def reply_button(self):
        reply_option_email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                  "#result > div:nth-child(7) > div > div:nth-child(1)")))
        return reply_option_email.click()

    def agreement_button(self):
        required_agreement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#agreement_1")))
        return required_agreement.click()

    def after_step(self):
        self.driver.save_screenshot(f"screenshots/TestKlientBiznesowy.png")

    def test_end(self):
        self.driver.quit()




test = TestKlientBiznesowy()
test.navigate_to_form_view()
test.radio_button()
test.name_field()
test.email_field()
test.phone_field()
test.subject_select_list()
test.form_input_field()
test.reply_button()
test.agreement_button()
test.after_step()
test.test_end()
