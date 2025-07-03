prompt_template = """
你是一名SQLite专家，现在需要阅读并理解下面的【数据库schema】描述，以及可能用到的【参考信息】，并运用SQLite知识生成sql语句回答【用户问题】。
【用户问题】
{question}

【数据库schema】
{db_schema}

【参考信息】
{evidence}

【用户问题】
{question}

```sql"""

db_schema = """
【DB_ID】 f1_database.db
【Schema】
# Table: main.Circuito
[
(id:TEXT, Primary Key, Examples: [adelaide, ain-diab, aintree]),
(nombre:TEXT, Examples: [Silverstone Circuit]),
(ciudad:TEXT, Examples: [Silverstone, Monte-Carlo, Indianapolis]),
(pais:TEXT, Examples: [UK, Monaco, USA])
]

# Table: main.Escuderia
[
(id:TEXT, Primary Key, Examples: [adams, afm, alfa]),
(nombre:TEXT, Examples: [Alfa Romeo, Talbot-Lago, ERA]),
(nacionalidad:TEXT, Examples: [Swiss, French, British])
]

# Table: main.GP
[
(id:TEXT, Primary Key, Examples: [1950_Belgian Grand Prix]),
(año:INTEGER, Examples: [1950, 1951, 1952]),
(dia:INTEGER, Examples: [13, 21, 30]),
(mes:INTEGER, Examples: [5, 6, 7]),
(hora:TEXT, Examples: [0, 14, 15]),
(circuito:TEXT, Examples: [silverstone, monaco, indianapolis]),
(granpremio:TEXT, Examples: [British Grand Prix, Monaco Grand Prix, Indianapolis 500])
]

# Table: main.Piloto
[
(id:TEXT, Primary Key, Examples: [Cannoc, abate, abecassis]),
(nombre:TEXT, Examples: [Nino, Luigi, Reg]),
(apellido:TEXT, Examples: [Farina, Fagioli, Parnell]),
(fecha_nacimiento:TEXT, Examples: [1906-10-30, 1898-06-09, 1911-07-02]),
(nacionalidad:TEXT, Examples: [Italian, British, French])
]

# Table: main.PilotoEscuderia
[
(piloto_id:TEXT, Primary Key, Examples: [Cannoc, abate, abecassis]),
(escuderia_id:TEXT, Primary Key, Examples: [alfa, lago, era])
]

# Table: main.ResultadoGP
[
(gp_id:TEXT, Primary Key, Examples: [1950_Belgian Grand Prix]),
(piloto_id:TEXT, Primary Key, Examples: [Cannoc, abate, abecassis]),
(escuderia_id:TEXT, Examples: [alfa, lago, era]),
(posicion:INTEGER, Examples: [1, 2, 3]),
(parrilla:INTEGER, Examples: [1, 2, 4]),
(tiempo:TEXT, Examples: [2:13:23.600, +2.600, +52.000]),
(puntos:FLOAT, Examples: [9.0, 6.0, 4.0])
]

【Foreign keys】
"""

evidence = """
Ejemplos, explicaciones e información para que el modelo sepa lo que hacer
"""