import requests


def download(url, file_name, progress_bar):
    t = 0
    f = open(file_name, "wb")
    file = requests.get(url, stream=True)
    total_size = int(file.headers['content-length'])
    for chunk in file.iter_content(chunk_size=1024):
        t += len(chunk)
        if chunk:
            f.write(chunk)
            progress_bar.setValue(int((t / total_size) * 100))
            # print((t / total_size) * 100)
    f.close()
    progress_bar.setValue(100)
