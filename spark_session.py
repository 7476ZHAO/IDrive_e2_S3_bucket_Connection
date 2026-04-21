from pyspark.sql import SparkSession

def get_spark():
    return SparkSession.builder
        .appName("delta-test")
        .config("spark.jars.packages",
                "org.apache.hadoop:hadoop-aws:3.3.1,io.delta:delta-core_2.12:2.4.0")
        .config("spark.hadoop.fs.s3a.endpoint",
                "https://s3.us-west-1.idrivee2.com") # need to be updated  
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider",
                "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "true")
        .getOrCreate()