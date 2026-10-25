from abc import ABC, abstractmethod


class Artista(ABC):
    """Clase base para todos los artistas."""

    GENEROS_PERMITIDOS = {
        "pop",
        "rock",
        "electrónica",
        "reguetón",
        "rap",
        "hip hop",
        "jazz",
        "blues",
        "salsa",
        "cumbia",
        "banda",
        "regional mexicano"
    }

    def __init__(self, nombre, genero, popularidad):
        # Validar nombre
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        # Validar género
        if not self.validar_genero(genero):
            raise ValueError("El género musical no está permitido.")

        self.nombre = nombre.strip()
        self.genero = genero.strip()

        # Se utiliza la propiedad para validar la popularidad
        self.popularidad = popularidad

        print(f"🎤 ¡Bienvenido al festival, {self.nombre}!")

    @property
    def popularidad(self):
        return self._popularidad

    @popularidad.setter
    def popularidad(self, popularidad):
        if not self.validar_popularidad(popularidad):
            raise ValueError(
                "La popularidad debe estar entre 1 y 100."
            )

        self._popularidad = popularidad

    @staticmethod
    def validar_genero(genero):
        """Verifica que el género sea uno de los permitidos."""

        if not isinstance(genero, str):
            return False

        return genero.strip().lower() in Artista.GENEROS_PERMITIDOS

    @staticmethod
    def validar_popularidad(popularidad):
        """Verifica que la popularidad esté entre 1 y 100."""

        return (
            isinstance(popularidad, int)
            and not isinstance(popularidad, bool)
            and 1 <= popularidad <= 100
        )

    def presentarse(self):
        """Presentación general del artista."""

        print(
            f"🎙️ Hola, soy {self.nombre} y mi género musical "
            f"es {self.genero}."
        )

    @abstractmethod
    def actuar(self):
        """Cada clase derivada debe implementar este método."""
        pass

    def despedirse(self):
        """Despedida general del artista."""

        print(
            f"👏 {self.nombre}: ¡Muchas gracias! "
            f"¡Hasta la próxima!"
        )

    def mostrar_info(self):
        """Muestra los datos del artista."""

        print("\n📋 Información del artista")
        print(f"Nombre: {self.nombre}")
        print(f"Género: {self.genero}")
        print(f"Popularidad: {self.popularidad}/100")


# -------------------------------------------------------
# CLASE CANTANTE
# -------------------------------------------------------

class Cantante(Artista):

    def __init__(
        self,
        nombre,
        genero,
        popularidad,
        cancion_mas_popular
    ):
        super().__init__(nombre, genero, popularidad)

        if not cancion_mas_popular.strip():
            raise ValueError(
                "La canción más popular no puede estar vacía."
            )

        self.cancion_mas_popular = cancion_mas_popular.strip()

    def presentarse(self):
        super().presentarse()
        print("🎵 ¡Prepárense para cantar!")

    def actuar(self):
        print(
            f"🎶 {self.nombre} canta su éxito "
            f"{self.cancion_mas_popular} con gran energía."
        )


# -------------------------------------------------------
# CLASE DJ
# -------------------------------------------------------

class DJ(Artista):

    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)

        if not estilo.strip():
            raise ValueError(
                "El estilo del DJ no puede estar vacío."
            )

        self.estilo = estilo.strip()

    def presentarse(self):
        super().presentarse()
        print("🎉 ¡Que empiece la fiesta!")

    def actuar(self):
        print(
            f"🎧 El DJ {self.nombre} mezcla temas de estilo "
            f"{self.estilo}, haciendo vibrar al público."
        )


# -------------------------------------------------------
# CLASE BANDA
# -------------------------------------------------------

class Banda(Artista):

    def __init__(
        self,
        nombre,
        genero,
        popularidad,
        integrantes
    ):
        super().__init__(nombre, genero, popularidad)

        if (
            not isinstance(integrantes, int)
            or isinstance(integrantes, bool)
            or integrantes <= 0
        ):
            raise ValueError(
                "El número de integrantes debe ser un entero positivo."
            )

        self.integrantes = integrantes

    def presentarse(self):
        super().presentarse()
        print("🎸 ¡Somos una banda en vivo!")

    def actuar(self):
        print(
            f"🎸 La banda {self.nombre} con "
            f"{self.integrantes} integrantes toca "
            f"un poderoso solo de guitarra."
        )


# -------------------------------------------------------
# FUNCIÓN POLIMÓRFICA
# -------------------------------------------------------

def iniciar_festival(lista_artistas):
    """
    Inicia el festival con todos los artistas.
    Utiliza polimorfismo puro.
    """

    print("\n🎉 ¡BIENVENIDOS AL FESTIVAL! 🎉")
    print("=" * 50)

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()

        print("🎆 Fin de la actuación 🎆")
        print("=" * 50)