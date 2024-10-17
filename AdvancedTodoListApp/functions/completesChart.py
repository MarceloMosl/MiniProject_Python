import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


def completesChart(tasks: list):

    if len(tasks) == 0:
        print("Please complete one tasks before creating the chart. :D")
        return

    task_dates = [task["deadline"] for task in tasks]

    date_counts = Counter(task_dates)

    # date_counts = {"2024-10-17": 3, "2024-10-18": 1, "2024-10-11": 4}

    dates = list(date_counts.keys())

    # dates = ["2024-10-17", "2024-10-18",  "2024-10-11"]

    high_priority_counts = [0] * len(dates)  # [0, 0, 0]        # len(dates) = 3
    medium_priority_counts = [0] * len(dates)
    low_priority_counts = [0] * len(dates)

    for i, date in enumerate(dates):
        tasks_for_date = [task for task in tasks if task["deadline"] == date]
        priority_counts = Counter(task["priority"] for task in tasks_for_date)

        high_priority_counts[i] = priority_counts.get("high", 0)
        medium_priority_counts[i] = priority_counts.get("medium", 0)
        low_priority_counts[i] = priority_counts.get("low", 0)

    plt.bar(dates, high_priority_counts, color="red", label="High")
    plt.bar(
        dates,
        medium_priority_counts,
        bottom=high_priority_counts,
        color="blue",
        label="Medium",
    )
    plt.bar(
        dates,
        low_priority_counts,
        bottom=np.array(high_priority_counts) + np.array(medium_priority_counts),
        color="green",
        label="Low",
    )

    plt.xlabel("Date")
    plt.ylabel("Number of Tasks Completed")
    plt.title("Number of Tasks Completed per Day (Stacked by Priority)")

    plt.legend(loc="upper left")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


# mockData = [
#     {"description": "Homework", "deadline": "2024-01-31", "priority": "Medium"},
#     {"description": "Finish project", "deadline": "2024-02-15", "priority": "High"},
#     {"description": "Grocery shopping", "deadline": "2024-02-05", "priority": "Low"},
#     {"description": "Pay bills", "deadline": "2024-02-05", "priority": "Medium"},
#     {
#         "description": "Meeting with client",
#         "deadline": "2024-01-20",
#         "priority": "High",
#     },
#     {
#         "description": "Read book for class",
#         "deadline": "2024-02-10",
#         "priority": "Medium",
#     },
#     {"description": "Laundry", "deadline": "2024-01-18", "priority": "Low"},
#     {
#         "description": "Complete coding assignment",
#         "deadline": "2024-01-28",
#         "priority": "High",
#     },
#     {"description": "Workout at gym", "deadline": "2024-01-22", "priority": "Low"},
#     {
#         "description": "Research for project",
#         "deadline": "2024-02-12",
#         "priority": "Medium",
#     },
#     {
#         "description": "Prepare presentation",
#         "deadline": "2024-01-25",
#         "priority": "High",
#     },
#     {
#         "description": "Book dentist appointment",
#         "deadline": "2024-02-01",
#         "priority": "Low",
#     },
#     {"description": "Study for exam", "deadline": "2024-01-30", "priority": "High"},
#     {"description": "Visit family", "deadline": "2024-02-20", "priority": "Low"},
#     {"description": "Clean house", "deadline": "2024-01-23", "priority": "Medium"},
#     {"description": "Plan vacation", "deadline": "2024-02-28", "priority": "Low"},
#     {"description": "Write blog post", "deadline": "2024-01-29", "priority": "Medium"},
#     {
#         "description": "Complete online course",
#         "deadline": "2024-02-15",
#         "priority": "High",
#     },
#     {"description": "Organize office", "deadline": "2024-01-26", "priority": "Low"},
#     {"description": "Attend conference", "deadline": "2024-02-05", "priority": "High"},
# ]


# completesChart(mockData)
