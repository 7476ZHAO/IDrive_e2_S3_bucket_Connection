# data_loader.py

from spark_session import get_spark
from config import DATA_PATH

spark = get_spark()

# substitute with real path
# DATA_PATH = "s3a://your-bucket/your_name/data"

def load_data():
    df = spark.read.format("delta").load(DATA_PATH)
    return df
