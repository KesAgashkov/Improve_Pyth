# Создать отдельный файл для негативных тестов. Функцию проверки вынести в отдельную библиотеку.
# Повредить архив (например, отредактировав его в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами распаковки (e) и проверки (t) поврежденного архива.
import subprocess
from prac_2 import checkout

def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    # print(result.stdout)
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False

folderin = "/home/kes/tst"
folderout = "/home/kes/out"
folderext = "/home/kes/folder1"
folderbad = "/home/kes/folder2"

def test_step1():
    # test1
    assert checkout_negative(f"cd {folderbad};  7z e arx2.7z -o{folderext} -y", "ERRORS"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout_negative(f"cd {folderbad}; 7z t arx2.7z", "ERRORS"), "test2 FAIL"



def test_step6():
    # test6
    res1 = checkout(f"cd {folderin};  7z a {folderout}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {folderout}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"

def test_step7():
    # test7
    res1 = checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test7 FAIL"
    res2 = checkout(f"ls {folderext}", "test1.txt")
    res3 = checkout(f"ls {folderext}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"

def test_step8():
    #test8
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "1 files")