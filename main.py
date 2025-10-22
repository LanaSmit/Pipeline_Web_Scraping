from extract import extract_data
from transform import transform_data
from load import load_data
import pandas as pd


def main():
    # Extract data
    extract_data()

    # Load data into a Polars DataFrame
    df = pd.read_csv("netflix_top10.csv")

    # Transform data
    df = transform_data(df)

    # Load data into PostgreSQL
    conn = "postgresql://postgres:lana@localhost:5432/postgres"
    load_data(df,"netflix_top10_movies", conn)   

    print("ETL process completed successfully.")
#"postgresql://Lana:lana@localhost:5432/dbPipeine_2"

if __name__ == "__main__":
    main()