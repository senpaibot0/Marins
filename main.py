import math
import random
import pyodbc
from datetime import datetime, timedelta
from dbCon import getConnexion
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def generate_longitude(index):
    return math.cos(index / 10) * 180

def generate_latitude(index):
    return math.sin(index / 10) * 90

def generate_random_time():
    start_time = datetime(2024, 1, 1, 6, 0, 0)
    random_minutes = random.randint(0, 14 * 60)
    return (start_time + timedelta(minutes=random_minutes)).strftime('%H:%M:%S')


@app.get("/GetAnimalLocations/")
async def GetAnimalLocations():
    cnxn = getConnexion()
    cursor = cnxn.cursor()

    id_animal = []
    cursor.execute("SELECT IDAnimal, IDLocation, DateEnregistrement, TempsEnregistrement, latitude, longitude  FROM AnimalLocation")
    rows = cursor.fetchall()
    for row in rows:
        id_animal.append(f'IDAnimal: {row[0]}, IDLocation: {row[1]}, DateEnregistrement: {row[2]}, TempsEnregistrement: {row[3]}, latitude: {row[4]}, longitude: {row[5]}' )

    cursor.close()
    cnxn.close()
    return id_animal

class CoordinateData(BaseModel):
    nombre_de_coordonnees: int

@app.post("/generate-data/")
async def generate_data_api(data: CoordinateData):
    generate_data(data.nombre_de_coordonnees)
    return {"message": "Data generated successfully."}

def generate_data(nombre_de_coordonnees):
    cnxn = getConnexion()
    cursor = cnxn.cursor()


    id_animal = []
    cursor.execute("SELECT IDAnimal FROM Animal")
    rows = cursor.fetchall()
    for row in rows:
        id_animal.append(row[0])

    id_location = []
    cursor.execute("SELECT IDLocation FROM Locations")
    rows = cursor.fetchall()
    for row in rows:
        id_location.append(row[0])


    for i in range(nombre_de_coordonnees):
        random_animal_id = random.choice(id_animal)
        random_location_id = random.choice(id_location)
        random_date = datetime.today().date()
        random_time = generate_random_time()
        random_latitude = generate_latitude(i)
        random_longitude = generate_longitude(i)

        insert_query = ''' INSERT INTO AnimalLocation (IDAnimal, IDLocation, DateEnregistrement, TempsEnregistrement, latitude, longitude) 
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(insert_query, (random_animal_id, random_location_id, random_date, random_time, random_latitude, random_longitude))
        cnxn.commit()


    cursor.close()
    cnxn.close()


#def createAnimal():




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)