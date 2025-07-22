# feedback_filter.py
import csv

def filter_feedback():
    keywords = ["ERROR", "BUG",]
    filtered_entries = []

    with open("feedback_log.txt", "r") as log_file:
        line = log_file.readline()
        while line:
            if any(keyword in line.upper() for keyword in keywords):
                filtered_entries.append(line.strip())
            line = log_file.readline()

    with open("feedback_summary.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Timestamp", "User", "Feedback"])
        for entry in filtered_entries:
            try:
                timestamp = entry.split(']')[0][1:]
                rest = entry.split(']')[1].strip()
                user, feedback = rest.split(":", 1)
                writer.writerow([timestamp, user.strip(), feedback.strip()])
            except ValueError:
                continue  # skip bad lines

    print("✅ Summary saved to 'feedback_summary.csv'.")

if __name__ == "__main__":
    filter_feedback()
