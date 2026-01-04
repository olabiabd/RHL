import psycopg2
import os

def load_to_redshift(s3_path: str):
    """
    Load CSV data from S3 into Amazon Redshift using COPY
    """

    conn = psycopg2.connect(
        host=os.getenv("REDSHIFT_HOST"),
        port=os.getenv("REDSHIFT_PORT"),
        dbname=os.getenv("REDSHIFT_DB"),
        user=os.getenv("REDSHIFT_USER"),
        password=os.getenv("REDSHIFT_PASSWORD"),
    )

    schema = os.getenv("REDSHIFT_SCHEMA")
    table = os.getenv("REDSHIFT_TABLE")
    iam_role = os.getenv("REDSHIFT_IAM_ROLE")

    copy_sql = f"""
        COPY {schema}.{table}
        FROM '{s3_path}'
        IAM_ROLE '{iam_role}'
        FORMAT AS CSV
        IGNOREHEADER 1
        EMPTYASNULL
        BLANKSASNULL
        TIMEFORMAT 'auto'
        TRUNCATECOLUMNS;
    """

    with conn.cursor() as cur:
        cur.execute(copy_sql)
        conn.commit()

    conn.close()
