import schedule
import time
import random
import string
from commit_generator import commit_generator
import sys

def set_number_of_commits():
    return random.randint(5, 25)


def alter_file():
    # Read the content of the file
    file_path = 'alterable_file.py'

    # Make your alterations to the content (replace 'old_content' with your specific changes)
    random_content = ''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(400))

    # Write the random content to the file
    with open(file_path, 'w') as file:
        file.write(random_content)

def change_and_commit():
    num = set_number_of_commits()
    for i in range(num):
        alter_file()
        commit_generator(i+1)


def schedule_random_daily():
    # Get a random time within the 24-hour period
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)

    # Schedule the function to run at the random time every day
    schedule.every().day.at(
        f"{random_hour:02d}:{random_minute:02d}").do(change_and_commit)

    print(
        f"Function scheduled to run at {random_hour:02d}:{random_minute:02d} every day.")


if __name__ == "__main__":
    while True:
        # Pick a new random time at midnight
        midnight = "00:00"
        schedule.every().day.at(midnight).do(schedule_random_daily)

        # Run the scheduler continuously
        while True:
            schedule.run_pending()
            time.sleep(1)
