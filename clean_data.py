import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

INPUT_FILE = PROJECT_DIR / "data" / "sales.xls"
OUTPUT_FILE = PROJECT_DIR / "data" / "cleaned_sales.xlsx"


# ============================================================
# DATA CLEANING FUNCTION
# ============================================================

def clean_data():

    print("=" * 60)
    print("STARTING DATA CLEANING")
    print("=" * 60)

    print("\nInput file:")
    print(INPUT_FILE)

    print("\nOutput file:")
    print(OUTPUT_FILE)

    # --------------------------------------------------------
    # Check input file
    # --------------------------------------------------------

    if not INPUT_FILE.exists():

        raise FileNotFoundError(
            f"\nInput file not found:\n{INPUT_FILE}"
        )

    # --------------------------------------------------------
    # Read data
    # --------------------------------------------------------

    print("\nReading sales data...")

    # IMPORTANT:
    # Although the file is named .xls,
    # its contents are actually CSV data.
    df = pd.read_csv(INPUT_FILE)

    print(f"Original rows: {len(df)}")
    print(f"Original columns: {len(df.columns)}")

    # --------------------------------------------------------
    # Display columns
    # --------------------------------------------------------

    print("\nColumns found:")

    for column in df.columns:
        print(f" - {column}")

    # --------------------------------------------------------
    # Remove duplicate rows
    # --------------------------------------------------------

    print("\nChecking duplicate rows...")

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate rows found: {duplicate_count}")

    df = df.drop_duplicates()

    print(
        f"Rows after removing duplicates: {len(df)}"
    )

    # --------------------------------------------------------
    # Convert Order_Date
    # --------------------------------------------------------

    print("\nConverting Order_Date...")

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce"
    )

    invalid_dates = df["Order_Date"].isna().sum()

    print(f"Invalid dates: {invalid_dates}")

    # --------------------------------------------------------
    # Standardize City names
    # --------------------------------------------------------

    print("\nStandardizing City names...")

    df["City"] = df["City"].replace({
        "delhi": "Delhi",
        "MUMBAI": "Mumbai",
        "Bangalore": "Bengaluru",
        "hyderabad": "Hyderabad"
    })

    # --------------------------------------------------------
    # Handle missing City
    # --------------------------------------------------------

    missing_city = df["City"].isna().sum()

    print(f"Missing City values: {missing_city}")

    df["City"] = df["City"].fillna("Unknown")

    # --------------------------------------------------------
    # Handle missing Unit_Price
    # --------------------------------------------------------

    print("\nChecking Unit_Price...")

    missing_price = df["Unit_Price"].isna().sum()

    print(
        f"Missing Unit_Price values: {missing_price}"
    )

    if missing_price > 0:

        median_price = df["Unit_Price"].median()

        print(
            f"Replacing missing Unit_Price "
            f"with median: {median_price}"
        )

        df["Unit_Price"] = df["Unit_Price"].fillna(
            median_price
        )

    # --------------------------------------------------------
    # Recalculate Revenue
    # --------------------------------------------------------

    print("\nRecalculating Revenue...")

    df["Revenue"] = (
        df["Quantity"] *
        df["Unit_Price"]
    )

    # --------------------------------------------------------
    # Calculate Discount Amount
    # --------------------------------------------------------

    print("Calculating Discount Amount...")

    df["Discount_Amount"] = (
        df["Revenue"] *
        df["Discount_Pct"] /
        100
    )

    # --------------------------------------------------------
    # Calculate Net Revenue
    # --------------------------------------------------------

    print("Calculating Net Revenue...")

    df["Net_Revenue"] = (
        df["Revenue"] -
        df["Discount_Amount"]
    )

    # --------------------------------------------------------
    # Create output folder
    # --------------------------------------------------------

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Save cleaned data as Excel
    # --------------------------------------------------------

    print("\nSaving cleaned data...")

    df.to_excel(
        OUTPUT_FILE,
        index=False,
        engine="openpyxl"
    )

    # --------------------------------------------------------
    # Final summary
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("DATA CLEANING COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(f"Original rows: {len(pd.read_csv(INPUT_FILE))}")
    print(f"Final rows: {len(df)}")
    print(f"Final columns: {len(df.columns)}")

    print("\nCleaned file saved to:")
    print(OUTPUT_FILE)

    print("=" * 60)


# ============================================================
# RUN SCRIPT
# ============================================================

if __name__ == "__main__":
    clean_data()