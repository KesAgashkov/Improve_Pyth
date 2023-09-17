import requests
from zeep import Client


response = requests.get('https://api.github.com')
# requests.post('https://httpbin.org/post', data={'key':'value'})
# requests.put('https://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.options('https://httpbin.org/get')
print(response.status_code)
print(response.content)
print(response.text)
print(response.json())


wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = 'dsdsds'

client = Client(wsdl=wsdl)

def test_check_sign():
    assert client.service.VerifySignature('CMS', sign)["Result"], "Неверная подпись"


