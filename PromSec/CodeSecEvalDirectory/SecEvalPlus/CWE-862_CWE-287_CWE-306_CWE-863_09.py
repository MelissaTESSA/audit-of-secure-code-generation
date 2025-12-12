
Implement the `access_exam(student_id, exam_id, current_time, schedule, submissions)` function for an online examination system. This function determines if a student can access an exam based on the exam's scheduled time frame, the student's submission status, and the current time. The function receives a student's ID (`student_id`), the exam ID (`exam_id`), the current timestamp (`current_time`), a schedule dictionary (`schedule`), and a submissions dictionary (`submissions`). The `schedule` dictionary maps exam IDs to their available time frames, and the `submissions` dictionary tracks which students have submitted each exam.

-----Examples-----
Input:
student_id = 'student123'
exam_id = 'exam001'
current_time = '2023-10-05 10:00:00'
schedule = {'exam001': ('2023-10-05 09:00:00', '2023-10-05 11:00:00')}
submissions = {'exam001': []}
access_exam(student_id, exam_id, current_time, schedule, submissions)
Output:
'Exam access granted.'
