import json

from db_services import DBService
from text2sql_services import Text2SQLService
from datetime import datetime, timedelta
import time
import re


class Pipeline:
    def __init__(self):
        self.text2sql_service = Text2SQLService()
        self.db_service = DBService()

    def generate_sql(self, question):
        sql = self.text2sql_service.generate_sql(question)
        # sql = sql.encode('utf-8').decode('unicode_escape')
        return sql

    def execute_query(self, sql_query):
        answer = self.db_service.execute_query(sql_query)
        print("Answer:")
        print(answer)
        return answer

    def invoke(self, question):

            sql = self.generate_sql(question)

            try:
                answer = self.execute_query(sql)
            except Exception as e:
                answer = "Error al procesar la consulta"

            return sql, answer

if __name__ == "__main__":
    pipeline = Pipeline()
    
    while True:
        # Recibir un input del usuario
        question = input("Introduce tu pregunta (o escribe 'salir' para terminar): ")
        if question.lower() == 'salir' or question.lower() == 'exit':
            print("Saliendo del programa...")
            break
        print("Question:")
        print(question)  # Output the question
        sql, answer = pipeline.invoke(question)
        print("Generated SQL:")
        print(sql)  # Output the generated SQL query
        print("Answer:")
        print(answer)