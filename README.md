
# ETL Sales Data Pipeline

An end-to-end ETL pipeline built with Python, Pandas, and MySQL.

## What This Project Does
- Extracts raw sales data from a CSV file (1000 records, 10 columns)
- Transforms it using Pandas — cleans column names, fixes date formats, converts currency strings to numbers
- Loads the cleaned data into a MySQL database using SQLAlchemy
- SQL queries generate business insights on top of the loaded data

## Tech Stack
- Python, Pandas, SQLAlchemy
- MySQL, MySQL Workbench

## Key SQL Insights Generated
- Total revenue by country
- Sales by product category
- Monthly revenue trend (2019–2020)

## How to Run
1. Clone this repo
2. Install dependencies: `pip install pandas sqlalchemy mysql-connector-python`
3. Create a MySQL database called `sales_db`
4. Update the DB credentials in `main.py`
5. Run: `python main.py`

## Output
1000 rows successfully loaded into MySQL `sales_data` table.







