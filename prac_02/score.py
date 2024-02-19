"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

VALID_LOW_SCORE_THRESHOLD = 0
VALID_HIGH_SCORE_THRESHOLD = 100
EXCELLENT_SCORE_THRESHOLD = 90
BAD_SCORE_THRESHOLD = 50


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))
    print(determine_score(random.randint(0, 100)))


def determine_score(score):
    if score < VALID_LOW_SCORE_THRESHOLD or score > VALID_HIGH_SCORE_THRESHOLD:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE_THRESHOLD:
        return "Excellent"
    elif score >= BAD_SCORE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
