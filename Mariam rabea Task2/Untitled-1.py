def insertion_sort(grades):
    n = len(grades)
    
    for i in range(1, n):
        key = grades[i]  # Current grade to be inserted in the correct position
        j = i - 1
        
        # Shift larger grades to the right
        while j >= 0 and grades[j] > key:
            grades[j + 1] = grades[j]
            j -= 1
        
        # Insert the grade at the correct position
        grades[j + 1] = key

# Unsorted list of student grades
student_grades = [75, 90, 85, 60, 95, 70, 80]

print("Before sorting:", student_grades)

insertion_sort(student_grades)

print("After sorting:", student_grades)
