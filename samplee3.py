import numpy as np

attendance = np.array([[1, 1],
                       [1, 0],
                       [1, 1],
                       [0, 1]])

per_student = np.sum(attendance, axis=1)
overall = np.sum(attendance)

print("Attendance matrix:\n", attendance)
print("Total per student:", per_student)
print("Overall attendance:", overall)