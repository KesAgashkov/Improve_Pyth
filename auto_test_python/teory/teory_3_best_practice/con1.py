# Задание 1.
#
# Условие:
# Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора из файла /proc/loadavg
# (можно писать просто всё содержимое этого файла).
#
# Задание 2. (дополнительное задание)
#
# Дополнить все тесты ключом команды 7z -t (тип архива). Вынести этот параметр в конфиг.

import pytest
from checkers import checkout, getout
import random, string
import yaml
from datetime import datetime

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)

@pytest.fixture()
def make_folders():
    return checkout("mkdir {} {} {} {}".format(data["folder_in"], data["folder_in"], data["folder_ext"], data["folder_ext2"]), "")

@pytest.fixture()
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_in"], data["folder_ext"], data["folder_ext2"]), "")
@pytest.fixture()
def make_files():
    list_of_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], filename, data["bs"]), ""):
            list_of_files.append(filename)
    return list_of_files

@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not checkout("cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], subfoldername, testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename

@pytest.fixture(autouse=True)
def add_log_info():
    d = f"time = {datetime.now().strftime('%H:%M:%S.%f')} count = {data['count']} size = {data['bs']} load cpu = {getout('uptime')}"
    getout(f"echo {d} >> stat.txt")


