import os


def popUtil(command):
    p = os.popen(command)
    g = p.buffer.read().decode("utf-8")
    p.close()
    return g
