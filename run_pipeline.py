"""
AQI Multimodal Environmental Monitoring Pipeline

Runs the complete pipeline in sequence.

Author: Samruddhi Magadum
"""

import subprocess
import sys


def run_script(script):
    print(f"\n{'='*60}")
    print(f"Running: {script}")
    print(f"{'='*60}")

    result = subprocess.run(
        [sys.executable, script]
    )

    if result.returncode != 0:
        print(f"\n❌ Error while running {script}")
        exit()

    print(f"✅ Completed: {script}")


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


if __name__ == "__main__":

    print("\n🌍 AQI Multimodal Environmental Monitoring Pipeline")

    for script in pipeline:
        run_script(script)

    print("\n🎉 Pipeline Finished Successfully!")