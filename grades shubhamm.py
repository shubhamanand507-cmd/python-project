import os
import sys

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.subjects = {
            'Calculus': 0,
            'Physics': 0,
            'Programming': 0,
            'English': 0,
            'Electronics': 0
        }
        self.total_marks = 0
        self.percentage = 0.0
        self.result = ""
        self.failed_subjects = []
        self.needs_supplementary = False
        self.supplementary_subject = ""

    def get_marks_from_user(self):
        print(f"\nGetting marks for {self.name} (Roll: {self.roll_number})")
        print("----------------------------------------")
        
        for subject in self.subjects:
            while True:
                try:
                    marks_input = input(f"Marks for {subject} (0-100): ")
                    marks = float(marks_input)
                    if marks < 0 or marks > 100:
                        print("Marks should be between 0 and 100!")
                        continue
                    self.subjects[subject] = marks
                    break
                except:
                    print("Please enter numbers only!")

    def compute_result(self):
        # Adding marks
        self.total_marks = 0
        for marks in self.subjects.values():
            self.total_marks += marks
        
        # Find percentage
        self.percentage = (self.total_marks / 500) * 100
        
        # Checking failed subjects
        self.failed_subjects = []
        for subject, marks in self.subjects.items():
            if marks < 40:
                self.failed_subjects.append(subject)
        
        # Final result
        if len(self.failed_subjects) == 0:
            # All subjects passed
            self.result = "PASS"
            self.needs_supplementary = False
        elif len(self.failed_subjects) == 1 and self.percentage >= 40:
            # one subject failed but overall good
            self.result = "PASS"
            self.needs_supplementary = True
            self.supplementary_subject = self.failed_subjects[0]
        else:
            # Either multiple fails or low overall percentage
            self.result = "FAIL"
            self.needs_supplementary = False

    def show_result(self):
        print("\n" + "=" * 60)
        print("VIT BHOPAL - MID SEMESTER RESULT")
        print("=" * 60)
        print(f"NAME: {self.name}")
        print(f"ROLL NUMBER: {self.roll_number}")
        print("\nMARKS OBTAINED:")
        print("-" * 25)
        
        for subject, marks in self.subjects.items():
            passed = "PASS" if marks >= 40 else "FAIL"
            print(f"{subject:12} : {marks:5.1f}/100  - {passed}")
        
        print("\nFINAL RESULT:")
        print("-" * 12)
        print(f"TOTAL MARKS: {self.total_marks}/500")
        print(f"PERCENTAGE: {self.percentage:.2f}%")
        print(f"RESULT: {self.result}")
        
        if self.needs_supplementary:
            print(f"\nNOTE: You passed but failed in {self.supplementary_subject}")
            print("You need to give supplementary exam!")
            print(f"Subject: {self.supplementary_subject}")
        elif self.failed_subjects:
            print(f"\nFailed in: {', '.join(self.failed_subjects)}")
            if len(self.failed_subjects) > 1:
                print("Failed in multiple subjects")
            else:
                print("Overall percentage is below 40%")
        else:
            print("\nWell done! Cleared all subjects")
        
        # final status
        if self.result == "PASS" and not self.needs_supplementary:
            print("Status: Full Pass - No supplementary needed")
        elif self.result == "PASS" and self.needs_supplementary:
            print("Status: Pass with supplementary")
        else:
            print("Status: Failed - Must reappear for exams")
        
        print("=" * 60)

def process_multiple_students():
    student_list = []
    
    print("VIT BHOPAL - STUDENT RESULT SYSTEM")
    print("==================================")
    
    while True:
        # Getting students information
        student_name = input("\nStudent Name: ").strip()
        roll_no = input("Roll Number: ").strip()
        
        if not student_name or not roll_no:
            print("Please enter both name and roll number!")
            continue
        
        # Create new student
        new_student = Student(student_name, roll_no)
        
        # Get marks
        new_student.get_marks_from_user()
        
        # Calculate result
        new_student.compute_result()
        
        # Show result
        new_student.show_result()
        
        # Save to list
        student_list.append(new_student)
        
        # Ask if user wants to continue
        another = input("\nProcess another student? (y/n): ").strip().lower()
        if another not in ['y', 'yes']:
            break
    
    # Show final summary if multiple students
    if len(student_list) > 1:
        show_final_summary(student_list)

