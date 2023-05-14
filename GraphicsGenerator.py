import mysql.connector
import config
import matplotlib.pyplot as plt
import numpy as np
from mysql.connector import errorcode

#Conexão com banco de dados
try:
    cnx = mysql.connector.connect(user=config.user, password=config.password, database=config.database)
    if cnx.is_connected():
        print('Conexão com banco de dados feita com sucesso')
        
        #Fazer consulta no banco de dados através do cursor    
        cursor = cnx.cursor()

        query = ('SELECT name, population FROM city ORDER BY Population DESC LIMIT 10')
        query1 = ('SELECT name, population, lifeexpectancy FROM country ORDER BY Population DESC LIMIT 10')

        #Printar o resultado das querys
        cursor.execute(query)
        resultado = cursor.fetchall()
        
        coluna_x = [resultados[0] for resultados in resultado]
        coluna_y = [resultados[1] for resultados in resultado]
        
        #for row in resultado:
        #    cidades.append(str(row[0]))
        #    populacao.append(int(row[1]))
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Nome de usuario ou senha estão incorretos')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados não existe')
    else:
        print(err)
else:
    cnx.close()
        
plt.barh(range(len(coluna_x)), coluna_y)
plt.yticks(range(len(coluna_x)), coluna_x)

plt.gca().invert_yaxis()

plt.title('As 10 maiores cidades populacionais do mundo')
plt.xlabel('Quantidade populacional')

plt.show()
