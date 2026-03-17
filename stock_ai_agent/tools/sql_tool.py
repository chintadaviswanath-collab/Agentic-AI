import sqlite3
import pandas as pd

class SQLTool:
    def __init__(self, db_path="data/database.db"):
        self.conn = sqlite3.connect(db_path)

    def save_dataframe(self, df, table_name):
        df.to_sql(table_name, self.conn, if_exists="replace", index=True)

    def load_dataframe(self, table_name):
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", self.conn, index_col="index")
            return df
        except:
            return None

    def close(self):
        self.conn.close()
