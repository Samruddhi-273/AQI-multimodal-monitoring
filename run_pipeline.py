"""
AQI Multimodal Environmental Monitoring Pipeline

Runs the complete pipeline in sequence.

Author: Samruddhi Magadum
"""

import subprocess
import sys
from pathlib import Path

# ======================================================
# Check Required Datasets
# ======================================================

required_files = [
    "data/raw/station_hour.csv",
    "data/raw/stations.csv"
]

missing = [file for file in required_files if not Path(file).exists()]

if missing:
    print("\n❌ Required dataset(s) not found!\n")

    for file in missing:
        print(f"Missing: {file}")

    print("\n📥 Please download the datasets from the Google Drive link provided in README.md")
    print("After downloading, place them inside:")
    print("data/raw/\n")

    sys.exit(1)

# ======================================================
# Function to Run Scripts
# ======================================================

def run_script(script):

    print(f"\n{'='*60}")
    print(f"Running: {script}")
    print(f"{'='*60}")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\n❌ Error while running {script}")
        sys.exit(1)

    print(f"✅ Completed: {script}")

# ======================================================
# Pipeline
# ======================================================

pipeline = [

    "src/data_collection.py",
    "src/data_validation.py",
    "src/imputation.py",
    "src/data_fusion.py",
    "src/feature_engineering.py",
    "src/physics.py",
    "src/quality_score.py",
    "src/sensor_drift_detection.py",
    "src/outlier_visualization.py",
    "src/model.py",
    "src/model_comparison.py"

]

# ======================================================
# Execute Pipeline
# ======================================================

if __name__ == "__main__":

    print("\n🌍 AQI Multimodal Environmental Monitoring Pipeline")

    for script in pipeline:
        run_script(script)

    print("\n🎉 Pipeline Finished Successfully!")