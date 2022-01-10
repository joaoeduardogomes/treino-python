from datetime import date

class Data:
    def __init__(self):
        self.d = (f"{date.today().day} / {date.today().month} / {date.today().year}")
        print(self.d)


