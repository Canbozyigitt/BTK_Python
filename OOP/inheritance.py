class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person created.")

    def who_am_i(self):
        print("I am a person.")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created.")

    def who_am_i(self):
        print("Im a student.")

class Teacher(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.teacherNumber = number
        print("Teacher created.")

    def who_am_i(self):
        print("I'm a teacher.")


mustafa = Student(fname="Mustafa", lname="Haita", number=12345)
mustafa.who_am_i()