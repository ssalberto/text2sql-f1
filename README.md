# Conversational assistant for databases
This is the F1 version of the Text2SQL project I developed. This assistant allows people to interact in natural language with many kinds of databases. In this specific version, I created an F1 database containing information about drivers, races, tracks, and results. By providing the schema, the user question, and some information about the context and the task, the system is capable of producing an SQL query that can be executed to provide real information contained in the DB, so we can avoid hallucinations.

The system can run locally, no API usage. This is in order to keep confidential information safe—it is not sent to any external server. I use the Text2SQL model XiYanSQL-QwenCoder (7B param). 

![1](https://github.com/user-attachments/assets/4b3e7560-b7f5-4fea-8dcb-e7c2c0689d00)  
Diagram explaining the main functionality of the system.


## Example
![image](https://github.com/user-attachments/assets/938fb711-4c69-43ca-80f6-c334fde36ca0)
A human asking "¿Who won the Spanish GP in 2013?". The system will translate the question into a valid SQL query and will extract the real data directly from the database.


The web integration with streamlit looks as folows:
![image](https://github.com/user-attachments/assets/98e95ae9-ebab-4101-a19a-9d5872ccb1af)