def show_final_summary(all_students):
    print("\n" + "=" * 80)
    print("FINAL SUMMARY - ALL STUDENTS")
    print("=" * 80)
    print(f"{'Name':<18} {'Roll No':<12} {'Total':<8} {'%':<10} {'Result':<8} {'Status':<15} {'Remarks'}")
    print("-" * 80)
    
    for student in all_students:
        # Determine status
        if student.needs_supplementary:
            status_text = "Need Suppl"
            remark_text = f"Suppl in {student.supplementary_subject}"
        elif student.result == "PASS":
            status_text = "Clear Pass"
            remark_text = "All clear"
        else:
            status_text = "Failed"
            if len(student.failed_subjects) > 1:
                remark_text = f"Failed in {len(student.failed_subjects)} subjects"
            else:
                remark_text = "Low overall %"
        
        print(f"{student.name:<18} {student.roll_number:<12} {student.total_marks:<8} {student.percentage:<10.2f} {student.result:<8} {status_text:<15} {remark_text}")
    
    # Calculate statistics
    passed_all = [s for s in all_students if s.result == "PASS" and not s.needs_supplementary]
    need_suppl = [s for s in all_students if s.needs_supplementary]
    failed_all = [s for s in all_students if s.result == "FAIL"]
    total_passed = len(passed_all) + len(need_suppl)
    
    print("\nRESULT STATISTICS:")
    print(f"Total students processed: {len(all_students)}")
    print(f"Clear pass: {len(passed_all)}")
    print(f"Pass with supplementary: {len(need_suppl)}")
    print(f"Failed: {len(failed_all)}")
    print(f"Overall pass rate: {(total_passed/len(all_students))*100:.2f}%")
    
    if need_suppl:
        print(f"\nStudents needing supplementary:")
        for student in need_suppl:
            print(f"  - {student.name} ({student.roll_number}): {student.supplementary_subject}")
    
    print("=" * 80)

def clear_screen():
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    clear_screen()
    print("\nVIT Bhopal University - Result System")
    print("-------------------------------------")
    print("How it works:")
    print("• Need 40 marks in each subject to pass")
    print("• Need 40% overall to pass")
    print("• If fail in 1 subject but have 40% overall: PASS but need supplementary")
    print("\nOptions:")
    print("1. Check one student")
    print("2. Check multiple students")
    print("3. See the rules again")
    print("4. Quit")
    
    try:
        choice = input("\nChoose option (1-4): ").strip()
        return choice
    except:
        return "4"

def show_rules():
    print("\n" + "=" * 65)
    print("HOW RESULTS ARE CALCULATED")
    print("=" * 65)
    print("1. FOR EACH SUBJECT:")
    print("   • Need at least 40 marks to pass a subject")
    print("   • Subjects: Calculus, Physics, Programming, English, Electronics")
    print()
    print("2. OVERALL PASSING:")
    print("   • Need at least 40% total percentage")
    print()
    print("3. SPECIAL CASE:")
    print("   • If you fail in ONLY ONE subject")
    print("   • AND your total percentage is 40% or more")
    print("   • THEN: You PASS but must give supplementary for that one subject")
    print("   • This doesn't work if you fail in more than one subject")
    print()
    print("4. POSSIBLE RESULTS:")
    print("   • FULL PASS: Pass all subjects with 40% or more overall")
    print("   • PASS WITH SUPPLEMENTARY: Pass overall but fail in one subject")
    print("   • FAIL: Fail in multiple subjects OR have less than 40% overall")
    print("=" * 65)
    input("\nPress Enter to continue...")

def main():
    while True:
        user_choice = show_main_menu()
        
        if user_choice == '1':
            # Single student
            clear_screen()
            name = input("Student Name: ").strip()
            roll = input("Roll Number: ").strip()
            
            if name and roll:
                student = Student(name, roll)
                student.get_marks_from_user()
                student.compute_result()
                student.show_result()
                
                input("\nPress Enter to continue...")
            else:
                print("Please enter both name and roll number!")
                input("Press Enter to continue...")
                
        elif user_choice == '2':
            # Multiple students
            clear_screen()
            process_multiple_students()==input("\nPress Enter to continue...")
            
        elif user_choice == '3':
            # Show rules
            clear_screen()
            show_rules()
            
        elif user_choice == '4':
            # Exit
            print("\nThanks for using VIT Bhopal Result System!")
            print("Goodbye!")
            break
            
        else:
            print("Please choose 1, 2, 3, or 4!")
            input("Press Enter to continue...")

if __name__ == "__main__":   
    main()