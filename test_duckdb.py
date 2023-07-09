import duckdb

duckdb.sql("SELECT 42").show()

results = duckdb.sql("SELECT 42").fetchall()
print(results)

results = duckdb.sql("SELECT 42").df()
print(results)

con = duckdb.connect('file.db')
con.sql('CREATE TABLE integers(i INTEGER)')
con.sql('INSERT INTO integers VALUES (42)')
con.sql('SELECT * FROM integers').show()