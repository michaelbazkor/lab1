"""Verify the serverless Databricks Connect session can read the course data."""
from databricks.connect import DatabricksSession

DATA_PATH = "/Volumes/94290_lab/course_data/airbnb/airbnb_1_12_parquet"

spark = DatabricksSession.builder.profile("lab1").serverless().getOrCreate()

print("server version:", spark.sql("SELECT current_version().dbr_version AS v").first()["v"])
df = spark.read.parquet(DATA_PATH)
print(f"rows: {df.count():,}   columns: {len(df.columns)}")
