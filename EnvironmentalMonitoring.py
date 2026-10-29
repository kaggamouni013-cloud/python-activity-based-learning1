'''Algorithm
Start.

Input the nested list of environmental readings, where each inner list represents readings from one monitoring station.

Input the threshold value for classification.

Initialize variables to store the total, minimum, maximum, and number of readings.

Traverse each nested list using loops.

Calculate the average, minimum, and maximum readings.

Classify each observation:

If reading is less than or equal to the threshold, classify it as Safe.

Otherwise, classify it as Unsafe.

Display the average, minimum, maximum, and classification of each reading.
Stop
Flowchart
Start
Input nested readings and threshold
Traverse all readings using nested loops
Calculate average, minimum and maximum
Is reading ≤ threshold?
Yes

Classify as Safe
No

Classify as Unsafe
Display results
Stop
code 

# File name: EnvironmentalMonitoring.py

# Nested lists of air-quality readings (AQI)
readings = [
    [35, 45, 55],
    [60, 75, 85],
    [25, 40, 50]
]

threshold = 50

all_readings = []

print("Environmental Monitoring Data Analyzer")
print("---------------------------------------")

for i, station in enumerate(readings, start=1):
    average = sum(station) / len(station)
    minimum = min(station)
    maximum = max(station)

    print(f"\nMonitoring Station {i}")
    print("Readings:", station)
    print(f"Average: {average:.2f}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

    for value in station:
        all_readings.append(value)
        status = "Safe" if value <= threshold else "Unsafe"
        print(f"Reading {value}: {status}")

# Overall environmental summary
print("\nOverall Summary")
print("----------------")
print(f"Overall Average: {sum(all_readings) / len(all_readings):.2f}")
print(f"Overall Minimum: {min(all_readings)}")
print(f"Overall Maximum: {max(all_readings)}")
print(f"Threshold: {threshold}")
output
Environmental Monitoring Data Analyzer
---------------------------------------

Monitoring Station 1
Readings: [35, 45, 55]
Average: 45.00
Minimum: 35
Maximum: 55
Reading 35: Safe
Reading 45: Safe
Reading 55: Unsafe

Monitoring Station 2
Readings: [60, 75, 85]
Average: 73.33
Minimum: 60
Maximum: 85
Reading 60: Unsafe
Reading 75: Unsafe
Reading 85: Unsafe

Monitoring Station 3
Readings: [25, 40, 50]
Average: 38.33
Minimum: 25
Maximum: 50
Reading 25: Safe
Reading 40: Safe
Reading 50: Safe

Overall Summary
----------------
Overall Average: 52.78
Overall Minimum: 25
Overall Maximum: 85
Threshold: 50'''