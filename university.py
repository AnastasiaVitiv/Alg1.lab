from array import array


class Student:
    def __init__(self, student_id=0, name="", grades=None):
        self.student_id = student_id
        self.name = name
        self.__grades = grades if grades is not None else array('f')

    def average_grade(self):
        if len(self.__grades) == 0:
            return None

        total = 0
        for grade in self.__grades:
            total += grade

        return total / len(self.__grades)

    def fix_the_students(self):
        average = self.average_grade()
        if average is not None and 40 <= average < 50:
            return f"*{self.name}"
        return self.name


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_ranking(self):
        self.students = [student for student in self.students if (student.average_grade() or 0) >= 40]
        ranked_students = []

        while self.students:
            best_student = self.students[0]
            for student in self.students:
                if student.average_grade() > best_student.average_grade():
                    best_student = student

            ranked_students.append(best_student)
            self.students.remove(best_student)

        print("Рейтинг студентів:")
        for student in ranked_students:
            average = student.average_grade()
            print(f"{student.fix_the_students()}: {average if average is not None else 'Немає оцінок'}")


student1 = Student(1, "Іван Іванов", array('f', [85, 90, 78, 92]))
student2 = Student(2, "Петро Петрович", array('f', [50, 45, 50, 30]))
student3 = Student(3, "Олег Олегович", array('f', [23, 34.4, 0, 47]))
student4 = Student(4, "Віктор Федор", array('f', [100, 99]))

group = Group()

group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
group.add_student(student4)

group.show_ranking()