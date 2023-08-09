import json
import csv
import pickle
import os


def convert_txt_to_json(txt_file, json_file):
    with open(txt_file, 'r', encoding='utf-8') as f,\
        open(json_file, "w", encoding='utf-8') as js_f:
        contents = f.readlines()
        my_dict = {}
        for el in contents:
            key, val = el.split("-")
            my_dict[key.title()] = float(val)
        json.dump(my_dict, js_f, separators=(',\n', ':'), ensure_ascii=False)


def json_to_csv():
    with open('task8_2.json', "r", encoding='utf-8') as js_f:
        res = json.load(js_f)
        lst = []
        keys = res[0].keys()
        lst.append(keys)
        for el in res:
            vals = el.values()
            lst.append(vals)

    with open('task8_2.csv', "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for el in lst:
            writer.writerow(el)


def search_json_convert_pickle():
    for el in os.listdir():
        if el.endswith(".json"):
            with open(el, "r", encoding="utf-8") as j:
                res = json.load(j)
            path = ''.join(el.split(".")[:-1]) + ".pickle"
            with open(path, "wb") as p:
                pickle.dump(res,p)


def pickle_dct_to_csv():
    with open('new_json.pickle', 'rb') as f:
        data = pickle.load(f)

    with open("new_c.csv", "w", encoding="utf-8") as c:
        writer = csv.writer(c)
        for row in data:
            writer.writerow(str(row))