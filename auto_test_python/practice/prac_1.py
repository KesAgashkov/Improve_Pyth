import subprocess

# #! /bin/bash
# result=$(cat /etc/os-release)
# if [[ $result == *"jammy"* && $result == *"22.04.01"* && $? == 0 ]];
# then echo "SUCCESS"
# else echo "FAIL"

def script_1():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        res = result.stdout.split("\n")
        print(res)
        if "VERSION_CODENAME=jammy" in res and 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in res:
            print("SUCCESS")
        else:
            print("FAIL")

script_1()
