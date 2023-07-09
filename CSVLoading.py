import timeit
import duckdb
import pandas as pd



path = "/workspaces/learn_duckdb/housing/housing.tgz"
# results = duckdb.sql(f"SELECT * FROM read_csv_auto('{path}', compression=gzip, header=True, ignore_errors=True)").to_df()
# # SELECT * FROM read_csv_auto(['flights1.csv', 'flights2.csv'], union_by_name=True)
# # results = duckdb.sql("SELECT * FROM read_csv_auto(['flights1.csv', 'flights2.csv'], union_by_name=True)").to_df()
# print(results.columns)
# results.info()
# print(results)

conn = duckdb.connect()
conn.execute("INSTALL httpfs")
conn.execute("LOAD httpfs")
start = timeit.default_timer()
#Your statements here
# results = duckdb.sql(f"SELECT * FROM read_csv_auto('{path}', compression=gzip, header=True, ignore_errors=True, filename=True)").to_df()
# results = duckdb.sql(f"SELECT * FROM read_csv_auto('{path}', compression=gzip, header=True, ignore_errors=True, filename=True)")
# results = duckdb.sql(f"SELECT * FROM read_csv_auto('{path}', compression=gzip, header=True, ignore_errors=True)")
results = duckdb.sql(f"SELECT row_number() OVER () as row_number, * FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet')")
print(results)
# results.info()
# print(results)
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
#Your statements here
# results = pd.read_csv(path, compression='gzip', sep=",")
results = pd.read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet")
results = results.reset_index()
print(results)
# results.info()
# print(results)
stop = timeit.default_timer()
print('Time: ', stop - start)

