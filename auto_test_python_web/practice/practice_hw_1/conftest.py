import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def btn_selector():
    return "button"


@pytest.fixture()
def error_code():
    return "401"


@pytest.fixture()
def account_name():
    return f"Hello, {testdata['login']}"

#Элементы создания поста

@pytest.fixture()
def button_create():
    return """/html/body/div[1]/main/div/div[2]/div[1]/button"""
@pytest.fixture()
def input_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
@pytest.fixture()
def button_save():
    return """/html/body/div/main/div/div/form/div/div/div[7]/div/button"""
@pytest.fixture()
def el_created_article():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def name_of_art():
    return """Новая тестовая статья"""

