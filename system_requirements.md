# System Requirements

This project requires the following system-level dependencies to run successfully.

---

## 1. Java (Required for Spark)

Apache Spark requires Java to run.

Install OpenJDK 17:

```bash
sudo apt update
sudo apt install openjdk-17-jdk
```

Verify installation:

```bash
java -version
```

---

## 2. Python

Python 3.8 or higher is recommended.

Check version:

```bash
python3 --version
```

---

## 3. Python Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

---

## 4. AWS Credentials (Required for S3 Access)

Configure credentials on the server:

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

## 5. Notes

* Do NOT include credentials in this repository
* Ensure the correct S3 endpoint is configured in `spark_session.py`
* Spark dependencies (Hadoop AWS, Delta Lake) are configured in code via `spark.jars.packages`

---

## Summary

This project separates:

* System dependencies (Java)
* Python dependencies (requirements.txt)
* Credentials (local configuration)

This design improves security and maintainability.
