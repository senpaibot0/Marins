import math
import random
import pyodbc
from datetime import datetime, timedelta
from dbCon import getConnexion
from fastapi import FastAPI, HTTPException, Path, Form
from pydantic import BaseModel


description = """
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀

## Users

You will be able to:

* **Create des Animaux Marins** (_implemented_). 
* **Lire les donnes sur leurs loactiosations** (_implemented_). 
* **Fluch la table AnimalLoaction** (implemented). 
* **Delete des Animaux selon leur ID** (_not implemented_). 
* **Ajouter Adoptiion par un particulier** (_not implemented_). 
* **Reajuster le code sql + requetes(10)** (_not implemented_). 
* **generer Animaux, Generer Les prorpio, Generer les Sante de lamimal, cree adoption, cree climat, modification **  
"""

app = FastAPI( title="Generate Data and Send to Ms SQL",
    description= description,
    version="0.0.1",)

def generate_longitude(index):
    return math.cos(index / 10) * 180

def generate_latitude(index):
    return math.sin(index / 10) * 90

def generate_random_time():
    start_time = datetime(2023, 1, 1, 0, 0, 0)  # Début de l'année 2023
    end_time = datetime(2024, 12, 31, 23, 59, 59)  # Fin de l'année 2024
    # Calculer la différence totale de secondes entre start_time et end_time
    difference = end_time - start_time
    difference_in_seconds = difference.total_seconds()
    # Générer un nombre aléatoire de secondes à ajouter à start_time
    random_seconds = random.randint(0, int(difference_in_seconds))
    # Calculer le nouveau timestamp aléatoire
    random_timestamp = start_time + timedelta(seconds=random_seconds)
    return random_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')



# class Animal(BaseModel):
#     espesce: str
#     nom: str
#     statutAdoption: int



@app.patch('/CreationClimat/') #climat
async def create_animal(espece: str = Form(...), nom: str = Form(...), statutAdoption: int = Form(...)):
    try:
        cnxn = getConnexion()
        cursor = cnxn.cursor()

        insert_query = ''' INSERT INTO Climat (Espece, Nom, statutAdoption) 
            VALUES (?, ?, ?)
            '''
        cursor.execute(insert_query, (espece, nom, statutAdoption))
        cnxn.commit()
        message = f"L'animal {nom} a bien été créé !"
    except Exception as e:
        cnxn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        cnxn.close()
    return {"message": message} 

@app.patch('/CreationParticulier/')# proprio
async def create_Particulier(Type: str = Form(...), nom: str = Form(...), Contact: str = Form(...)):
    try:
        cnxn = getConnexion()
        cursor = cnxn.cursor()

        insert_query = ''' INSERT INTO Particulier (Type, nom, Contact) 
            VALUES (?, ?, ?)
            '''
        cursor.execute(insert_query, (Type, nom, Contact))
        cnxn.commit()
        
        message = f"Le Particulier {nom} a bien été créé !"
    except Exception as e:
        cnxn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        cnxn.close()
    return {"message": message}

@app.patch('/CreationAnimal/')
async def create_animal(espece: str = Form(...), nom: str = Form(...), statutAdoption: int = Form(...)):
    try:
        cnxn = getConnexion()
        cursor = cnxn.cursor()

        insert_query = ''' INSERT INTO Animal (Espece, Nom, statutAdoption) 
            VALUES (?, ?, ?)
            '''
        cursor.execute(insert_query, (espece, nom, statutAdoption))
        cnxn.commit()
        message = f"L'animal {nom} a bien été créé !"
    except Exception as e:
        cnxn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        cnxn.close()
    return {"message": message}





# class CoordinateData(BaseModel):
#     nombre_de_coordonnees: int

@app.post("/generate-data/}")
async def generate_data_api(nombre : int):
    generate_data(nombre)
    return {"message": "Data generated successfully."}

def generate_data(nombre_de_coordonnees):
    try:
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

    except Exception as e:
        cnxn.rollback()
        raise e
    finally:
        cursor.close()
        cnxn.close()

    return {"message": f"La génération des {nombre_de_coordonnees} données a bien été faite !"}




@app.get("/GetAnimalLocations/")
async def Get_Animal_Locations():
    try:
        cnxn = getConnexion()
        cursor = cnxn.cursor()

        animalLocs = []
        cursor.execute("SELECT IDAnimal, IDLocation, DateEnregistrement, TempsEnregistrement, latitude, longitude  FROM AnimalLocation")
        rows = cursor.fetchall()
        for row in rows:
            animalLocs.append(f'IDAnimal: {row[0]}, IDLocation: {row[1]}, DateEnregistrement: {row[2]}, TempsEnregistrement: {row[3]}, latitude: {row[4]}, longitude: {row[5]}' )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        cnxn.close()
    return animalLocs

@app.delete("/FlushAnimalLocations/")
async def Flush_Animal_Locs():
    try:
        cnxn = getConnexion()
        cursor = cnxn.cursor()
        
        cursor.execute("DROP TABLE IF EXISTS AnimalLocation")
        cnxn.commit()
        message = "Tous a bien été supprimé de Animal Location."
    except Exception as e:
        cnxn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        cnxn.close()
    return {'message': message}


@app.delete("/FlushAnimal/{Animal_id}") # ici il manque de faire de quoi avec la forigh key de Sante de lanimal
async def delete_animal(Animal_id: int):
    try:
        cnxn = getConnexion()
        cursor = cnxn.cursor()

        delete_query = "DELETE FROM Animal WHERE IDAnimal = ?"
        cursor.execute(delete_query, (Animal_id,))
        cnxn.commit()

        if cursor.rowcount == 0:
            return {'message': "Aucun Animal touver avec cet ID"}
        else:
            return {'message': "Animal Bien Supprimer !"}

    except Exception as e:
        cnxn.rollback()  
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        cnxn.close()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
