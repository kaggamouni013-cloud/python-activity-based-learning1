'''Algorithm
Start.

Store candidate details, including marks, assessment scores, attendance percentage, and eligibility status.

Define the minimum eligibility criteria:

Academic marks must be at least 60%.

Assessment score must be at least 50%.

Attendance must be at least 75%.

Candidate must satisfy the eligibility conditions.

Calculate the weighted score for each candidate using:

Academic marks: 40%

Assessment score: 40%
Attendance: 20%

Filter out candidates who do not meet all eligibility requirements.

Rank qualified candidates in descending order of weighted score.

Apply deterministic tie-breaking rules:

Higher assessment score ranks first.

If still tied, higher academic marks rank first.

If still tied, higher attendance ranks first.

If still tied, candidate ID in alphabetical order ranks first.

Display the ranked qualified candidates and rejected candidates with their reasons.

Stop.
Flowchart
Start
Input candidate marks, assessment, attendance, and eligibility
Calculate weighted score
Does candidate satisfy all eligibility criteria?
Yes

Add to qualified list
No

Record rejection reason
Sort qualified candidates by score and tie-breaking rules
Display rankings and rejected candidates
Stop
Code 

# File name: internship_ranking.py
# Multi-Criteria Internship Candidate Ranking

candidates = [
    {
        "id": "C104",
        "name": "Ananya",
        "marks": 85,
        "assessment": 90,
        "attendance": 95,
        "eligible": True
    },
    {
        "id": "C102",
        "name": "Rahul",
        "marks": 90,
        "assessment": 90,
        "attendance": 90,
        "eligible": True
    },
    {
        "id": "C101",
        "name": "Priya",
        "marks": 90,
        "assessment": 90,
        "attendance": 90,
        "eligible": True
    },
    {
        "id": "C103",
        "name": "Kiran",
        "marks": 75,
        "assessment": 80,
        "attendance": 70,
        "eligible": True
    },
    {
        "id": "C105",
        "name": "Meera",
        "marks": 55,
        "assessment": 85,
        "attendance": 90,
        "eligible": True
    },
    {
        "id": "C106",
        "name": "Arjun",
        "marks": 80,
        "assessment": 45,
        "attendance": 85,
        "eligible": True
    },
    {
        "id": "C107",
        "name": "Divya",
        "marks": 88,
        "assessment": 82,
        "attendance": 92,
        "eligible": False
    }
]

# Minimum eligibility requirements
MIN_MARKS = 60
MIN_ASSESSMENT = 50
MIN_ATTENDANCE = 75

qualified = []
rejected = []

for c in candidates:
    # Calculate weighted score
    c["score"] = (
        0.40 * c["marks"]
        + 0.40 * c["assessment"]
        + 0.20 * c["attendance"]
    )

    # Collect all applicable rejection reasons
    reasons = []

    if c["marks"] < MIN_MARKS:
        reasons.append("Marks below 60")
    if c["assessment"] < MIN_ASSESSMENT:
        reasons.append("Assessment below 50")
    if c["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75")
    if not c["eligible"]:
        reasons.append("Eligibility condition not met")

    if reasons:
        rejected.append((c, reasons))
    else:
        qualified.append(c)

# Deterministic ranking:
# 1. Higher weighted score
# 2. Higher assessment score
# 3. Higher academic marks
# 4. Higher attendance
# 5. Alphabetically smaller candidate ID
qualified.sort(
    key=lambda c: (
        -c["score"],
        -c["assessment"],
        -c["marks"],
        -c["attendance"],
        c["id"]
    )
)

print("INTERNSHIP CANDIDATE RANKING")
print("=" * 65)
print("\nQualified Candidates:")

print(f"{'Rank':<6}{'ID':<8}{'Name':<12}"
      f"{'Score':<10}{'Assessment':<12}{'Marks':<8}"
      f"{'Attendance':<10}")

for rank, c in enumerate(qualified, start=1):
    print(
        f"{rank:<6}{c['id']:<8}{c['name']:<12}"
        f"{c['score']:<10.2f}{c['assessment']:<12}"
        f"{c['marks']:<8}{c['attendance']:<10}"
    )

print("\nRejected Candidates:")
for c, reasons in rejected:
    print(f"{c['id']} - {c['name']}: "
          + ", ".join(reasons))

print("\nTotal candidates:", len(candidates))
print("Qualified:", len(qualified))
print("Rejected:", len(rejected))
output
INTERNSHIP CANDIDATE RANKING
=================================================================

Qualified Candidates:
Rank  ID      Name        Score     Assessment  Marks   Attendance
1     C101    Priya       90.00     90          90      90
2     C102    Rahul       90.00     90          90      90
3     C104    Ananya      89.00     90          85      95

Rejected Candidates:
C103 - Kiran: Attendance below 75
C105 - Meera: Marks below 60
C106 - Arjun: Assessment below 50
C107 - Divya: Eligibility condition not met

Total candidates: 7
Qualified: 3
Rejected: 4'''