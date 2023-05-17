
# Proyecto final Introducción a redes - socket programming 🔌

El siguiente proyecto consiste de un juego de Connect 4 con dos jugadores, en linea, en la misma red local.

# Requísitos para poder jugar

 `-numpy
 -wcwidth
 -tabulate`

Estos 3 requisitos pueden ser instalados con la ayuda de pip en la terminal escribiendo `-pip install *nombre*`

## ¿Qué encontrarás?

Network 📶
    Network es una clase que utiliza el cliente para comunicarse con el servidor

Server 🖥
    Es el servidor desde donde se controlan todos los juegos, se aceptan todas las conexiónes y se envía información a los clientes

Game 🕹
    Clase del objeto juego que es donde se encuentra la logica de conect4

Client 📱
    El cliente envía sus jugadas al servidor y juega connect4
