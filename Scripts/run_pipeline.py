import subprocess
import sys
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

SCRIPT_DIR = Path(__file__).resolve().parent

CLEAN_SCRIPT = SCRIPT_DIR / "clean_data.py"
LOAD_SCRIPT = SCRIPT_DIR / "load_postgresql.py"


# ============================================================
# RUN COMPLETE PIPELINE
# ============================================================

def run_pipeline():

    print("=" * 60)
    print("STARTING SALES AUTOMATION PIPELINE")
    print("=" * 60)

    # --------------------------------------------------------
    # Check scripts
    # --------------------------------------------------------

    if not CLEAN_SCRIPT.exists():

        raise FileNotFoundError(
            f"\nCleaning script not found:\n{CLEAN_SCRIPT}"
        )

    if not LOAD_SCRIPT.exists():

        raise FileNotFoundError(
            f"\nPostgreSQL loading script not found:\n{LOAD_SCRIPT}"
        )

    # --------------------------------------------------------
    # STEP 1: CLEAN DATA
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("STEP 1: CLEANING SALES DATA")
    print("=" * 60)

    subprocess.run(
        [
            sys.executable,
            str(CLEAN_SCRIPT)
        ],
        check=True
    )

    print("\nData cleaning completed successfully!")

    # --------------------------------------------------------
    # STEP 2: LOAD INTO POSTGRESQL
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("STEP 2: LOADING DATA INTO POSTGRESQL")
    print("=" * 60)

    subprocess.run(
        [
            sys.executable,
            str(LOAD_SCRIPT)
        ],
        check=True
    )

    print("\nPostgreSQL loading completed successfully!")

    # --------------------------------------------------------
    # PIPELINE COMPLETED
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("SALES AUTOMATION PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nPipeline:")
    print("Raw sales data")
    print("      ↓")
    print("Data cleaning")
    print("      ↓")
    print("Cleaned Excel file")
    print("      ↓")
    print("PostgreSQL")
    print("      ↓")
    print("sales table")
    print("=" * 60)


# ============================================================
# RUN PIPELINE
# ============================================================

if __name__ == "__main__":
    run_pipeline()
