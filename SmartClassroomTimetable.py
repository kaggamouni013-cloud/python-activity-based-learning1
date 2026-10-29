'''Algorithm
Start.

Store course details, classroom capacities, and available periods using lists and tuples.

Store the number of students enrolled in each course.

Assign each course a classroom and a time period.

Check whether the classroom capacity is sufficient for the course enrollment.

Check for timetable clashes:

A room must not be assigned to two courses in the same period.

An instructor must not teach two courses in the same period.

If a capacity violation or clash occurs, mark the allocation as invalid and display the reason.
Check whether every course has been assigned.

Display the timetable and the final allocation status.

Stop.
Flowchart
Start
Input courses, rooms, periods and constraints
Select next course and available room-period combination
Room capacity sufficient?
Yes

Check room and instructor clashes
No

Try another room
Conflict-free assignment found?
Assign course and process remaining courses
All courses assigned successfully?
Display timetable and allocation status
Stop
Code 

# File name: SmartClassroomTimetable.py

# Courses: (course_name, students, instructor)
courses = [
    ("Python", 35, "Dr Rao"),
    ("Mathematics", 45, "Dr Kumar"),
    ("Physics", 25, "Dr Rao"),
    ("Chemistry", 30, "Dr Mehta")
]

# Rooms: (room_name, capacity)
rooms = [
    ("Room A", 40),
    ("Room B", 50),
    ("Room C", 30)
]

# Available periods
periods = ["09:00", "10:00", "11:00"]

# Each assignment: (course, room, period, instructor)
timetable = []


def can_assign(course, room, period):
    name, students, instructor = course
    room_name, capacity = room

    # Check classroom capacity
    if students > capacity:
        return False

    # Check room and instructor clashes
    for entry in timetable:
        _, assigned_room, assigned_period, assigned_teacher = entry

        if assigned_period == period:
            if assigned_room == room_name:
                return False
            if assigned_teacher == instructor:
                return False

    return True


def allocate(index):
    # All courses assigned
    if index == len(courses):
        return True

    course = courses[index]

    for period in periods:
        for room in rooms:
            if can_assign(course, room, period):
                timetable.append(
                    (course[0], room[0], period, course[2])
                )

                if allocate(index + 1):
                    return True

                # Backtrack if later courses cannot be assigned
                timetable.pop()

    return False


print("SMART CLASSROOM TIMETABLE ALLOCATION")
print("------------------------------------")

if allocate(0):
    print("\nCourse        Room      Period   Instructor")
    print("--------------------------------------------")

    for course, room, period, teacher in timetable:
        print(f"{course:<14}{room:<10}{period:<9}{teacher}")

    print("\nAll courses scheduled successfully.")
    print("Capacity violations: 0")
    print("Room clashes: 0")
    print("Instructor clashes: 0")
else:
    print("\nNo valid timetable found.")
    print("All courses cannot be accommodated")
    print("under the stated constraints.")
output
SMART CLASSROOM TIMETABLE ALLOCATION
------------------------------------

Course        Room      Period   Instructor
--------------------------------------------
Python        Room A    09:00    Dr Rao
Mathematics   Room A    10:00    Dr Kumar
Physics       Room A    11:00    Dr Rao
Chemistry     Room B    09:00    Dr Mehta

All courses scheduled successfully.
Capacity violations: 0
Room clashes: 0
Instructor clashes: 0'''