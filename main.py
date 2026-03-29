import pandas as pd
from sqlalchemy import create_engine

# ── STEP 1: Load the CSV ──────────────────────────────────────
df = pd.read_csv("Sales_data.csv")
print("✅ Data loaded. Rows:", len(df))
print("Columns:", df.columns.tolist())

# ── STEP 2: Clean column names ────────────────────────────────
# Your file has spaces in column names — this removes them
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("\n✅ Cleaned columns:", df.columns.tolist())

# ── STEP 3: Clean the data ────────────────────────────────────
# order_value_EUR has commas like "17,524.02" — convert to number
df["order_value_eur"] = df["order_value_eur"].str.replace(",", "").astype(float)

# Convert date column to proper date format
df["date"] = pd.to_datetime(df["date"])

# Drop any null rows (none in your file, but good practice)
df.dropna(inplace=True)

print("✅ Data cleaned. Sample:")
print(df.head(3))
print("\nData types:")
print(df.dtypes)

# ── STEP 4: Load into MySQL ───────────────────────────────────
# Replace 'root' and 'yourpassword' with your MySQL username and password
engine = create_engine("mysql+mysqlconnector://root:12345@localhost/sales_db")

df.to_sql("sales_data", con=engine, if_exists="replace", index=False)

print("\n✅ Data successfully loaded into MySQL!")
print("Total rows inserted:", len(df))


