import psycopg2

def load_data(df, table_name, conn):
    # Connect to PostgreSQL database
    conn = psycopg2.connect(conn)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        Title TEXT,
        Views INTEGER,
        Runtime TEXT,
        Hours_Viewed INTEGER
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data into the table
    for _, row in df.iterrows():
        insert_query = f"""
        INSERT INTO {table_name} (Title, Views, Runtime, Hours_Viewed)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(insert_query, (
            row["title"],        # lowercase
            row["views"],
            row["runtime"],
            row["hours_viewed"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
