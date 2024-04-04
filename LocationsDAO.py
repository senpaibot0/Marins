from dbCon import getConnexion

class LocationsDAO:
    @staticmethod
    def create_location(id_climat: int, habitat: str, latitude: float, longitude: float):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("INSERT INTO Locations (IDClimat, Habitat, Latitude, Longitude) VALUES (?, ?, ?, ?)", (id_climat, habitat, latitude, longitude))
            cnxn.commit()
        return "Location record created successfully."
    
    @staticmethod
    def get_location_by_id(location_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Locations WHERE IDLocation = ?", (location_id,))
            result = cursor.fetchone()
            if result:
                return {"IDLocation": result[0], "IDClimat": result[1], "Habitat": result[2], "Latitude": result[3], "Longitude": result[4]}
            else:
                return None

    @staticmethod
    def get_all_locations():
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Locations")
            locations = []
            for row in cursor.fetchall():
                locations.append({"IDLocation": row[0], "IDClimat": row[1], "Habitat": row[2], "Latitude": row[3], "Longitude": row[4]})
            return locations

    @staticmethod
    def update_location(location_id: int, id_climat: int = None, habitat: str = None, latitude: float = None, longitude: float = None):
        cnxn = getConnexion()
        updates = []
        params = []
        if id_climat is not None:
            updates.append("IDClimat = ?")
            params.append(id_climat)
        if habitat is not None:
            updates.append("Habitat = ?")
            params.append(habitat)
        if latitude is not None:
            updates.append("Latitude = ?")
            params.append(latitude)
        if longitude is not None:
            updates.append("Longitude = ?")
            params.append(longitude)
        params.append(location_id)
        update_statement = "UPDATE Locations SET " + ", ".join(updates) + " WHERE IDLocation = ?"
        
        with cnxn.cursor() as cursor:
            cursor.execute(update_statement, params)
            cnxn.commit()
        return "Location record updated successfully."

    @staticmethod
    def delete_location(location_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("DELETE FROM Locations WHERE IDLocation = ?", (location_id,))
            cnxn.commit()
        return "Location record deleted successfully."
