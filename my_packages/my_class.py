class User:
    def __init__(self,name,mail_address,point):
        self.name = name
        self.mail_address = mail_address
        self.point = point

    def add_point(self,point):
        self.point += point


