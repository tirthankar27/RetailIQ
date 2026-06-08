import pandas as pd

from app.services.data_processor import (
    standardize_dataframe
)

def load_standardized_df(
    upload,
    mapping
):

    if upload.file_path.endswith(".csv"):

        df = pd.read_csv(
            upload.file_path
        )

    else:

        df = pd.read_excel(
            upload.file_path
        )

    return standardize_dataframe(
        df,
        mapping
    )