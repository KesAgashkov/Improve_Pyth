import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


# Задание
# Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие
# на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров
# title, description, content.

def test_search_new_articles(user_login):
    add_art = S.post(url=data['address'],
                     data={'title': data["title"], 'description': data["description"], "content": data["content"]},
                     headers={'X-Auth-Token': user_login})
    full_art = S.get(url=data['address'], headers={'X-Auth-Token': user_login})
    print(full_art.json())
    full_art = [i['description'] for i in full_art.json()["data"]]
    assert (add_art.status_code == 200 and add_art.json()["description"] in full_art), \
        "Статья не найдена в списке статей"


def test_step1(user_login, post_title):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'}).json()['data']
    result_title = [i['title'] for i in result]
    assert post_title in result_title, 'test_step1 FAIL'
