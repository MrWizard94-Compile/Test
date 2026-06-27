import argparse
import subprocess
import sys


def run_command(command, description):
    """Executes a shell command and handles errors cleanly."""
    print(f"Executing: {description}...")
    try:
        # shell=True is required on Windows to resolve executable paths correctly
        result = subprocess.run(
            command, shell=True, check=True, text=True, capture_output=True
        )
        if result.stdout:
            print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error during: {description}")
        print(f"Details: {e.stderr.strip()}")
        sys.exit(1)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Automate initial Git repository setup and push."
    )
    parser.add_argument(
        "repo_name",
        type=str,
        help="The name of the remote GitHub repository to target.",
    )

    args = parser.parse_args()

    # Construct the dynamic remote URL
    remote_url = (
        f"https://github.com/MrWizard94-Compile/{args.repo_name}.git"
    )

    # Define the core Git lifecycle pipeline
    commands = [
        ("git init", "Initializing local Git repository"),
        ("git branch -M main", "Renaming primary branch to 'main'"),
        ("git add .", "Staging all files in current directory"),
        ('git commit -m "Initial commit"', "Creating initial commit"),
        (
            f"git remote add origin {remote_url}",
            f"Linking remote URL: {remote_url}",
        ),
        ("git push -u origin main", "Pushing local commits to GitHub main"),
    ]

    # Sequentially execute each automation step
    for cmd, desc in commands:
        run_command(cmd, desc)

    print("\n[SUCCESS] Git setup pipeline complete!")


if __name__ == "__main__":
    main()
