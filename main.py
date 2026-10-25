from clases.artistas import (
    Artista,
    Cantante,
    DJ,
    Banda,
    iniciar_festival
)


def solicitar_cantidad_artistas():
    """Solicita la cantidad de artistas."""

    while True:
        try:
            cantidad = int(
                input("¿Cuántos artistas se presentarán?: ")
            )

            if cantidad <= 0:
                raise ValueError(
                    "La cantidad debe ser mayor que cero."
                )

            return cantidad

        except ValueError as error:
            print(f"❌ Error: {error}")


def solicitar_tipo_artista():
    """Solicita el tipo de artista."""

    while True:
        tipo = input(
            "Tipo de artista (Cantante, DJ o Banda): "
        ).strip().lower()

        if tipo in ["cantante", "dj", "banda"]:
            return tipo

        print(
            "❌ Tipo incorrecto. "
            "Debe introducir Cantante, DJ o Banda."
        )


def solicitar_genero():
    """Solicita y valida el género musical."""

    while True:
        genero = input(
            "Género musical: "
        ).strip().lower()

        if Artista.validar_genero(genero):
            return genero

        print("❌ Género musical no permitido.")

        print("\nGéneros permitidos:")
        print(
            "Pop, Rock, Electrónica, Reguetón, Rap, "
            "Hip Hop, Jazz, Blues, Salsa, Cumbia, "
            "Banda y Regional Mexicano."
        )


def solicitar_popularidad():
    """Solicita una popularidad válida."""

    while True:
        try:
            popularidad = int(
                input("Popularidad (1-100): ")
            )

            if not Artista.validar_popularidad(popularidad):
                raise ValueError(
                    "La popularidad debe estar entre 1 y 100."
                )

            return popularidad

        except ValueError as error:
            print(f"❌ Error: {error}")


def solicitar_integrantes():
    """Solicita el número de integrantes."""

    while True:
        try:
            integrantes = int(
                input("Número de integrantes: ")
            )

            if integrantes <= 0:
                raise ValueError(
                    "El número de integrantes debe ser positivo."
                )

            return integrantes

        except ValueError as error:
            print(f"❌ Error: {error}")


def crear_artista():
    """Crea el artista según el tipo seleccionado."""

    tipo = solicitar_tipo_artista()

    nombre = input("Nombre del artista: ").strip()

    genero = solicitar_genero()

    popularidad = solicitar_popularidad()

    if tipo == "cantante":

        cancion = input(
            "Canción más popular: "
        ).strip()

        return Cantante(
            nombre,
            genero,
            popularidad,
            cancion
        )

    elif tipo == "dj":

        estilo = input(
            "Estilo del DJ (House, Techno, Dubstep, etc.): "
        ).strip()

        return DJ(
            nombre,
            genero,
            popularidad,
            estilo
        )

    else:

        integrantes = solicitar_integrantes()

        return Banda(
            nombre,
            genero,
            popularidad,
            integrantes
        )


def main():
    """Programa principal."""

    lista_artistas = []

    print("=" * 50)
    print("🎵 FESTIVAL MUSICAL 🎵")
    print("=" * 50)

    cantidad = solicitar_cantidad_artistas()

    for numero in range(1, cantidad + 1):

        print(f"\nRegistro del artista {numero}")
        print("-" * 50)

        while True:

            try:
                artista = crear_artista()

                lista_artistas.append(artista)

                print(
                    f"✅ {artista.nombre} fue registrado "
                    f"correctamente."
                )

                break

            except ValueError as error:

                print(
                    f"❌ Error al registrar al artista: {error}"
                )

                print(
                    "Por favor, vuelva a introducir los datos."
                )

    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()