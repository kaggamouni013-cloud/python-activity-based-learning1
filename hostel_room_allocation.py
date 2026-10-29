'''Algorithm
Objective: Allocate students to hostel rooms based on room capacity, eligibility requirements, and grouping constraints. Detect duplicate assignments and calculate the number of students who remain unallocated.

Start the program.

Store student details, including student ID, gender, and group.

Store room details, including room number, capacity, eligible gender, and permitted group.

Initialize an empty room-allocation list.

For each student:

Check whether the student has already been assigned a room.

Find a room that meets the student's eligibility requirements.

Check whether the room has available capacity.

Check the grouping constraints.
Check the grouping constraints.

If a suitable room is found, allocate the student and update the room occupancy.

If no suitable room is available, add the student to the unallocated list.

Check for duplicate student assignments.

Calculate the total unallocated demand.

Display room allocations, occupancy, duplicate assignments, and unallocated students.

Stop.
Flowchart

flowchart TD
    A([Start]) --> B[Load student and room details]
    B --> C[Initialize allocations and occupancy]
    C --> D[Select next student]
    D --> E{More students?}
    E -- No --> K[Check duplicate assignments]
    E -- Yes --> F[Find an eligible room]
    F --> G{Capacity and grouping valid?}
    G -- Yes --> H[Allocate student and update occupancy]
    G -- No --> I{Another room available?}
    I -- Yes --> F
    I -- No --> J[Add student to unallocated list]
    H --> L[Process next student]
    J --> L
    L --> D
    K --> M[Calculate unallocated demand]
    M --> N[Display allocation report]
    N --> O([Stop])
code 

# University Hostel Room Allocation

students = [
    {"id": "S101", "gender": "F", "group": "G1"},
    {"id": "S102", "gender": "F", "group": "G1"},
    {"id": "S103", "gender": "M", "group": "G2"},
    {"id": "S104", "gender": "M", "group": "G2"},
    {"id": "S105", "gender": "F", "group": "G1"},
    {"id": "S106", "gender": "M", "group": "G3"},
    {"id": "S107", "gender": "F", "group": "G3"},
    {"id": "S108", "gender": "M", "group": "G2"}
]

rooms = [
    {"room": "R101", "capacity": 2, "gender": "F", "group": "G1"},
    {"room": "R102", "capacity": 2, "gender": "M", "group": "G2"},
    {"room": "R103", "capacity": 1, "gender": "F", "group": "G1"},
    {"room": "R104", "capacity": 1, "gender": "M", "group": "G3"},
    {"room": "R105", "capacity": 1, "gender": "F", "group": "G3"}
]

allocations = {room["room"]: [] for room in rooms}
assigned_students = set()
duplicates = []
unallocated = []

for student in students:
    sid = student["id"]

    # Detect duplicate student records/assignments
    if sid in assigned_students:
        duplicates.append(sid)
        continue

    assigned_students.add(sid)
    allocated = False

    for room in rooms:
        rid = room["room"]

        # Check eligibility, grouping, and room capacity
        if (
            student["gender"] == room["gender"]
            and student["group"] == room["group"]
            and len(allocations[rid]) < room["capacity"]
        ):
            allocations[rid].append(sid)
            allocated = True
            break

    if not allocated:
        unallocated.append(sid)

# Report
print("===== HOSTEL ROOM ALLOCATION =====")

for room in rooms:
    rid = room["room"]
    occupants = allocations[rid]
    print(
        f"{rid}: {occupants} "
        f"({len(occupants)}/{room['capacity']} occupied)"
    )

print("\n===== DUPLICATE ASSIGNMENTS =====")
if duplicates:
    print(", ".join(duplicates))
else:
    print("None")

print("\n===== UNALLOCATED STUDENTS =====")
if unallocated:
    print(", ".join(unallocated))
else:
    print("None")

print("\n===== SUMMARY =====")
total_students = len(students)
allocated_count = sum(len(v) for v in allocations.values())

print("Total student records:", total_students)
print("Students allocated:", allocated_count)
print("Students unallocated:", len(unallocated))
print("Duplicate records detected:", len(duplicates))
print("Total room capacity:", sum(r["capacity"] for r in rooms))
output
===== HOSTEL ROOM ALLOCATION =====
R101: ['S101', 'S102'] (2/2 occupied)
R102: ['S103', 'S104'] (2/2 occupied)
R103: ['S105'] (1/1 occupied)
R104: ['S106'] (1/1 occupied)
R105: ['S107'] (1/1 occupied)

===== DUPLICATE ASSIGNMENTS =====
None

===== UNALLOCATED STUDENTS =====
S108

===== SUMMARY =====
Total student records: 8
Students allocated: 7
Students unallocated: 1
Duplicate records detected: 0
Total room capacity: 7'''