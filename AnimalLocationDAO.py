from dbCon import getConnexion
from datetime import datetime

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

