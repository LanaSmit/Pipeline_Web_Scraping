"""import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize the column names to lowercase
    df = df.rename({col: col.lower() for col in df.columns})

    # Remove numbers from the "title" column
    df = df["title"].str.replace(r"\d+", "", regex=True)

    # Replace spaces with underscores in the "title" column
    df =  df["title"].str.replace(" ", "_")
    

    return df
"""
import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize column names to lowercase and replace spaces with underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    print("Cleaned columns:", df.columns.tolist())

    # Remove numbers from the "title" column
    df["title"] = df["title"].str.replace(r"\d+", "", regex=True)

    # Replace spaces with underscores in the "title" column
    df["title"] = df["title"].str.replace(" ", "_")

    return df
