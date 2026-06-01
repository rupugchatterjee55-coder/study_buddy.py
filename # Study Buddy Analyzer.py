# Study Buddy Analyzer
import os
import math
from datetime import datetime


def calculate_score(study_hours, mobile_hours):
    score = study_hours * 10 - mobile_hours * 5
    if score < 0:
        score = 0
    elif score > 100:
        score = 100
    return round(score, 1)


def get_nonnegative_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            f = float(val)
            if f < 0:
                print("Please enter a non-negative number.")
                continue
            return f
        except ValueError:
            print("Please enter a valid number (e.g. 2 or 2.5).")


def get_optional_target(prompt):
    val = input(prompt).strip()
    if val == "":
        return None
    try:
        t = float(val)
        if t < 0 or t > 100:
            print("Target must be between 0 and 100. Ignoring target.")
            return None
        return t
    except ValueError:
        print("Invalid target. Ignoring target.")
        return None


def save_report(text, folder="reports"):
    os.makedirs(folder, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"study_report_{ts}.txt"
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    print("===== STUDY BUDDY ANALYZER =====")

    name = input("Enter your name: ").strip() or "Anonymous"

    study_hours = get_nonnegative_float("How many hours do you study daily? ")
    mobile_hours = get_nonnegative_float("How many hours do you use mobile daily? ")
    days_left = get_nonnegative_float("Days left for exam: ")

    target = get_optional_target("Enter desired target score (0-100) or press Enter to skip: ")

    score = calculate_score(study_hours, mobile_hours)

    print("\nGenerating Report...")
    for _ in range(3):
        print("...")

    lines = []
    lines.append("===== REPORT =====")
    lines.append(f"Name: {name}")
    lines.append(f"Study Hours (daily): {study_hours}")
    lines.append(f"Mobile Hours (daily): {mobile_hours}")
    lines.append(f"Days left for exam: {days_left}")
    lines.append(f"Study Score: {score}/100")

    if score >= 70:
        lines.append("Assessment: Excellent! Keep it up.")
    elif score >= 40:
        lines.append("Assessment: Good, but you can improve.")
    else:
        lines.append("Assessment: You need to focus more on studies.")

    if study_hours < mobile_hours:
        lines.append("Suggestion: Reduce mobile usage.")
    else:
        lines.append("Suggestion: Great balance between study and mobile usage.")

    if days_left <= 30:
        lines.append("Note: Exam is near! Revise daily.")
    else:
        lines.append("Note: You have enough time. Stay consistent.")

    if target is not None:
        # score = study_hours*10 - mobile_hours*5
        # required study_hours to reach target: study_needed = (target + mobile_hours*5)/10
        study_needed = (target + mobile_hours * 5) / 10.0
        study_needed_ceiled = math.ceil(study_needed * 10) / 10.0
        extra_hours_total = max(0.0, study_needed_ceiled - study_hours)
        if extra_hours_total <= 0:
            lines.append(f"Target {target} already achieved or no extra study needed.")
        else:
            if days_left > 0:
                extra_per_day = math.ceil((extra_hours_total / max(1, int(days_left))) * 10) / 10.0
            else:
                extra_per_day = extra_hours_total
            lines.append(f"Target: {target}")
            lines.append(f"Estimated study hours needed (daily) to reach target: {study_needed_ceiled}")
            lines.append(f"Additional hours required total: {extra_hours_total}")
            lines.append(f"Suggested extra per day: {extra_per_day}")

    report_text = "\n".join(lines)
    print("\n" + report_text)

    save_choice = input("\nSave this report to file? (y/N): ").strip().lower()
    if save_choice == "y":
        path = save_report(report_text)
        print(f"Report saved to: {path}")

    print("\nThank you for using Study Buddy Analyzer!")


if __name__ == "__main__":
    main()