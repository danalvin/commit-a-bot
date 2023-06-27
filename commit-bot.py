import os
import time
from git import Repo

# Define the repository path
repo_path = "//home/waituika/projects/commit-a-bot"

# Function to create a commit
def create_commit():
    # Get the current time
    current_time = time.strftime("%H:%M:%S", time.localtime())

    # Append the time to the commit message
    commit_message = f"Commit at {current_time}"

    # Create a new file with the commit message
    file_path = os.path.join(repo_path, f"{current_time}.txt")
    with open(file_path, "w") as file:
        file.write(commit_message)

    # Stage and commit the changes
    repo = Repo(repo_path)
    repo.index.add([file_path])
    repo.index.commit(commit_message)

# Create six commits per day
while True:
    create_commit()
    time.sleep(3 * 60)  # Sleep for 3 minutes