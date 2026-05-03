 # student management system 
 # Done by : Rathinakumar , Anbuchelvan
 # sectinon 3
 
class Student:
    def __init__(self, sid, name, fee, m1, m2, m3):
        self.sid = sid
        self.name = name
        self.total_fee = fee
        self.marks = [m1, m2, m3]

        self.cgpa = self.calculate_cgpa()
        self.scholarship = self.calculate_scholarship()
        self.paid_fee = 0

    def calculate_cgpa(self):
        avg = sum(self.marks) / len(self.marks)
        return avg / 10

    def calculate_scholarship(self):
        if self.cgpa >= 9:
            return 0.5 * self.total_fee
        elif self.cgpa >= 7.5:
            return 0.25 * self.total_fee
        else:
            return 0

    def pay_fee(self, amount):
        self.paid_fee += amount

    def get_balance(self):
        final_fee = self.total_fee - self.scholarship
        return final_fee - self.paid_fee

    def display(self):
        print("\n--- Student Details ---")
        print(f"ID: {self.sid}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"CGPA: {self.cgpa:.2f}")
        print(f"Total Fee: {self.total_fee}")
        print(f"Scholarship: {self.scholarship}")
        print(f"Paid: {self.paid_fee}")
        print(f"Balance: {self.get_balance():.2f}")

        if self.get_balance() <= 0:
            print("Status: Fully Paid")
        else:
            print("Status: Pending")
students = {}

def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    fee = float(input("Enter Total Fee: "))

    print("Enter Marks (out of 100):")
    m1 = float(input("Python: "))
    m2 = float(input("Maths: "))
    m3 = float(input("DSA: "))

    students[sid] = Student(sid, name, fee, m1, m2, m3)
    print("Student added!")

def pay_fee():
    sid = input("Enter ID: ")
    if sid in students:
        amt = float(input("Enter amount: "))
        students[sid].pay_fee(amt)
        print("Payment done!")
    else:
        print("Student not found")

def view_students():
    for s in students.values():
        s.display()

def search_student():
    sid = input("Enter ID: ")
    if sid in students:
        students[sid].display()
    else:
        print("Not found")

while True:
    print("\n" + "="*35)
    print("      STUDENT MANAGEMENT SYSTEM      ")
    print("="*35)
    print("1.", "Add Student")
    print("2.", "Pay Fee")
    print("3.", "Student Details")
    print("4.","search student")
    print("5.", "Exit")
    print("="*35)

    ch = input("Enter your choice: ")

    if ch == '1':
        add_student()
    elif ch == '2':
        pay_fee()
    elif ch == '3':
        view_students()
    elif ch == '4':
        search_student()

    elif ch == '5':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice")