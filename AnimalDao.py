from dbCon import getConnexion

class AnimalDAO:
    @staticmethod
    def create_animal(espece: str, nom: str, statutAdoption: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("INSERT INTO Animal (Espece, Nom, StatutAdoption) VALUES (?, ?, ?)", (espece, nom, statutAdoption))
            cnxn.commit()
        return f"Animal {nom} created successfully."

    @staticmethod
    def get_animal_by_id(animal_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Animal WHERE IDAnimal = ?", (animal_id,))
            result = cursor.fetchone()
            if result:
                return {"IDAnimal": result[0], "Espece": result[1], "Nom": result[2], "StatutAdoption": result[3]}
            else:
                return None
            
    @staticmethod
    def get_All_animals():
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Animal")
            result = cursor.fetchall()
            if result:
                return {"IDAnimal": result[0], "Espece": result[1], "Nom": result[2], "StatutAdoption": result[3]}
            else:
                return None

    @staticmethod
    def delete_animal(animal_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("DELETE FROM Animal WHERE IDAnimal = ?", (animal_id,))
            cnxn.commit()
        return "Animal deleted successfully."
    
    
