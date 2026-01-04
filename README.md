# 🚗 Vehicle Availability ETL

## Overview

The **Vehicle Availability ETL** project is a production-ready data pipeline that extracts vehicle availability and maintenance data from the **TruLinks API**, transforms complex nested API responses into analytics-ready tabular datasets, and uploads **timestamped, Redshift-compatible CSV files** to **Amazon S3**.

The pipeline is designed with **scalability, reliability, and cloud deployment** in mind and can run both **locally** and as an **AWS Lambda function**.

---

## Key Features

- ✅ Redshift-safe CSV formatting
- ✅ Nested JSON flattening (maintenance & VOR data)
- ✅ AWS Lambda compatible
- ✅ Environment-based secrets management
- ✅ Modular ETL architecture
- ✅ Timestamped S3 archiving
- ✅ Easy to extend for additional API endpoints

---

## What the Pipeline Does

1. Connects securely to the TruLinks API
2. Fetches vehicle availability data
3. Flattens nested structures such as:
   - Vehicle metadata
   - Vehicle Off Road (VOR) details
   - Current maintenance events
   - Upcoming maintenance events
4. Cleans and normalizes data for Amazon Redshift ingestion
5. Generates CSV files with execution timestamps
6. Uploads processed data to Amazon S3

Each run produces **one row per vehicle**, optimized for analytics and reporting.

---

## Project Structure

vehicle-availability-etl/
│
├── app/
│ ├── init.py
│ ├── config.py # Environment configuration
│ ├── api_handler.py # TruLinks API requests
│ ├── processor.py # Data transformation logic
│ ├── utils.py # Redshift-safe cleaning helpers
│ ├── s3_uploader.py # S3 upload and archiving
│ └── lambda_handler.py # AWS Lambda entry point
│
├── run_local.py # Local execution script
├── requirements.txt # Python dependencies
├── .env.example # Environment variable template
└── README.md




---

## Loading Data into Amazon Redshift

After the vehicle availability CSV is generated and uploaded to Amazon S3, the pipeline can automatically load the data into **Amazon Redshift** using the `COPY` command.

This approach is:
- Fast (S3 → Redshift native)
- Scalable
- Production-standard

---

## Prerequisites for Redshift Load

Ensure the following are in place:

- An existing Redshift cluster
- A target table created in Redshift
- An IAM Role attached to Redshift with S3 read access
- The CSV file already uploaded to S3 by this ETL

<img width="1402" height="545" alt="image" src="https://github.com/user-attachments/assets/dde9c3a4-66c6-4199-a65f-aaf37bbe06f7" />

