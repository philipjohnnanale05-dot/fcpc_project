class Gradebook:
    def __init__(self):
        # Create a list of lists to store student grades
        self.grades = [
            [85, 90, 88],
            [92, 87, 95],
            [78, 85, 80]
        ]

    # Access grades
    def access_grade(self, row, position):
        return self.grades[row][position]

    # Change a grade
    def update_grade(self, row, position, new_grade):
        self.grades[row][position] = new_grade

    # Add a new grade to a row
    def add_grade(self, row, new_grade):
        self.grades[row].append(new_grade)

    # Insert a grade at a specific position
    def insert_grade(self, row, position, new_grade):
        self.grades[row].insert(position, new_grade)

    # Delete a grade by value
    def remove_grade(self, row, grade):
        self.grades[row].remove(grade)

    # Delete a grade by position
    def delete_grade(self, row, position):
        self.grades[row].pop(position)

    # Count rows and items
    def check_grades(self):
        print("Number of rows:", len(self.grades))
        print("Items in the first row:", len(self.grades[0]))

    # Display all grades
    def display_grades(self):
        for row in self.grades:
            print(row)


# Create an object
my_gradebook = Gradebook()

# Display all grades
print("Original Grades:")
my_gradebook.display_grades()

# Access a grade
print("\nAccess grade:", my_gradebook.access_grade(1, 2))

# Update a grade
my_gradebook.update_grade(1, 2, 98)
print("\nAfter updating:")
my_gradebook.display_grades()

# Add a grade
my_gradebook.add_grade(0, 95)
print("\nAfter adding a grade:")
my_gradebook.display_grades()

# Insert a grade
my_gradebook.insert_grade(0, 1, 89)
print("\nAfter inserting a grade:")
my_gradebook.display_grades()

# Remove a grade by value
my_gradebook.remove_grade(2, 85)
print("\nAfter removing a grade:")
my_gradebook.display_grades()

# Delete a grade by position
my_gradebook.delete_grade(1, 0)
print("\nAfter deleting a grade:")
my_gradebook.display_grades()

# Check the number of rows and items
print("\nChecking the Gradebook:")
my_gradebook.check_grades()
