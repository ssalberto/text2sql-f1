import sqlite3
import ergast_py
from tqdm import tqdm
import pandas as pd
import time

# Create a connection to the SQLite database
conn = sqlite3.connect('f1_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Piloto (
    id TEXT PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    fecha_nacimiento TEXT,
    nacionalidad TEXT
);

''')

cursor.execute('''
CREATE TABLE Escuderia (
    id TEXT PRIMARY KEY,
    nombre TEXT,
    nacionalidad TEXT
);
''')

cursor.execute('''
CREATE TABLE PilotoEscuderia (
    piloto_id TEXT,
    escuderia_id TEXT,
    PRIMARY KEY (piloto_id, escuderia_id),
    FOREIGN KEY (piloto_id) REFERENCES Piloto(id),
    FOREIGN KEY (escuderia_id) REFERENCES Escuderia(id)
);
''')

cursor.execute('''
CREATE TABLE GP (
    id TEXT PRIMARY KEY,
    año INTEGER,
    dia INTEGER,
    mes INTEGER,
    hora TEXT,
    circuito TEXT,
    granpremio TEXT
);
''')


cursor.execute('''
CREATE TABLE ResultadoGP (
gp_id TEXT,
piloto_id TEXT,
escuderia_id TEXT,
posicion INTEGER,
parrilla INTEGER,
tiempo TEXT,
puntos FLOAT,
PRIMARY KEY (gp_id, piloto_id),
FOREIGN KEY (gp_id) REFERENCES GP(id),
FOREIGN KEY (piloto_id) REFERENCES Piloto(id)
);
''')

cursor.execute('''
CREATE TABLE Circuito (
    id TEXT PRIMARY KEY,
    nombre TEXT,
    ciudad TEXT,
    pais TEXT
);
''')

drivers = {}
teams = {}
races = {}

# Loop through the years from 1950 to 2024
for year in tqdm(range(1950, 2022)):
    
    for race in range(1, 25):
        try:

            e = ergast_py.Ergast()
            session = e.season(year).round(race).get_results()[0]
            session_id = f"{year}_{session.race_name}"
            
        except Exception as e:
            print(f"Skipping year {year}, race {race} due to error: {e}")
            continue


        cursor.execute('''
            INSERT OR IGNORE INTO GP (id, año, mes, dia, hora, circuito, granpremio)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                session_id,
                session.date.year,
                session.date.month,
                session.date.day,
                session.date.hour,
                session.circuit.circuit_id,
                session.race_name
        ))

        # Store circuit data
        cursor.execute('''
            INSERT OR IGNORE INTO Circuito (id, nombre, ciudad, pais)
            VALUES (?, ?, ?, ?)
            ''', (
            session.circuit.circuit_id,
            session.circuit.circuit_name,
            session.circuit.location.locality,
            session.circuit.location.country
        ))

        for result in session.results:

            cursor.execute('''
                INSERT OR IGNORE INTO ResultadoGP (gp_id, piloto_id, escuderia_id, posicion, parrilla, tiempo, puntos)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                session_id,
                result.driver.driver_id,
                result.constructor.constructor_id,
                result.position,
                result.grid,
                result.time.time,
                result.points
            ))

            # Store driver data

            if result.driver.driver_id not in drivers:
                drivers[result.driver.driver_id] = {
                    'id': result.driver.driver_id,
                    'nombre': result.driver.given_name,
                    'apellido': result.driver.family_name,
                    'fecha_nacimiento': result.driver.date_of_birth,
                    'nacionalidad': result.driver.nationality
                }

            # Store team data

            if result.constructor.constructor_id not in teams:
                teams[result.constructor.constructor_id] = {
                    'id': result.constructor.constructor_id,
                    'nombre': result.constructor.name,
                    'nacionalidad': result.constructor.nationality
                }

            # Add driver-team relationship

            cursor.execute('''
                INSERT OR IGNORE INTO PilotoEscuderia (piloto_id, escuderia_id)
                VALUES (?, ?)
                ''', (
                result.driver.driver_id,
                result.constructor.constructor_id
            ))
        
    # time.sleep(60)
        

# Store driver and team data in the database

for driver in drivers.values():
    
    cursor.execute('''
        INSERT OR IGNORE INTO Piloto (id, nombre, apellido, fecha_nacimiento, nacionalidad)
        VALUES (?, ?, ?, ?, ?)
        ''', (
        driver['id'],
        driver['nombre'],
        driver['apellido'],
        driver['fecha_nacimiento'],
        driver['nacionalidad']
    ))

for team in teams.values():
    
    cursor.execute('''
        INSERT OR IGNORE INTO Escuderia (id, nombre, nacionalidad)
        VALUES (?, ?, ?)
        ''', (
        team['id'],
        team['nombre'],
        team['nacionalidad']
    ))

# Create indexes for faster queries
cursor.execute('''
    CREATE INDEX IF NOT EXISTS idx_gp_id ON ResultadoGP (gp_id);
''')
cursor.execute('''
    CREATE INDEX IF NOT EXISTS idx_piloto_id ON ResultadoGP (piloto_id);
''')

# Commit changes and close the connection
conn.commit()
conn.close()