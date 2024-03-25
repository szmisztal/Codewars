import subprocess

def git_commit_push(message):
    try:
        subprocess.run(["git", "add", "."], check = True)
        subprocess.run(["git", "commit", "-m", message], check = True)
        subprocess.run(["git", "push"], check = True)
        print("Successfully sending commits on GH")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


git_commit_push("Commit by my script")
