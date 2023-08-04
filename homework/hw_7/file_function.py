from string import ascii_lowercase
from random import choices
from random import randint
from random import randbytes
from random import uniform
import os

__all__ = [
    "write_pair_nums",
    "write_random_name",
    "my_func",
    "func",
    "func_2",
    "func_3",
    "sort_files_by_exten",
    "rename_files_by_cond"
]


def write_pair_nums(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num} | {float_num:.2f}\n')


VOWELS = 'аеиоуыэюя'  # гласные русские буквы
def write_random_name(count_names: int):
    count = 0
    str_names = ""
    while count != count_names:
        word = choices(alfabet, k=randint(4, 7))
        if any(item in VOWELS for item in word):
            str_names += ''.join(word).capitalize() + '\n'
            count += 1
    with open('task7_2.txt', 'a', encoding='utf-8') as f:
        f.write(str_names)

alfabet = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1)])
write_random_name(6)


def my_func():
    with open('task7_1.txt', 'r', encoding='utf-8') as f_nums,\
          open('task7_2.txt', 'r', encoding='utf-8') as f_names:
        nums = f_nums.readlines()
        names = f_names.readlines()

    for_write = []
    long = max(len(nums), len(names))
    i = 0
    while len(nums) != len(names):
        if len(nums) > len(names):
            names.extend(names[:len(nums)-len(names)])
        else:
            nums.extend(nums[:len(names) - len(nums)])

    while i < long:
        name = names[i]
        num = nums[i]
        a, b = map(float, num.split('|'))
        mult = a * b

        if mult >= 0:
            for_write.append(f'{name.upper().rstrip()} - {round(mult)}\n')
        else:
            for_write.append(f'{name.lower().rstrip()} - {abs(mult)}\n')
        i += 1

    with open("task7_3.txt", 'w', encoding='utf-8')as f:
        f.writelines(for_write)


def func(ext, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096, files=42):
    for i in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        size = randint(min_rand_bytes, max_rand_bytes)
        with open(name, 'wb') as f:
            f.write(randbytes(size))


def func_2(files=10, **kwargs):
    dct = kwargs
    val = []
    for k, v in dct.items():
        val.append(v)
    for i in range(files):
        ext = str(*choices(val))
        func(ext, files=1, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096)

def func_3(dir):
    my_path = os.getcwd() + dir
    try:
        os.makedirs(my_path)
        os.chdir(my_path)
    except FileExistsError:
        os.chdir(my_path)
    func_2(5, a='.txt', b='.doc', c='.exe')
    os.chdir('..')


def sort_files_by_exten():
    exts = {"видео": ("mp4", "avi"), "изображения": ("jpg", "png"), "текст": ("txt", "md")}
    for key, extens in exts.items():
        pat = os.getcwd()
        ful_p = pat + "\\" + key
        os.mkdir(ful_p)
        for i in range(len(extens)):
            os.chdir(ful_p)
            os.mkdir(ful_p + "\\" + extens[i])
            os.chdir("..")

    for el in os.listdir():
        if os.path.isfile(el):
            temp_el = el.split(".")[-1]
            for k, v in exts.items():
                if temp_el in v:
                    cur = os.getcwd() + "\\" + el
                    distin = os.getcwd() + "\\" + k + "\\" + v[v.index(temp_el)] + "\\" + el
                    os.replace(cur, distin)



def rename_files_by_cond(desire_name:str, count_dig_sn: int, exten_init: str, exten_finit: str, rang_init_name: (int,int)):

    start_num = 1
    for el in os.listdir():
        if os.path.isfile(el) and el.split(".")[-1] == exten_init:
            temp =el[rang_init_name[0]:rang_init_name[1]] + desire_name+str(start_num).rjust(count_dig_sn,"0") +  exten_finit
            new_name = os.path.join(os.getcwd(), temp)
            old_name = os.path.join(os.getcwd(), el)
            start_num += 1
            os.rename(old_name,new_name)
