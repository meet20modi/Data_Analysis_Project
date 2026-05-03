from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("C:\\Users\Meet Modi\\OneDrive\\Desktop\\Data Analysis Project\\Result.csv")
print(df.head())
# Step 1: MySQL Connection

username = "root"       # MySQL username
password = "9337"       # your MySQL password
host = "localhost"
port = "3306"           # MySQL default port
database = "db_project" # your MySQL database

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# Step 2: Load DataFrame into MySQL
table_name = "customer"

df.to_sql(table_name, con=engine, if_exists="replace", index=False)

print(f"✅ Data successfully loaded into table '{table_name}' in database '{database}'")