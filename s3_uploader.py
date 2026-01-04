import boto3
import tempfile
import pandas as pd
from datetime import datetime
from .utils import clean_dataframe_for_redshift

def upload_to_s3(file_path, bucket, endpoint, api_groups, group):
    s3 = boto3.client("s3")
    endpoint_name = endpoint.split("/")[-1]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    key = f"RHA_archive/{api_groups[group]}{endpoint_name}_{timestamp}.csv"

    df = pd.read_csv(file_path)
    df = clean_dataframe_for_redshift(df)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        df.to_csv(tmp.name, index=False, encoding="utf-8", quoting=1)
        s3.upload_file(tmp.name, bucket, key)

    return key
