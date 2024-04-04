from dbCon import getConnexion

class ClimatDAO:
    @staticmethod
    def create_climat(temperature: float, vent: float, courant: float):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("INSERT INTO Climat (Temperature, Vent, Courant) VALUES (?, ?, ?)", (temperature, vent, courant))
            cnxn.commit()
        return "Climat record created successfully."
    
    @staticmethod
    def get_climat_by_id(climat_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Climat WHERE IDClimat = ?", (climat_id,))
            result = cursor.fetchone()
            if result:
                return {"IDClimat": result[0], "Temperature": result[1], "Vent": result[2], "Courant": result[3]}
            else:
                return None

    @staticmethod
    def get_all_climats():
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("SELECT * FROM Climat")
            climats = []
            for row in cursor.fetchall():
                climats.append({"IDClimat": row[0], "Temperature": row[1], "Vent": row[2], "Courant": row[3]})
            return climats

    @staticmethod
    def update_climat(climat_id: int, temperature: float = None, vent: float = None, courant: float = None):
        cnxn = getConnexion()
        updates = []
        params = []
        if temperature is not None:
            updates.append("Temperature = ?")
            params.append(temperature)
        if vent is not None:
            updates.append("Vent = ?")
            params.append(vent)
        if courant is not None:
            updates.append("Courant = ?")
            params.append(courant)
        params.append(climat_id)
        update_statement = "UPDATE Climat SET " + ", ".join(updates) + " WHERE IDClimat = ?"
        
        with cnxn.cursor() as cursor:
            cursor.execute(update_statement, params)
            cnxn.commit()
        return "Climat record updated successfully."

    @staticmethod
    def delete_climat(climat_id: int):
        cnxn = getConnexion()
        with cnxn.cursor() as cursor:
            cursor.execute("DELETE FROM Climat WHERE IDClimat = ?", (climat_id,))
            cnxn.commit()
        return "Climat record deleted successfully."
