import os
from cs50 import SQL

uri = os.getenv("DATABASE_URL")
is_postgres = False
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
    is_postgres = True

db = SQL(uri if uri else "sqlite:///finance.db")

schema_file = "schema_postgres.sql" if is_postgres else "schema.sql"

with open(schema_file, "r") as f:
    schema_script = f.read()

# cs50 SQL requires executing one statement at a time
for statement in schema_script.split(';'):
    if statement.strip():
        db.execute(statement.strip())

print("Database created successfully using " + schema_file)