import pandas as pd

def clean_dataframe_for_redshift(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace("/", "_")
    )

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("").astype(str)
        else:
            df[col] = df[col].fillna(0)

    return df
