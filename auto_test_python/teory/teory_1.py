import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False



# checkout("ls", "sem")
# # import subprocess
# # result = subprocess.Popen("ls", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=0x08000000)
# #
#
