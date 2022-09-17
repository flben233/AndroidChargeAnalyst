class Config:
    def __init__(self, file_path):
        self.c = open(file_path, encoding="utf-8")
        self.s = self.c.read().split("\n")

    def getVar(self, key):
        flag = True
        for x in self.s:
            if key + "=" in x:
                flag = False
                return x.replace(key + "=", "").strip()
        if flag:
            return None
