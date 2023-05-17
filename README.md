
# Proyecto final Introducción a redes - socket programming 🔌

El siguiente proyecto consiste de un juego de Connect 4 con dos jugadores, en linea, en la misma red local.

# Requisitos para poder jugar 📝

 `-numpy
 -wcwidth
 -tabulate`

Estos 3 requisitos pueden ser instalados con la ayuda de pip en la terminal escribiendo `-pip install *nombre*`

## ¿Qué encontrarás? 🧐

Network 📶
    Network es una clase que utiliza el cliente para comunicarse con el servidor

Server 🖥
    Es el servidor desde donde se controlan todos los juegos, se aceptan todas las conexiones y se envía información a los clientes

Game 🕹
    Clase del objeto juego que es donde se encuentra la lógica de conect4

Client 📱
    El cliente envía sus jugadas al servidor y juega connect4
    
# Pasos 🎲
1. Cambiar la IP en network.py y server.py a la de tu dispositivo/red
2. Correr server.py
3. Correr en otra terminal client.py
4. Si se va a jugar solo, correr dos terminales de client.py
5. Si se va a jugar en dos dispositivos, asegurarse que ambas están en la misma red y correr client.py
6. Después de tener una conexión exitosa, solo falta disfrutar 🎉
