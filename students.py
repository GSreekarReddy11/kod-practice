import student_result,student_result1,student_result2
student_name="Sreekar reddy"
roll_no=180
m1=80
m2=35
m3=77
total=m1+m2+m3
average=total/3 

print(student_result.student_details(student_name,roll_no))
print(student_result1.calculate_total(m1,m2,m3))
print(student_result1.calculate_average(total))
print(student_result2.get_result(average))
print(student_result2.show_grade(average))
