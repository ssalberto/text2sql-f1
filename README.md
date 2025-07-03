# Conversational assistant for databases
This is the f1 version of the text2sql project I developed. This assistant allows people to interact in natural language with many kinds of databases. In this specific version, I created a F1 database containing information about drivers, races, tracks and results. By providing the schema, the user question and some information about the context and the task, the system is capable of producing an SQL query that can be executed to provide real information contained in the DB, so we can avoid hallucinations.

The system can run locally, no API uses. This is in order to keep confiential information safe, it is not sent to any external server. I use the Text2SQL model XiYanSQL-QwenCoder (7B param). 

![1](https://github.com/user-attachments/assets/4b3e7560-b7f5-4fea-8dcb-e7c2c0689d00)  
Diagram explaining the main functionality of the system.
