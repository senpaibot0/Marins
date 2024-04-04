from dbCon import getConnexion

class AdoptionDAO:
    @staticmethod
    def create_adoption(id_animal: int, id_particulier: int, date_adoption: str, interet: str):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO Adoption (IDAnimal, IDParticulier, DateAdoption, Interet) 
            VALUES (?, ?, ?, ?)
            """, (id_animal, id_particulier, date_adoption, interet))
            cnxn.commit()
        return "Adoption record created successfully."

    @staticmethod
    def get_adoption_by_id(adoption_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Adoption WHERE IDAdoption = ?", (adoption_id,))
            result = cursor.fetchone()
            if result:
                return {
                    "IDAdoption": result[0], 
                    "IDAnimal": result[1], 
                    "IDParticulier": result[2], 
                    "DateAdoption": result[3], 
                    "Interet": result[4]
                }
            else:
                return None

    @staticmethod
    def get_all_adoptions():
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Adoption")
            adoptions = []
            for row in cursor.fetchall():
                adoptions.append({
                    "IDAdoption": row[0], 
                    "IDAnimal": row[1], 
                    "IDParticulier": row[2], 
                    "DateAdoption": row[3], 
                    "Interet": row[4]
                })
            return adoptions

    @staticmethod
    def delete_adoption(adoption_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("DELETE FROM Adoption WHERE IDAdoption = ?", (adoption_id,))
            cnxn.commit()
        return "Adoption record deleted successfully."
