# Student Grade Management System
import statistics

class GradeManager:
    def __init__(self):
        # Dictionary to store student data: {student_id: {'name': str, 'grades': list}}
        self.students = {}
        # Set to track unique subjects
        self.subjects = set()
        
    def add_student(self, student_id, name):
        """Add a new student to the system"""
        if student_id not in self.students:
            self.students[student_id] = {'name': name, 'grades': []}
            print(f"✅ Student {name} (ID: {student_id}) added successfully!")
        else:
            print(f"❌ Student with ID {student_id} already exists!")
    
    def add_grade(self, student_id, subject, grade):
        """Add a grade for a student in a specific subject"""
        if student_id in self.students:
            # Tuple to store subject and grade together
            grade_entry = (subject, grade)
            self.students[student_id]['grades'].append(grade_entry)
            self.subjects.add(subject)  # Add to set of subjects
            print(f"✅ Grade {grade} added for {self.students[student_id]['name']} in {subject}")
        else:
            print(f"❌ Student with ID {student_id} not found!")
    
    def calculate_average(self, student_id):
        """Calculate average grade for a student"""
        if student_id in self.students:
            grades = self.students[student_id]['grades']
            if grades:
                # Extract just the numeric grades from tuples
                numeric_grades = [grade[1] for grade in grades]
                return sum(numeric_grades) / len(numeric_grades)
            return 0
        return None
    
    def get_grade_distribution(self):
        """Get grade distribution across all students"""
        grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        
        # Loop through all students
        for student_data in self.students.values():
            for subject, grade in student_data['grades']:
                # Conditional statements to categorize grades
                if grade >= 90:
                    grade_counts['A'] += 1
                elif grade >= 80:
                    grade_counts['B'] += 1
                elif grade >= 70:
                    grade_counts['C'] += 1
                elif grade >= 60:
                    grade_counts['D'] += 1
                else:
                    grade_counts['F'] += 1
        
        return grade_counts
    
    def find_top_performers(self, n=3):
        """Find top N performing students"""
        student_averages = []
        
        for student_id, data in self.students.items():
            avg = self.calculate_average(student_id)
            if avg is not None and avg > 0:
                student_averages.append((data['name'], avg, student_id))
        
        # Sort by average grade (descending)
        student_averages.sort(key=lambda x: x[1], reverse=True)
        
        return student_averages[:n]
    
    def get_subject_statistics(self):
        """Get statistics for each subject"""
        subject_grades = {}
        
        # Collect grades by subject
        for student_data in self.students.values():
            for subject, grade in student_data['grades']:
                if subject not in subject_grades:
                    subject_grades[subject] = []
                subject_grades[subject].append(grade)
        
        # Calculate statistics for each subject
        subject_stats = {}
        for subject, grades in subject_grades.items():
            if grades:  # Check if list is not empty
                subject_stats[subject] = {
                    'average': sum(grades) / len(grades),
                    'highest': max(grades),
                    'lowest': min(grades),
                    'count': len(grades)
                }
        
        return subject_stats
    
    def display_report(self):
        """Display comprehensive report"""
        print("\n" + "="*50)
        print("📊 STUDENT GRADE MANAGEMENT REPORT")
        print("="*50)
        
        # Student count
        print(f"Total Students: {len(self.students)}")
        print(f"Subjects Taught: {', '.join(sorted(self.subjects))}")
        
        # Top performers
        print("\n🏆 TOP PERFORMERS:")
        top_students = self.find_top_performers()
        for i, (name, avg, student_id) in enumerate(top_students, 1):
            print(f"{i}. {name} (ID: {student_id}) - Average: {avg:.2f}")
        
        # Grade distribution
        print("\n📈 GRADE DISTRIBUTION:")
        distribution = self.get_grade_distribution()
        for grade, count in distribution.items():
            print(f"Grade {grade}: {count} students")
        
        # Subject statistics
        print("\n📚 SUBJECT STATISTICS:")
        subject_stats = self.get_subject_statistics()
        for subject, stats in subject_stats.items():
            print(f"\n{subject}:")
            print(f"  Average: {stats['average']:.2f}")
            print(f"  Highest: {stats['highest']}")
            print(f"  Lowest: {stats['lowest']}")
            print(f"  Total Grades: {stats['count']}")

# Demo usage
def main():
    gm = GradeManager()
    
    # Add students
    students_data = [
        (101, "Alice Johnson"),
        (102, "Bob Smith"),
        (103, "Carol Davis"),
        (104, "David Wilson"),
        (105, "Emma Brown")
    ]
    
    for student_id, name in students_data:
        gm.add_student(student_id, name)
    
    # Add grades (subject, grade tuples)
    grades_data = [
        (101, "Math", 95), (101, "Science", 88), (101, "English", 92),
        (102, "Math", 78), (102, "Science", 85), (102, "English", 80),
        (103, "Math", 90), (103, "Science", 94), (103, "English", 89),
        (104, "Math", 65), (104, "Science", 70), (104, "English", 68),
        (105, "Math", 88), (105, "Science", 91), (105, "English", 85)
    ]
    
    for student_id, subject, grade in grades_data:
        gm.add_grade(student_id, subject, grade)
    
    # Display comprehensive report
    gm.display_report()
    
    # Interactive menu
    print("\n" + "="*50)
    print("🔧 INTERACTIVE FEATURES")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Add new student")
        print("2. Add grade for existing student")
        print("3. View student average")
        print("4. Generate report")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                gm.add_student(student_id, name)
            except ValueError:
                print("❌ Invalid student ID! Please enter a number.")
        
        elif choice == '2':
            try:
                student_id = int(input("Enter student ID: "))
                subject = input("Enter subject: ")
                grade = float(input("Enter grade: "))
                if 0 <= grade <= 100:
                    gm.add_grade(student_id, subject, grade)
                else:
                    print("❌ Grade must be between 0 and 100!")
            except ValueError:
                print("❌ Invalid input! Please enter valid numbers.")
        
        elif choice == '3':
            try:
                student_id = int(input("Enter student ID: "))
                avg = gm.calculate_average(student_id)
                if avg is not None:
                    name = gm.students[student_id]['name']
                    print(f"📊 {name}'s average grade: {avg:.2f}")
                else:
                    print("❌ Student not found!")
            except ValueError:
                print("❌ Invalid student ID! Please enter a number.")
        
        elif choice == '4':
            gm.display_report()
        
        elif choice == '5':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()