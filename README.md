# Student Management System – README

##  Developed By

- Rathinakumar
- Anbuchelvan
- Section 3

---

## Project Description

This is a simple Student Management System built using Python.
It helps manage student records, calculate CGPA, assign scholarships, and track fee payments.

The system is menu-driven and runs in the console.

---

## ⚙️ Features

- Add new student details
- Record fee payments
- Automatically calculate CGPA
- Scholarship calculation based on CGPA
- Search student by ID
- View all student details
- Payment status (Fully Paid / Pending)

---

##  Logic Used

###  CGPA Calculation

- Average of 3 subject marks is taken
- CGPA = Average / 10

###  Scholarship Rules

- CGPA ≥ 8 → 50% fee reduction
- CGPA ≥ 7.5 → 25% fee reduction
- CGPA < 7.5 → No scholarship

---

##  Project Structure

Student Class
- Stores student details
- Calculates CGPA and scholarship
- Tracks fee payment

Functions:
- add_student() → Adds new student
- pay_fee() → Records payment
- view_students() → Displays all students
- search_student() → Finds student by ID

---

##  How to Run

1. Make sure Python is installed
2. Save the file as student_management.py
3. Open terminal / command prompt
4. Run:

python student_management.py

---

##  Menu Options

1. Add Student
2. Pay Fee
3. Student Details
4. Search Student
5. Exit

---

##  Example Workflow

1. Add a student with marks and fee
2. System calculates CGPA and scholarship
3. Pay fee partially or fully
4. Check remaining balance
5. View student status

---




##  Limitations

- Data is not saved permanently (resets after program exit)
- Works only in command-line interface

---

## Conclusion

This project demonstrates:
- Object-Oriented Programming (OOP)
- Functions
- Conditional logic
- Data handling using dictionaries

---

Simple but powerful beginner project to understand real-world system design in Python.
