class Teacher:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        print(f"老師姓名: {self.name}, Email: {self.email}")