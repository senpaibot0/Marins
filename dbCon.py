import pyodbc

def getConnexion():	
    conn_str = (
                    "Driver=ODBC Driver 17 for SQL Server;"
                    "Server=MSI\SQLEXPRESS;"
                    "Database=GeoMarinBD;"   
                    "Encrypt=yes;"
                    "TrustServerCertificate=yes;"
                    "Trusted_Connection=yes;"
                )
    
    cnxn = pyodbc.connect(conn_str) 
    return cnxn
    
