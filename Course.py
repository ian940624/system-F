class Course:
    def __init__(self, name, teacher, schedule, location="未指定"):
        self.name = name
        self.teacher = teacher  # 指派負責的老師
        self.schedule = schedule  # 上課時間
        self.location = location  # 教室地點
        self.students = []  # 存放修課學生

    def enroll_student(self, student):
        """學生選課時，檢查是否超過 3 門課限制"""
        if len(student.courses) < 3:
            student.enroll(self)
            self.students.append(student)
            print(f"✅ {student.name} 選擇了 {self.name} (時間: {self.schedule}, 地點: {self.location})")
        else:
            print(f"⚠️ {student.name} 已達選課上限 (3 門)，無法選擇 {self.name}！")

    def get_info(self):
        print(f"課程: {self.name}, 授課老師: {self.teacher.name}, 時間: {self.schedule}, 地點: {self.location}")
        print("修課學生:")
        for student in self.students:
            print(f"- {student.name} ({student.student_id})")
