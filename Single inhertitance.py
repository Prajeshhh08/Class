class notification:
    def __init__(self,person,content):
        self.p=person
        self.c=content

class message(notification):
    def __init__(self, person, content,time):
        super().__init__(person, content)
        self.t=time
    def disp(self):
        print(f"You've a message from {self.p} \"{self.c}\" {self.t} seconds ago!")

m=message("Jai","Mankatha polama",10)
m.disp()

