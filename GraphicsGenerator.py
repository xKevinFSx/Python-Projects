import mysql.connector
import config
from mysql.connector import errorcode


#Conexão com banco de dados
try:
    cnx = mysql.connector.connect(user=config.user, password=config.password, database=config.database)
    if cnx.is_connected():
        print('Conexão com banco de dados feita com sucesso')
        
        #Fazer consulta no banco de dados através do cursor    
        cursor = cnx.cursor()

        query = ('SELECT name, population FROM city ORDER BY Population DESC LIMIT 10')

        cursor.execute(query)
        resultado = cursor.fetchall()
        
        for i in resultado:
            print(i)
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Nome de usuario ou senha estão incorretos')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados não existe')
    else:
        print(err)
else:
    cnx.close()