# Study Buddy Analyzer

def calculate_score(study_hours, mobile_hours):
    score = study_hours * 10 - mobile_hours * 5

    if score < 0:
        score = 0
    elif score > 100:
        score = 100

    return score


print("===== STUDY BUDDY ANALYZER =====")

name = input("Enter your name: ")
study_hours = int(input("How many hours do you study daily? "))
mobile_hours = int(input("How many hours do you use mobile daily? "))
days_left = int(input("Days left for exam: "))

score = calculate_score(study_hours, mobile_hours)

print("\nGenerating Report...")

for i in range(3):
    print("...")
    
print("\n===== REPORT =====")
print("Name:", name)
print("Study Score:", score, "/100")

if score >= 70:
    print("Excellent! Keep it up.")
elif score >= 40:
    print("Good, but you can improve.")
else:
    print("You need to focus more on studies.")

if study_hours < mobile_hours:
    print("Suggestion: Reduce mobile usage.")
else:
    print("Great balance between study and mobile usage.")

if days_left <= 30:
    print("Exam is near! Revise daily.")
else:
    print("You have enough time. Stay consistent.")

print("\nThank you for using Study Buddy Analyzer!")