from dbCon import getConnexion
from datetime import datetime
import random
import math
from datetime import datetime, timedelta
from dbCon import getConnexion

def generate_longitude(index):
    return math.cos(index / 10) * 180

def generate_latitude(index):
    return math.sin(index / 10) * 90

def generate_random_time(debut: datetime, fin  :datetime ):
    start_time = datetime(debut)  # Début de l'année 2023
    end_time = datetime(fin)  # Fin de l'année 2024
    # Calculer la différence totale de secondes entre start_time et end_time
    difference = end_time - start_time
    difference_in_seconds = difference.total_seconds()
    # Générer un nombre aléatoire de secondes à ajouter à start_time
    random_seconds = random.randint(0, int(difference_in_seconds))
    # Calculer le nouveau timestamp aléatoire
    random_timestamp = start_time + timedelta(seconds=random_seconds)
    return random_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')

class AnimalLocationDAO:
    @staticmethod
    def create_animal_location(id_animal: int, id_location: int, date_enregistrement: datetime, temps_enregistrement: datetime, latitude: float, longitude: float):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO AnimalLocation (IDAnimal, IDLocation, DateEnregistrement, TempsEnregistrement, Latitude, Longitude) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, (id_animal, id_location, date_enregistrement, temps_enregistrement, latitude, longitude))
            cnxn.commit()
        return "Animal location record created successfully."

    @staticmethod
    def get_animal_location_by_id(id_animal: int, id_location: int, date_enregistrement: datetime, temps_enregistrement: datetime):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("""
            SELECT * FROM AnimalLocation 
            WHERE IDAnimal = ? AND IDLocation = ? AND DateEnregistrement = ? AND TempsEnregistrement = ?
            """, (id_animal, id_location, date_enregistrement, temps_enregistrement))
            result = cursor.fetchone()
            if result:
                return {
                    "IDAnimal": result[0], 
                    "IDLocation": result[1], 
                    "DateEnregistrement": result[2], 
                    "TempsEnregistrement": result[3],
                    "Latitude": result[4], 
                    "Longitude": result[5]
                }
            else:
                return None

    @staticmethod
    def get_all_animal_locations():
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM AnimalLocation")
            locations = []
            for row in cursor.fetchall():
                locations.append({
                    "IDAnimal": row[0], 
                    "IDLocation": row[1], 
                    "DateEnregistrement": row[2], 
                    "TempsEnregistrement": row[3],
                    "Latitude": row[4], 
                    "Longitude": row[5]
                })
            return locations

    @staticmethod
    def delete_animal_location(id_animal: int, id_location: int, date_enregistrement: datetime, temps_enregistrement: datetime):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("""
            DELETE FROM AnimalLocation 
            WHERE IDAnimal = ? AND IDLocation = ? AND DateEnregistrement = ? AND TempsEnregistrement = ?
            """, (id_animal, id_location, date_enregistrement, temps_enregistrement))
            cnxn.commit()
        return "Animal location record deleted successfully."

    @staticmethod
    def flush_locations():
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE AnimalLocation")
            cnxn.commit()
        return "AnimalLocation table flushed."

    

    @staticmethod
    def generate_data(nombre_de_coordonnees:int):
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



