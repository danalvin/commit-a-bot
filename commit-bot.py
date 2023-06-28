import os
import time
from git import Repo

# Define the repository path
repo_path = "//home/waituika/projects/commit-a-bot"


# Define the file to update
file_path = "//home/waituika/projects/commit-a-bot/file.txt"

# Function to create a commit
def create_commit():
    # Get the current time
    current_time = time.strftime("%H:%M:%S", time.localtime())

    # Append the time to the existing file
    commit_message = f"Commit at {current_time}\n"

    # Open the file in append mode and write the commit message
    with open(file_path, "a") as file:
        file.write(commit_message)

    # Stage and commit the changes
    repo = Repo(repo_path)
    repo.index.add([file_path])
    repo.index.commit(commit_message)

# Create commits every 3 minutes
commit_count = 0
table_header = ["Commit Count", "Time"]
commit_table = []

while True:
    create_commit()
    commit_count += 1
    current_time = time.strftime("%H:%M:%S", time.localtime())
    commit_table.append([commit_count, current_time])
    print(tabulate(commit_table, headers=table_header, tablefmt="fancy_grid"))
    time.sleep(3 * 60)  # Sleep for 3 minutes