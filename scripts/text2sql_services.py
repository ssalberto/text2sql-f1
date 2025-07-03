import os
import time
import requests
from prompts import prompt_template, evidence, db_schema
from model import Text2SQLGenerator

class Text2SQLService:
    def __init__(self):
        self.text2sql_generator = Text2SQLGenerator()

    def generate_sql(self, question) -> str:

        prompt = prompt_template.format(evidence=evidence, db_schema=db_schema, question=question)

        sql = self.text2sql_generator.generate_response(prompt)
        return sql
    
# if __name__ == "__main__":
#     text2sql_service = Text2SQLService()

