from spark_session import get_spark
from config import DATA_PATH

spark = get_spark()

# 1️ Create a local DataFrame
df = spark.createDataFrame([
    (1, "Alice"),
    (2, "Sarah")
], ["id", "name"])

# 2️ Write to S3 (Delta format)
df.write.format("delta").mode("overwrite").save(DATA_PATH)

# 3️ Read back from S3 to verify
df2 = spark.read.format("delta").load(DATA_PATH)
df2.show()
