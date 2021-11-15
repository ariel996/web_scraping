# courseInfo


# assign a variable for the dictionary course and room number
course_room= {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
course_instructor= {'CS101': 'Haynes', 'CS102': 'Alvaraldo', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
course_meeting= {'CS101': '8:00am', 'CS102': '9:00am', 'CS103': '10:00am', 'NT110': '11:00am', 'CM241': '11:00pm'}


for key in course_room:
    print('Course :', course_room.keys())

    user_input = input('Enter a course number to display')
    print(user_input)
    print('Room:', course_room.get(user_input))
    print('Instructor: ', course_instructor.get(user_input))
    print('Meeting: ', course_meeting.get(user_input))























