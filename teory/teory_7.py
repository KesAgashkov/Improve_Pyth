# text = open("new.txt", "a", encoding="utf-8")
# text.writelines("БлаБла")
# # print(list(text))
# text.close()
#
# f = open("new.txt", "r", encoding="utf-8")
# print(list(f))

# with open("new.txt", "r+", encoding="utf-8") as f2:
    # print(*list(f2))

    # res = f2.read()
    # print(res)

    # while res := f2.readline(5):
    #     print(res,end='')

    # for line in f2:
    #     print(line,end="")
    # f2.writelines("\nКонец")

#Получение пути


import os
from pathlib import Path
import shutil

print(os.getcwd())
print(Path.cwd())
# os.chdir("..//..")
print(Path.cwd())
# os.mkdir("more_dir")
# Path("new").mkdir()

# os.makedirs("New/new/NEW")
# Path("New/new/NEW").mkdir(parents=True)
# os.rmdir("New")

# shutil.rmtree("New") #Удалить все дерево

# shutil.rmtree("new/NEW") #или ветку от дерева

#Создание пути
# print(os.path.join(os.getcwd(),"file"))
#
# print(Path().cwd() / "file2")


#Показать файлы в папке
# print(os.listdir("../test_test"))
#
# p = Path(Path.cwd())
# for el in p.iterdir():
#     if el.is_dir():
#         print(el)


for el in os.walk(os.getcwd()):
    print(el)