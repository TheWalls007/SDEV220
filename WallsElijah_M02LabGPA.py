"""
Honors or not calculator

Elijah Walls

Created 3/29/24

This calculator takes inputs of student names and GPAs and test if the student 
qualifies for either the Dean's List or the Honor Roll.

Ver 1.0 updated 3/30/24
"""

# Main function for program
def main():
    while True:
        # Ask for student's last name, if user enters ZZZ then the program ends
        lastName = input("Enter the student's last name (Enter 'ZZZ' to quit): ").strip().upper()
        if lastName == 'ZZZ':
            break
        # Ask for student's first name and their GPA
        firstName = input("Enter the student's first name: ").strip().capitalize()
        gpa = float(input("Enter the student's GPA: "))
        
        # Test if entered GPA qualifies for Dean's list or Honor roll
        if gpa >= 3.5:
            print(f"{firstName} {lastName} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{firstName} {lastName} has made the Honor Roll.")
        # print statement for if student doesn't qualify for either Honor roll or Dean's list
        else:
            print(f"Unfortunately, {firstName} {lastName} did not qualify for any honors.")

# Run the program            
if __name__ == "__main__":
    main()