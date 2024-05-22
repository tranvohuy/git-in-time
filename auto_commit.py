import os
import yaml
import random
import subprocess

# Load the timestamps from the YAML file
def load_timestamps(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data['timestamps']

# Append text to a file
def append_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + '\n')

# Automate the commits
def make_commits(timestamps, commit_file):
    for timestamp in timestamps:
        n = random.randint(1, 10)
        for i in range(1, n + 1):
            # Append the timestamp to the file
            append_to_file(commit_file, timestamp)

            # Commit the change with the timestamp
            commit_message = f"Date {timestamp} with the {i}/{n} commits"
            env = os.environ.copy()  # Copy the current environment
            env.update({
                "GIT_AUTHOR_DATE": timestamp,
                "GIT_COMMITTER_DATE": timestamp
            })
            try:
                subprocess.run(["git", "add", commit_file], check=True)
                subprocess.run(
                    ["git", "commit", "-m", commit_message],
                    env=env,
                    check=True
                )
                print(f"Committed: {commit_message}")
            except subprocess.CalledProcessError as e:
                print(f"Error during commit: {e}")
                break

# Main function
if __name__ == "__main__":
    yaml_file = "working_day.yml"
    commit_file = "commit.txt"

    timestamps = load_timestamps(yaml_file)
    make_commits(timestamps, commit_file)
