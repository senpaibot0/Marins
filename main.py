# from datetime import datetime, timedelta
# import random
# import pyodbc

# from dbCon import getConnexion
from fastapi import FastAPI, HTTPException, Path, Form
from pydantic import BaseModel
from AnimalDao import AnimalDAO
from ParticulierDAO import ParticulierDAO
from AdoptionDAO import AdoptionDAO
from AnimalLocationDAO import AnimalLocationDAO
from ClimatDAO import ClimatDAO
from LocationsDAO import LocationsDAO


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


class Animal(BaseModel):
    espesce: str
    nom: str
    statutAdoption: int



class CoordinateData(BaseModel):
    nombre_de_coordonnees: int

##################################    
# CRUD Operations pour les Animaux
##################################
@app.post("/animal/")
async def add_animal(espece: str = Form(...), nom: str = Form(...), statutAdoption: bool = Form(...)):
    return AnimalDAO.create_animal(espece, nom, statutAdoption)

@app.get("/animal/{animal_id}")
async def get_animal(animal_id: int):
    animal = AnimalDAO.get_animal_by_id(animal_id)
    if animal:
        return animal
    raise HTTPException(status_code=404, detail="Animal not found")

@app.get("/animals/")
async def get_all_animals():
    return AnimalDAO.get_All_animals()

@app.delete("/animal/{animal_id}")
async def delete_animal(animal_id: int):
    return AnimalDAO.delete_animal(animal_id)


##################################  
# CRUD Operations for Particulier
##################################  

@app.post("/particulier/")
async def create_particulier(type_particulier: str = Form(...), nom: str = Form(...), contact: str = Form(...)):
    return ParticulierDAO.create_particulier(type_particulier, nom, contact)

@app.get("/particulier/{particulier_id}")
async def get_particulier(particulier_id: int):
    return ParticulierDAO.get_particulier_by_id(particulier_id)

@app.get("/particuliers/")
async def get_all_particuliers():
    return ParticulierDAO.get_all_particuliers()

##################################  
# CRUD Operations for Adoption
##################################  

@app.post("/adoption/")
async def add_adoption(id_animal: int = Form(...), id_particulier: int = Form(...), date_adoption: str = Form(...), interet: str = Form(...)):
    return AdoptionDAO.create_adoption(id_animal, id_particulier, date_adoption, interet)

@app.get("/adoption/{adoption_id}")
async def get_adoption(adoption_id: int):
    return AdoptionDAO.get_adoption_by_id(adoption_id)

@app.get("/adoptions/")
async def get_all_adoptions():
    return AdoptionDAO.get_all_adoptions()

##################################  
# CRUD Operations for AnimalLocation
##################################  

@app.post("/animal_location/")
async def add_animal_location(id_animal: int, id_location: int, date_enregistrement: str, temps_enregistrement: str, latitude: float, longitude: float):
    # Assuming date and time conversion is handled appropriately
    return AnimalLocationDAO.create_animal_location(id_animal, id_location, date_enregistrement, temps_enregistrement, latitude, longitude)

@app.get("/animal_locations/")
async def get_all_locations():
    return AnimalLocationDAO.get_all_animal_locations()

@app.delete("/animal_locations/flush/")
async def flush_locations():
    return AnimalLocationDAO.flush_locations()

@app.patch("/generate-data/}")
async def generate_data_api(nombre : int):
    AnimalLocationDAO.generate_data(nombre)
    return {"message": "Data generated successfully."}

##################################  
# CRUD Operations for Climat
##################################  

@app.post("/climat/")
async def create_climat(temperature: float = Form(...), vent: float = Form(...), courant: float = Form(...)):
    return ClimatDAO.create_climat(temperature, vent, courant)

@app.get("/climat/{climat_id}")
async def get_climat(climat_id: int):
    return ClimatDAO.get_climat_by_id(climat_id)

@app.get("/climats/")
async def get_all_climats():
    return ClimatDAO.get_all_climats()

##################################  
# CRUD Operations pour Locations
##################################  

@app.post("/location/")
async def create_location(id_climat: int = Form(...), habitat: str = Form(...), latitude: float = Form(...), longitude: float = Form(...)):
    return LocationsDAO.create_location(id_climat, habitat, latitude, longitude)

@app.get("/location/{location_id}")
async def get_location(location_id: int):
    return LocationsDAO.get_location_by_id(location_id)

@app.get("/locations/")
async def get_all_locations():
    return LocationsDAO.get_all_locations()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
