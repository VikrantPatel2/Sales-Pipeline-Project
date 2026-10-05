import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from urllib.parse import quote_plus


# ============================================================
# PROJECT PATHS
# ============================================================

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

INPUT_FILE = PROJECT_DIR / "data" / "cleaned_sales.xlsx"


# ============================================================
# POSTGRESQL DATABASE CONFIGURATION
# ============================================================

DB_USER = "postgres"

# CHANGE THIS TO YOUR ACTUAL POSTGRESQL PASSWORD
DB_PASSWORD = 'YourPassword'

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "sales_automation"


# ============================================================
# LOAD DATA INTO POSTGRESQL
# ============================================================

def load_data():

    print("=" * 60)
    print("STARTING POSTGRESQL DATA LOADING")
    print("=" * 60)

    # --------------------------------------------------------
    # Check cleaned file
    # --------------------------------------------------------

    print("\nInput file:")
    print(INPUT_FILE)

    if not INPUT_FILE.exists():

        raise FileNotFoundError(
            f"\nCleaned file not found:\n{INPUT_FILE}\n\n"
            "Please run clean_data.py first."
        )

    # --------------------------------------------------------
    # Read cleaned Excel file
    # --------------------------------------------------------

    print("\nReading cleaned data...")

    df = pd.read_excel(INPUT_FILE)

    print(f"Rows loaded from Excel: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    # --------------------------------------------------------
    # Display columns
    # --------------------------------------------------------

    print("\nColumns being loaded:")

    for column in df.columns:
        print(f" - {column}")

    # --------------------------------------------------------
    # Check password
    # --------------------------------------------------------

    if DB_PASSWORD == "YOUR_POSTGRES_PASSWORD":

        raise ValueError(
            "\nPlease change DB_PASSWORD in load_postgresql.py "
            "to your actual PostgreSQL password."
        )

    # --------------------------------------------------------
    # Create PostgreSQL connection
    # --------------------------------------------------------

    print("\nConnecting to PostgreSQL...")

    encoded_password = quote_plus(DB_PASSWORD)

    connection_string = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{encoded_password}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(
        connection_string,
        pool_pre_ping=True
    )

    # --------------------------------------------------------
    # Test PostgreSQL connection
    # --------------------------------------------------------

    try:

        with engine.connect() as connection:

            print("PostgreSQL connection successful!")

    except Exception as error:

        print("\n" + "=" * 60)
        print("POSTGRESQL CONNECTION FAILED")
        print("=" * 60)

        print("\nError:")
        print(error)

        print("\nPlease check:")
        print("1. PostgreSQL server is running")
        print("2. Username is correct")
        print("3. PostgreSQL password is correct")
        print("4. Database 'sales_automation' exists")
        print("5. PostgreSQL is running on port 5432")

        raise

    # --------------------------------------------------------
    # Load data into PostgreSQL
    # --------------------------------------------------------

    print("\nLoading data into PostgreSQL...")

    try:

        df.to_sql(
            name="sales",
            con=engine,
            if_exists="replace",
            index=False
        )

        print("Data loaded successfully!")

    except Exception as error:

        print("\nError while loading data:")
        print(error)

        raise

    # --------------------------------------------------------
    # Verify loaded data
    # --------------------------------------------------------

    print("\nVerifying data in PostgreSQL...")

    try:

        with engine.connect() as connection:

            result = connection.exec_driver_sql(
                'SELECT COUNT(*) FROM "sales";'
            )

            row_count = result.scalar()

        print(f"Rows loaded into PostgreSQL: {row_count}")

    except Exception as error:

        print("\nCould not verify the data:")
        print(error)

        raise

    # --------------------------------------------------------
    # Final result
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("POSTGRESQL LOADING COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(f"Database : {DB_NAME}")
    print("Table    : sales")
    print(f"Rows     : {row_count}")
    print("=" * 60)


# ============================================================
# RUN SCRIPT
# ============================================================

if __name__ == "__main__":
    load_data()