import os
from typing import List, Dict, Any
import pandas as pd
from sqlalchemy import create_engine

class DBService:
    def __init__(self):
        self.conn_str = f"f1_database.db"
        self.engine = None

    def get_engine(self):
        if not self.engine:
            db_path = os.path.join(os.getcwd(),  self.conn_str)
            self.engine = create_engine(f"sqlite:///{db_path}")
        return self.engine


    def execute_query(self, sql_query: str) -> List[Dict[str, Any]]:
        try:
            engine = self.get_engine()
            df = pd.read_sql(sql_query, engine)
            return df.to_dict(orient="records")
        
        except Exception as e:
            print(f"Error executing query: {e}")
            return []


if __name__ == "__main__":
    pass