Festival Musical
Descripción
Este proyecto consiste en un sistema desarrollado en Python para gestionar las presentaciones de diferentes tipos de artistas en un festival musical.

El programa permite registrar Cantantes, DJs y Bandas, almacenarlos en una lista e iniciar el festival utilizando conceptos de Programación Orientada a Objetos.

Cada tipo de artista tiene su propia forma de actuar, pero todos comparten métodos para presentarse y despedirse.

Estructura del proyecto
festival_musical/
│
├── main.py
├── README.md
│
└── clases/
    └── artistas.py
Tipos de artistas
El sistema permite registrar tres tipos de artistas:

Cantante
Tiene como atributo adicional:

Canción más popular.
Su método actuar() muestra al cantante interpretando su canción más popular.

DJ
Tiene como atributo adicional:

Estilo.
Por ejemplo:

House
Techno
Dubstep
Su método actuar() muestra al DJ mezclando temas de su estilo musical.

Banda
Tiene como atributo adicional:

Número de integrantes.
El sistema valida que el número de integrantes sea un número entero positivo.

Géneros musicales permitidos
El programa permite los siguientes 12 géneros musicales:

Pop
Rock
Electrónica
Reguetón
Rap
Hip Hop
Jazz
Blues
Salsa
Cumbia
Banda
Regional Mexicano
Programación Orientada a Objetos
Este proyecto utiliza diferentes conceptos de Programación Orientada a Objetos.

Herencia
Las clases:

Cantante
DJ
Banda
heredan de la clase base:

Artista
Abstracción
La clase Artista utiliza ABC y el decorador:

@abstractmethod
El método actuar() es abstracto y debe ser implementado por las clases derivadas.

Polimorfismo
La función:

iniciar_festival(lista_artistas)
recorre la lista de artistas y ejecuta:

artista.presentarse()
artista.actuar()
artista.despedirse()
Cada objeto ejecuta su propia implementación de los métodos sin necesidad de utilizar isinstance() para distinguir el tipo de artista.

Encapsulamiento
La popularidad del artista se controla mediante:

@property
y:

@popularidad.setter
Esto permite validar que la popularidad se encuentre entre 1 y 100.

Métodos estáticos
La clase Artista utiliza métodos estáticos para realizar validaciones:

validar_genero()
validar_popularidad()
Validaciones
El sistema comprueba:

Que el tipo de artista sea Cantante, DJ o Banda.
Que el nombre del artista no esté vacío.
Que el género musical se encuentre entre los permitidos.
Que la popularidad esté entre 1 y 100.
Que el número de integrantes de una banda sea un entero positivo.
Que la canción más popular del cantante no esté vacía.
Que el estilo del DJ no esté vacío.
También se utiliza try/except para controlar los errores durante la captura de los datos.

Ejecución del programa
Para ejecutar el programa, se debe abrir una terminal en la carpeta principal del proyecto y ejecutar:

python main.py
Si el sistema utiliza el comando python3, se puede ejecutar:

python3 main.py
El programa solicitará primero la cantidad de artistas que se presentarán.

Después solicitará los datos correspondientes a cada artista:

Tipo de artista.
Nombre.
Género musical.
Popularidad.
Atributo específico según el tipo de artista.
Finalmente se iniciará el festival con todos los artistas registrados.

Funcionamiento del festival
La función iniciar_festival() recorre la lista de artistas.

Para cada artista ejecuta los siguientes métodos:

presentarse()
actuar()
despedirse()
Esto permite utilizar polimorfismo, ya que cada tipo de artista ejecuta su propia versión del método actuar().

Tecnologías utilizadas
Python
Programación Orientada a Objetos
Visual Studio Code
Git
GitHub