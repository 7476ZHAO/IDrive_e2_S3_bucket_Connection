from spark_session import get_spark

spark = get_spark()

# 1️ Create a local DataFrame
df = spark.createDataFrame([
    (1, "Alice"),
    (2, "Sarah")
], ["id", "name"])

# 2️ Write to S3 (Delta format)
df.write.format("delta").mode("overwrite").save("s3a://3c-scsu-bucket/test")

# 3️ Read back from S3 to verify
df2 = spark.read.format("delta").load("s3a://3c-scsu-bucket/test")
df2.show()
