# S3 Bucket Integration with Apache Spark (IDrive e2)

# Note: Sensitive credentials are not included in this repository and should be configured locally on the server.

## Overview

This project connects Apache Spark with IDrive e2 (S3-compatible object storage) to enable scalable data access and processing using the `s3a://` protocol.

---

## Data Loading Architecture

```text
You run training.py 
↓ 
training.py calls load_data() 
↓ 
data_loader.py calls spark.read.format("delta").load(...) 
↓ 
Spark reads Delta Lake data from s3a://bucket/path 
↓ 
Delta Lake layer (data format on S3) 
↓ 
❗ Authentication required here 
↓ 
Spark looks for system credentials (~/.aws/credentials) 
↓ 
Uses Access Key / Secret Key to authenticate with IDrive e2 
↓ 
IDrive e2 returns data 
↓ 
Spark loads data into DataFrame (df) 
↓ 
df is passed to model / training
```

---

## Setup

### 1. Configure Credentials (Server)

Create AWS-style credentials on the server:

```bash
mkdir -p ~/.aws
nano ~/.aws/credentials
```

Add:

```text
[default]
aws_access_key_id=YOUR_ACCESS_KEY
aws_secret_access_key=YOUR_SECRET_KEY
```

Set permissions:

```bash
chmod 600 ~/.aws/credentials
```

---

### 2. Configure Spark Session

```python
from pyspark.sql import SparkSession

def get_spark():
    return (
        SparkSession.builder
        .appName("delta-test")
        .config("spark.jars.packages",
                "org.apache.hadoop:hadoop-aws:3.3.1,io.delta:delta-core_2.12:2.4.0")
        .config("spark.hadoop.fs.s3a.endpoint",
                "https://s3.us-midwest-1.idrivee2.com")
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider",
                "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
        .getOrCreate()
    )
```

---

### 3. Load Data from S3

```python
from spark_session import get_spark

spark = get_spark()

DATA_PATH = "s3a://your-bucket/your_name/data"

def load_data():
    return spark.read.format("delta").load(DATA_PATH)
```

---

### 4. Run Training

```python
from data_loader import load_data
from model import train

df = load_data()
train(df)
```

---

## Security Design

* Credentials are **not hardcoded** in source code
* Stored securely in `~/.aws/credentials`
* Access is managed via system-level configuration
* Avoids exposing secrets in GitHub repositories

---

## Notes

* Ensure the correct **endpoint** is used (based on region)
* Bucket paths follow:

```text
s3a://bucket-name/folder/path
```

* Delta Lake support is enabled via Spark packages

---

## Summary

This setup enables:

* Secure access to cloud storage
* Clean separation between configuration and code
* Scalable data processing using Spark

---
