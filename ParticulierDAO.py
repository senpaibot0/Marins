from dbCon import getConnexion

class ParticulierDAO:
    @staticmethod
    def create_particulier(type_particulier: str, nom: str, contact: str):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("INSERT INTO Particulier (TypeParticulier, Nom, Contact) VALUES (?, ?, ?)", (type_particulier, nom, contact))
            cnxn.commit()
        return f"Particulier {nom} created successfully."

    @staticmethod
    def get_particulier_by_id(particulier_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Particulier WHERE IDParticulier = ?", (particulier_id,))
            result = cursor.fetchone()
            if result:
                return {"IDParticulier": result[0], "TypeParticulier": result[1], "Nom": result[2], "Contact": result[3]}
            else:
                return None

    @staticmethod
    def get_all_particuliers():
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Particulier")
            particuliers = []
            for row in cursor.fetchall():
                particuliers.append({"IDParticulier": row[0], "TypeParticulier": row[1], "Nom": row[2], "Contact": row[3]})
            return particuliers

    @staticmethod
    def update_particulier(particulier_id: int, type_particulier: str = None, nom: str = None, contact: str = None):
        cnxn = getConnexion()
        updates = []
        params = []
        if type_particulier is not None:
            updates.append("TypeParticulier = ?")
            params.append(type_particulier)
        if nom is not None:
            updates.append("Nom = ?")
            params.append(nom)
        if contact is not None:
            updates.append("Contact = ?")
            params.append(contact)
        params.append(particulier_id)
        update_statement = "UPDATE Particulier SET " + ", ".join(updates) + " WHERE IDParticulier = ?"
        
        with cnxn.cursor() as cursor:
            cursor.execute(update_statement, params)
            cnxn.commit()
        return "Particulier record updated successfully."

    @staticmethod
    def delete_particulier(particulier_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("DELETE FROM Particulier WHERE IDParticulier = ?", (particulier_id,))
            cnxn.commit()
        return "Particulier record deleted successfully."
