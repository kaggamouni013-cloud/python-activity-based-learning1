'''#Algorithm
Start.

Store the seating arrangement in a nested list, where each inner list represents a row of seats.

Generate seat assignments for registered participants using their registration IDs.

Calculate the total seating capacity from the nested list.

Accept ticket registration IDs for entry validation.

Check whether each ticket ID exists in the registration list.

Detect duplicate entries by checking whether the ID has already been used.

If the ID is valid and not previously used, allow entry; otherwise, reject it.

Calculate available seating capacity by subtracting assigned seats from total capacity.

Display seating assignments, entry validation results, duplicate entries, and available capacity.

Stop.

#flowchart
Start
Initialize nested seating list and registration IDs
Generate seating assignments and calculate total capacity
Read ticket registration ID
Is the ticket ID registered?
Yes

Check for duplicate entry
Allow entry if new; otherwise reject
No

Reject invalid ticket
Allow entry if new; otherwise reject
No

Reject invalid ticket
Calculate available seating capacity and display report
Stop

Code

# File name: campus_event.py
# Campus Event Seating and Entry Validation

# Nested list representing rows of seats
seating = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

# Registered participants and their assigned seats
registrations = {
    "REG101": "A1",
    "REG102": "A2",
    "REG103": "A3",
    "REG104": "B1",
    "REG105": "B2",
    "REG106": "B3"
}

# Calculate total seating capacity
total_capacity = sum(len(row) for row in seating)

# Track seats assigned and tickets already used
assigned_seats = set(registrations.values())
entered_tickets = set()
duplicate_entries = []

# Sample ticket scans (includes duplicate and invalid IDs)
ticket_scans = [
    "REG101",
    "REG102",
    "REG101",
    "REG110",
    "REG104",
    "REG105"
]

print("CAMPUS EVENT SEATING AND ENTRY REPORT")
print("-" * 42)

# Display seating assignments
print("\nSeating Assignments:")
for row in seating:
    for seat in row:
        participant = next(
            (reg for reg, s in registrations.items()
             if s == seat),
            "Available"
        )
        print(f"{seat}: {participant}", end=" | ")
    print()

# Validate tickets
print("\nTicket Validation:")
for ticket in ticket_scans:
    if ticket not in registrations:
        print(f"{ticket}: Invalid ticket")
    elif ticket in entered_tickets:
        print(f"{ticket}: Duplicate entry rejected")
        duplicate_entries.append(ticket)
    else:
        entered_tickets.add(ticket)
        print(f"{ticket}: Entry allowed")

# Calculate seating capacity
available_seats = total_capacity - len(assigned_seats)

print("\nEvent Summary:")
print("Total seating capacity:", total_capacity)
print("Assigned seats:", len(assigned_seats))
print("Available seats:", available_seats)
print("Successful entries:", len(entered_tickets))
print("Duplicate entries:", duplicate_entries)
print("Unused registered tickets:",
      len(registrations) - len(entered_tickets))
output
CAMPUS EVENT SEATING AND ENTRY REPORT
------------------------------------------

Seating Assignments:
A1: REG101 | A2: REG102 | A3: REG103 |
B1: REG104 | B2: REG105 | B3: REG106 |
C1: Available | C2: Available | C3: Available |

Ticket Validation:
REG101: Entry allowed
REG102: Entry allowed
REG101: Duplicate entry rejected
REG110: Invalid ticket
REG104: Entry allowed
REG105: Entry allowed

Event Summary:
Total seating capacity: 9
Assigned seats: 6
Available seats: 3
Successful entries: 4
Duplicate entries: ['REG101']
Unused registered tickets: 2'''