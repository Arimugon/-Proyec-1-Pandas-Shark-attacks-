# Proyec-1-Pandas-Shark-attacks
![shark-dangers](https://user-images.githubusercontent.com/113017465/198995330-241578d6-be52-4102-97ea-df8f2cd6f1ae.jpg)


Este proyecto consiste en la valoración y limpieza de una DataSet que facilita información acerca de los ataques producidos por tiburones en todo el mundo.La tabla contiene multitud de valores nulos y valores no relacionados que debemos limpiar. Además se nos pide que presentemos una hipótesis, saquemos conclusiones sobre ella y realicemos un proyecto de visualización para demostrarlas.

Lo primero que hay que realizar es la limpieza de los datos que tengo, para ello voy a utilizar Jupyter Notebook. Mi proceso de limpieza ha sido el siguiente:

  **-1.Lectura e info del DataSet:**
Valoro la informacion aportada,el número de valores nulos, la repercusion o importancia que tienen las diferentes columnas tanto para mi hipótesis como para la     integridad del DataSet. 
Planteamiento de mi hipótesis:

-El país en el que más ataques de tiburones se producen en en EEUU, concretamente en el area de Florida.

-Que se producen más ataques a hombres que a mujeres.

-Que el tiburon que más ataques a humanos produce es el White Shark.

  **-2.Eliminación de tablas y duplicados:**
Eliminación de tablas con casi el 100% de nulos 'unnamed_22' y 'unnamed_23'
Eliminación de valores duplicados.
Eliminación de valores nulos que hay al final de la tabla.
Eliminación de tablas con una alto porcentaje de duplicados. En esto caso yo eliminé 'case_number1', 'case_number2','href'y 'date'.

  **-3.Proceso limpieza de las columnas restantes:**
Tras la eliminación de las columnas mencionadas anteriormente, he procedido a limpiar una a una las columnas que me quedan.
Principalmente este proceso de limpieza ha consistido en:

3.1 Sustitución de valores nulos.

3.2 Minimización del número de valores nulos.

3.3 Creación de funciones para la unificación de los valores.

Una vez obtenido un DataSet nuevo y limpio, llevo a cabo un proceso de visualización para poder demostrar mi hipótesis a través de la creación de tablas.


**HIPÓTESIS:**

-El país en el que más ataques de tiburones se producen en en EEUU, concretamente en el area de Florida.
![ataques en usa](https://user-images.githubusercontent.com/113017465/198994093-a8832eb1-0b46-411f-b275-b2152b5eadd2.png)
![ataques en area](https://user-images.githubusercontent.com/113017465/198994221-337a70b6-c429-409f-a242-3d3caefe7330.png)

-Que se producen más ataques a hombres que a mujeres.
![ataques a genero](https://user-images.githubusercontent.com/113017465/198994264-f68339b1-0d46-4018-ad3c-cb2c3be05406.png)

-Que el tiburon que más ataques a humanos produce es el White Shark.
![sharks](https://user-images.githubusercontent.com/113017465/198994340-d53ce9f6-490d-42a8-9aeb-220d110cce61.png)




