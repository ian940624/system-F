from Student import Student
from Teacher import Teacher
from Course import Course


teacher1 = Teacher("李安成", "li_teacher@example.com")
teacher2 = Teacher("王心瑀", "wang_prof@example.com")
teacher3 = Teacher("張家寧", "chang_lecturer@example.com")
teacher4 = Teacher("林重複", "lin_ta@example.com")


courses = [
    Course("Python 程式設計", teacher1, "週一 10:00-12:00", "K101"),
    Course("資料結構", teacher2, "週二 14:00-16:00", "K205"),
    Course("人工智慧導論", teacher1, "週三 08:00-10:00", "K301"),
    Course("數據分析", teacher2, "週四 16:00-18:00", "K402"),
    Course("機器學習基礎", teacher3, "週五 09:00-11:00", "K503"),
    Course("Web 全端開發", teacher3, "週一 14:00-16:00", "K601"),
    Course("行動應用程式開發", teacher4, "週二 10:00-12:00", "K702"),
    Course("演算法設計", teacher4, "週三 13:00-15:00", "K803")
]


print("🎓 歡迎來到選課系統！請先註冊學生資訊。")
students = []
num_students = int(input("請輸入要註冊的學生人數: "))

for i in range(num_students):
    print(f"\n📌 註冊第 {i + 1} 位學生")
    student = Student.register_student()
    students.append(student)


print("\n📚 可選課程如下：")
for i, course in enumerate(courses, start=1):
    print(f"{i}. {course.name} - {course.teacher.name} ({course.schedule}, {course.location})")


for student in students:
    print(f"\n🎯 {student.name}，請選擇最多 3 堂課程！")
    selected_courses = input("請輸入課程編號（以逗號分隔，例如 1,2,3）: ").split(',')

    for course_index in selected_courses:
        try:
            course = courses[int(course_index) - 1]
            course.enroll_student(student)
        except (IndexError, ValueError):
            print(f"⚠️ 無效的課程編號: {course_index}")


print("\n✅ 選課完成，最終結果如下：")
for student in students:
    student.get_info()