
# copy_iframe_figures.py 

import shutil
import os

source = "code/notebooks/iframe_figures"
target = "_build/html/code/notebooks/iframe_figures"

print(f"[copy_iframe_figures.py] Copying {source} -> {target}")

# Ensure target directory exists
os.makedirs(os.path.dirname(target), exist_ok=True)

# Copy the directory (overwriting if needed)
if os.path.exists(target):
    shutil.rmtree(target)
shutil.copytree(source, target)

print("[copy_iframe_figures.py] Done.")

