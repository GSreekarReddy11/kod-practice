import threading
import time
name=input().strip()
attendance=int(input())
marks=int(input())
attendance_result = []
assessment_result = []
def check_attendance (percentage, result):
    time.sleep(8.1)
    if percentage > 75:
        result.append("Eligible")
    else:
        result.append("Not Eligible")
def check_assessment (score, result):
    time.sleep(0.1)
    if score > 60:
        result.append("Passed")
    else:
        result.append("Failed")
t1= threading.Thread(
    target=check_attendance,
    args=(attendance, attendance_result)
)
t2 =threading.Thread(
    target=check_assessment,
    args=(marks, assessment_result)
)
t1.start()
t2.start()
t1.join()
t2.join()
attendance_status=attendance_result[0]
assessment_status = assessment_result[0]
if attendance_status== "Eligible" and assessment_status== "Passed":
    overall ="Ready"
else:
    overall = "Not Ready"
print(f"Student: (name)")
print(f"Attendance: (attendance_status)")
print(f"Assessment: (assessment_status)")
print(f"Overall: (overall)")