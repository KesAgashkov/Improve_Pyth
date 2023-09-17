from sshcheckers import ssh_checkout, upload_files

def deploy():
    res = []
    upload_files("localhost", "kes", "1", r"C:\Users\Zver\PycharmProjects\improve_pyth\p7zip_16.02+dfsg-8_amd64.deb" , "/home/kes/p7zip_16.02+dfsg-8_amd64.deb")
    res.append(ssh_checkout("localhost", "kes", "1", "echo '1' | sudo -S dpkg -i /home/kes/p7zip_16.02+dfsg-8_amd64.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("localhost", "kes", "1", "echo '1' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)

if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")


