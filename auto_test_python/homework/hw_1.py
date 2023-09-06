import subprocess
import re
# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.
def script_1(com: str, path: str, text: str) -> bool:
    result = subprocess.run(f"{com} {path}", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        if text in result.stdout:
            return True
        else:
            return False

# print(script_1("ls", "/home", "us12"))

# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation
# модуля string). В этом режиме должно проверяться наличие слова в выводе.

def script_2(com: str, path: str, text: str) -> bool:
    result = subprocess.run(f"{com} {path}", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    res = re.sub(r'[.,"\'?:!;]', '', result.stdout).split("\n")[:-1]
    print(res)
    if result.returncode == 0:
        for el in res:
            if text == el:
                return True
        return False

# print(script_2("ls", "/home/kes", "MoreFile"))