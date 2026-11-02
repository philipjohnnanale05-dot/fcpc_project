class Gradebook:
    def __init__(self):
        # Create a list of lists
        self.grades = [
            [85, 90, 88],
            [92, 87, 95],
            [78, 85, 80]
        ]
    # Display all grades
    def display(self):
        print("Class Gradebook:")
        for row in self.grades:
            print(row)
    # Access a grade
    def access_grade(self, row, position):
        print("Grade:", self.grades[row][position])
    # Update a grade
    def update_grade(self, row, position, new_grade):
        self.grades[row][position] = new_grade
    # Add a grade
    def add_grade(self, row, new_grade):
        self.grades[row].append(new_grade)
    # Insert a grade
    def insert_grade(self, row, position, new_grade):
        self.grades[row].insert(position, new_grade)
    # Remove a grade by value
    def remove_grade(self, row, grade):
        self.grades[row].remove(grade)
    # Delete a grade by position
    def delete_grade(self, row, position):
        self.grades[row].pop(position)
    # Count rows and grades
    def check_length(self):
        print("Number of rows:", len(self.grades))
        print("Grades in the first row:", len(self.grades[0]))
# Create an object
my_class = Gradebook()
# Test the methods
my_class.display()
my_class.access_grade(1, 2)
my_class.update_grade(1, 2, 98)
my_class.add_grade(0, 95)
my_class.insert_grade(0, 1, 89)
my_class.remove_grade(2, 85)
my_class.delete_grade(1, 0)
print("\nUpdated Gradebook:")
my_class.display()
my_class.check_length()