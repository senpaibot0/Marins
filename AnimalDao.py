from dbCon import getConnexion

class AnimalDAO:
    @staticmethod
    def create_animal(espece: str, nom: str, statutAdoption: bool):
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
        animals = []  
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Animal")
            result = cursor.fetchall()
            if result:
                for row in result:
                    animal_dict = {
                        "IDAnimal": row[0], 
                        "Espece": row[1], 
                        "Nom": row[2], 
                        "StatutAdoption": row[3]
                    }
                    animals.append(animal_dict)
                return animals  # Return the list of dictionaries
            else:
                return "erreur lors du get All"


    @staticmethod
    def delete_animal(animal_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("DELETE FROM Animal WHERE IDAnimal = ?", (animal_id,))
            cnxn.commit()
        return "Animal deleted successfully."
    
    
