import os
import pandas as pd

from app.services.data_processor import (
    standardize_dataframe
)

def load_standardized_df(upload, mapping):

    os.makedirs(
        "processed",
        exist_ok=True
    )

    processed_path = (
        f"processed/{upload.id}.parquet"
    )

    # Already processed -> load directly
    if os.path.exists(processed_path):
        return pd.read_parquet(
            processed_path
        )

    # First time -> read original dataset
    if upload.file_path.endswith(".csv"):

        df = pd.read_csv(
            upload.file_path
        )

    else:

        df = pd.read_excel(
            upload.file_path
        )

    df = standardize_dataframe(
        df,
        mapping
    )

    # Save standardized dataframe
    df.to_parquet(
        processed_path,
        index=False
    )

    return df