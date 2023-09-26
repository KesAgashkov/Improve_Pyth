import yaml
from module import Site
import time

with open(r"C:\Users\Zver\Selenium_Pyth\practice_hw\testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_bad_auth(x_selector1, x_selector2, x_selector3, btn_selector, error_code):

    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3).text
    assert err_label == error_code, "test_step1 Failed"


def test_success_auth(x_selector1, x_selector2, x_selector4, btn_selector, account_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["pswd"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    code_label = site.find_element("xpath", x_selector4).text
    assert code_label == account_name, "test_step1 Failed"


def test_check_append_article(button_create, input_title, button_save, el_created_article, name_of_art):
    btn_plus = site.find_element("xpath", button_create)
    btn_plus.click()
    inp_title = site.find_element("xpath", input_title)
    inp_title.send_keys(name_of_art)
    btn_save = site.find_element("xpath", button_save)
    btn_save.click()
    time.sleep(testdata['sleep_time'])
    el_saved_art = site.find_element("xpath", el_created_article)
    assert el_saved_art.text == name_of_art, "Статья не была создана"
    site.driver.close()