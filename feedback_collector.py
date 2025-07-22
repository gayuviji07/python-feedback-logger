# feedback_collector.py
from datetime import datetime

def collect_feedback():
    with open("feedback_log.txt", "a") as log_file:
        while True:
            name = input("Enter your name (or type 'exit' to quit): ")
            if name.lower() == "exit":
                break
            feedback = input("Enter your feedback: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"[{timestamp}] {name}: {feedback}\n"
            log_file.write(entry)
            print("✅ Feedback recorded.\n")

if __name__ == "__main__":
    collect_feedback()
