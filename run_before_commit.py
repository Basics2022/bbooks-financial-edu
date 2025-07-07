# run_before_commit.py

import subprocess

print("🔧 Running pre-commit automation steps...\n")

# Step 1: Preprocess / validate
subprocess.run(["python", "copy_iframe_figures.py"], check=True)

# Step 2: Copy iframe_figures
subprocess.run(["python", "add_google_analytics.py"], check=True)

print("\n✅ All pre-commit steps completed successfully.")

