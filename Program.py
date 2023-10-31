student = Student(1, "Иван Иванов", "10-Б")
subject = Subject("Математика", "Мария Петровна")
diary = Diary(student)

diary.grades[subject] = [5, 4, 5]

diary.homework[subject] = "Решить уравнение"