# proyectofinalredes
PRoyecto final redes - socket programming
Juego de connect4 en línea (pero en red local)

#REQUEISITOS

 -numpy 
 -wcwidth
 -tabulate

Estos 3 requisitos pueden ser instalados con la ayuda de pip en la terminal escribiendo -pip install (nombre)

Network
    Network es una clase que utiliza el cliente para comunicarse con el servidor

Server
    Es el servidor desde donde se controlan todos los juegos, se aceptan todas las conexiónes y se envía información a los clientes

game
    Clase del objeto juego que es donde se encuentra la logica de conect4

cliente
    El cliente envía sus jugadas al servidor y juega connect4