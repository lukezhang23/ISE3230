"""
initialize_project.py

This script runs all data_generation scripts needed to generate data and related artifacts.
"""

import subprocess
import sys


def run_script(script_name):
    """Run a Python script and stop if it fails."""
    result = subprocess.run([sys.executable, script_name])
    if result.returncode != 0:
        print(f"Error: {script_name} failed with exit code {result.returncode}")
        sys.exit(result.returncode)


if __name__ == "__main__":
    run_script("generate_data.py")
    run_script("generate_chart.py")
    run_script("pdf_to_png.py")

    print("All scripts ran successfully!")
