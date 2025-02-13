import os
from dotenv import load_dotenv
load_dotenv()
import psycopg2

POSTGRES_URL = os.environ["POSTGRES_API"] 
connection = psycopg2.connect(POSTGRES_URL)
cursor = connection.cursor()

def ExecuteSQL(SQL):
    sql = SQL.lower()
    print(sql)
    if "insert" in sql:
        cursor.execute(SQL)
        connection.commit()
        return "Data Inserted Successfully"
    else:
        cursor.execute(SQL)
        # print(cursor.fetchall())
        if cursor.rowcount == 0:
            return "No Data Found"
        return cursor.fetchall()

# ExecuteSQL("INSERT INTO Expenses (date, amount, category, description) VALUES ('2024-03-15', 250, 'Groceries', 'Groceries');")
# ExecuteSQL("SELECT * FROM Expenses WHERE description ILIKE ANY (ARRAY['aata']);")