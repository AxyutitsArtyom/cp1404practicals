"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

VALID_LOW_SCORE_THRESHOLD = 0
VALID_HIGH_SCORE_THRESHOLD = 100
EXCELLENT_SCORE_THRESHOLD = 90
BAD_SCORE_THRESHOLD = 50

score = float(input("Enter score: "))
if score < VALID_LOW_SCORE_THRESHOLD or score > VALID_HIGH_SCORE_THRESHOLD:
    print("Invalid score")
elif score >= EXCELLENT_SCORE_THRESHOLD:
    print("Excellent")
elif score >= BAD_SCORE_THRESHOLD:
    print("Passable")
else:
    print("Bad")
