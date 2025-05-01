class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

    def checkStatus(self):
        if self.marks >= 500:
            print(f"🎉 Congratulations {self.name}, You passed with {self.marks} marks 😊")
        else:
            print(f"😔 Sorry {self.name}, You failed with {self.marks} marks.")


student1 = Student("Hammad", 600)

# we call both methods(🐍) 
student1.display()
student1.checkStatus()
