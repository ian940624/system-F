import os

class Student:
    MAX_COURSES = 3  # 設定選課上限為 3 堂課

    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.courses = []  # 存放已選的課程

    def enroll(self, course):
        """選課時檢查上限"""
        if len(self.courses) < self.MAX_COURSES:
            self.courses.append(course)
            print(f"✅ {self.name} 成功選課: {course.name}")
        else:
            print(f"⚠️ {self.name} 已達選課上限 ({self.MAX_COURSES} 堂)，無法再選 {course.name}!")

    def get_info(self):
        print(f"學生姓名: {self.name}, 學號: {self.student_id}, Email: {self.email}")
        print("已選課程:", [course.name for course in self.courses])

    @staticmethod
    def register_student():
        """讓學生自行輸入註冊資訊"""
        name = input("請輸入姓名: ")
        student_id = input("請輸入學號: ")
        email = input("請輸入 Email: ")
        return Student(name, student_id, email)
