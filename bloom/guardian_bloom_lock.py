import os
import hashlib
from datetime import datetime

# Path to the guardian lock file
lock_path = "capsules/inner_garden/guardian.lock"

# Generate SHA-3 hash of latest commit
def get_latest_commit_hash():
    with os.popen("git rev-parse HEAD") as stream:
        return stream.read().strip()

# Update guardian.lock with current timestamp and hash
def update_guardian_lock():
    if not os.path.exists(lock_path):
        print("guardian.lock not found.")
        return

    sha = get_latest_commit_hash()
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    with open(lock_path, "r") as file:
        lines = file.readlines()

    with open(lock_path, "w") as file:
        for line in lines:
            if "sha3_hash:" in line:
                file.write(f"sha3_hash: {sha}\\n")
            elif "timestamp:" in line:
                file.write(f"timestamp: {timestamp}\\n")
            else:
                file.write(line)

    print("guardian.lock updated successfully.")

if __name__ == "__main__":
    update_guardian_lock()
