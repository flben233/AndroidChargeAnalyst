import os.path

import gdown
import zipfile

try:
    # url = "https://dl.google.com/android/repository/platform-tools_r33.0.2-windows.zip?hl=zh-cn"
    # output = "platform-tools.zip"
    # gdown.download(url, output, quiet=False)
    # adbFile = zipfile.ZipFile(output)
    # adbFile.extractall(".\\")
    # print(os.path.isdir(".\\adb"))
    os.rename(".\\platform-tools", ".\\adb")
except Exception as e:
    print(e)
