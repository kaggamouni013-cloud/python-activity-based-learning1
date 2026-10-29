'''Algorithm
Objective: Compare students’ answers with an answer key, calculate question-wise success rates, identify the most frequently missed questions, and classify question difficulty.

Start the program.

Store the correct answer key and student answer strings.

Initialize counters for correct answers for each question.

Compare each student's answer with the corresponding correct answer.

Increase the question's correct-answer count when the answers match.

Calculate the success rate for each question:
    Success Rate= 
Total Students
Correct Answers
​
 ×100
Calculate the number of students who missed each question.

Identify the question or questions with the highest number of incorrect answers.

Classify question difficulty using the success rate:

Easy: 80% or higher

Moderate: 50% to below 80%

Difficult: Below 50%

Display question-wise results, success rates, difficulty classifications, and the most frequently missed questions.

Stop.
flowchart

flowchart TD
    A([Start]) --> B[Input answer key and student answers]
    B --> C[Initialize question-wise counters]
    C --> D[Compare each student answer with key]
    D --> E{Answer correct?}
    E -- Yes --> F[Increment correct count]
    E -- No --> G[Count incorrect answer]
    F --> H{More answers?}
    G --> H
    H -- Yes --> D
    H -- No --> I[Calculate success rates]
    I --> J[Classify question difficulty]
    J --> K[Find most frequently missed questions]
    K --> L[Display analysis report]
    L --> M([Stop])

code 

# Examination Question Difficulty and Performance Analysis

# Correct answer key
answer_key = ["A", "B", "C", "D", "A"]

# Student answers (each list represents one student)
students = {
    "Student 1": ["A", "B", "C", "D", "A"],
    "Student 2": ["A", "C", "C", "D", "B"],
    "Student 3": ["B", "B", "D", "A", "A"],
    "Student 4": ["A", "B", "C", "C", "B"],
    "Student 5": ["C", "D", "B", "D", "A"]
}

total_students = len(students)
total_questions = len(answer_key)

correct_count = [0] * total_questions

print("===== EXAM PERFORMANCE ANALYSIS =====")

# Compare student answers with the answer key
for student, answers in students.items():
    score = 0

    for q in range(total_questions):
        if q < len(answers) and answers[q].strip().upper() == answer_key[q]:
            correct_count[q] += 1
            score += 1

    print(f"{student}: {score}/{total_questions}")

# Calculate question-wise performance
success_rates = []
missed_counts = []

print("\n===== QUESTION-WISE ANALYSIS =====")

for q in range(total_questions):
    rate = (correct_count[q] / total_students) * 100
    missed = total_students - correct_count[q]

    success_rates.append(rate)
    missed_counts.append(missed)

    if rate >= 80:
        difficulty = "Easy"
    elif rate >= 50:
        difficulty = "Moderate"
    else:
        difficulty = "Difficult"

    print(
        f"Question {q + 1}: "
        f"Correct={correct_count[q]}, "
        f"Missed={missed}, "
        f"Success Rate={rate:.1f}%, "
        f"Difficulty={difficulty}"
    )

# Find all questions tied for the highest number of misses
max_missed = max(missed_counts)
hardest_questions = [
    q + 1 for q, count in enumerate(missed_counts)
    if count == max_missed
]

print("\n===== MOST FREQUENTLY MISSED QUESTIONS =====")
print("Question(s):", ", ".join(map(str, hardest_questions)))
print(f"Students missing each: {max_missed}/{total_students}")

print("\n===== SUMMARY =====")
print("Total students:", total_students)
print("Total questions:", total_questions)
print("Total responses:", total_students * total_questions)
print("Overall correct answers:", sum(correct_count))
overall_rate = (
    sum(correct_count) / (total_students * total_questions)
) * 100
print(f"Overall success rate: {overall_rate:.1f}%")
output
===== EXAM PERFORMANCE ANALYSIS =====
Student 1: 5/5
Student 2: 3/5
Student 3: 2/5
Student 4: 3/5
Student 5: 2/5

===== QUESTION-WISE ANALYSIS =====
Question 1: Correct=3, Missed=2, Success Rate=60.0%, Difficulty=Moderate
Question 2: Correct=3, Missed=2, Success Rate=60.0%, Difficulty=Moderate
Question 3: Correct=3, Missed=2, Success Rate=60.0%, Difficulty=Moderate
Question 4: Correct=3, Missed=2, Success Rate=60.0%, Difficulty=Moderate
Question 5: Correct=3, Missed=2, Success Rate=60.0%, Difficulty=Moderate

===== MOST FREQUENTLY MISSED QUESTIONS =====
Question(s): 1, 2, 3, 4, 5
Students missing each: 2/5

===== SUMMARY =====
Total students: 5
Total questions: 5
Total responses: 25
Overall correct answers: 15
Overall success rate: 60.0%'''