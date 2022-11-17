from pprint import pprint
from typing import Optional

from sqlmodel import Field, Session, SQLModel, col, create_engine, or_, select


class Héroe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    nombre_secreto: str
    edad: Optional[int] = None


sqlite_nombre = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_nombre}"
engine = create_engine(sqlite_url, echo=False)


def crear_héroes():
    héroe_1 = Héroe(nombre="Deadpond", nombre_secreto="Dive")
    héroe_2 = Héroe(nombre="Spider-Boy", nombre_secreto="Pedro")
    héroe_3 = Héroe(nombre="Rusty-Man", nombre_secreto="Tommy", edad=48)
    héroe_4 = Héroe(nombre="Tarantula", nombre_secreto="Natalia Roman-on", edad=32)
    héroe_5 = Héroe(nombre="Black Lion", nombre_secreto="Trevor Challa", edad=35)
    héroe_6 = Héroe(nombre="Dr. Weird", nombre_secreto="Steve Weird", edad=36)
    héroe_7 = Héroe(nombre="Captain America", nombre_secreto="Esteban", edad=93)
    with Session(engine) as session:
        session.add(héroe_1)
        session.add(héroe_2)
        session.add(héroe_3)
        session.add(héroe_4)
        session.add(héroe_5)
        session.add(héroe_6)
        session.add(héroe_7)
        session.commit()


def consultar_héroes():
    with Session(engine) as session:
        print("EJERCICIO 1: Edad contiene - y edad es null")
        consulta = select(Héroe).where(
            col(Héroe.nombre).contains("-"),
            col(Héroe.edad).is_(None),
        )
        resultado = session.exec(consulta).all()
        pprint(resultado)

        print("EJERCICIO 2: id es 1")
        consulta = select(Héroe).where(Héroe.id == 11111)
        resultado = session.exec(consulta).first()
        pprint(resultado)
        resultado = session.get(Héroe, 222221)
        pprint(resultado)

        print("EJERCICIO 3 longitud de nombre > 9 y edad < 70")
        from sqlalchemy.sql.expression import func

        consulta = (
            select(Héroe)
            .filter(func.length(Héroe.nombre) < 10)
            .where(col(Héroe.edad) < 70)
        )
        resultado = session.exec(consulta).all()
        pprint(resultado)

        print("EJERCICIO 4 no tienen edad, o edad > 65")
        consulta = select(Héroe).where(
            or_(col(Héroe.edad).is_(None), col(Héroe.edad) > 65)
        )

        resultado = session.exec(consulta).all()
        pprint(resultado)

        print("********")
        consulta = select(Héroe).where(col(Héroe.edad) > 40).limit(2)
        resultado = session.exec(consulta).all()
        pprint(resultado)
        # resultado = session.exec(select(Héroe).
        #                          where(Héroe.nombre == "Deadpond")).one()
        # pprint(resultado)


def modificar_héroes():
    with Session(engine) as session:
        consulta = select(Héroe).where(Héroe.nombre == "Spider-Boy")
        resultado = session.exec(consulta)
        héroe = resultado.one()
        print("Héroe:", héroe)
        héroe.edad = 20
        session.add(héroe)
        session.commit()
        session.refresh(héroe)
        print("Héroe modificado:", héroe)


def eliminar_héroes():
    with Session(engine) as session:
        consulta = select(Héroe).where(Héroe.nombre == "Tarantula")
        resultado = session.exec(consulta)
        héroe = resultado.one()
        print("Héroe:", héroe)
        session.delete(héroe)
        session.commit()
        print("Héroe eliminado:", héroe)


def eliminar_héroes_edad_NULL():
    with Session(engine) as session:
        consulta = select(Héroe).where(col(Héroe.edad).is_(None))
        héroes = session.exec(consulta)
        for héroe in héroes:
            print(héroe)
            session.delete(héroe)
        session.commit()


def crear_db_y_tablas():
    SQLModel.metadata.create_all(engine)


def main():
    crear_db_y_tablas()
    crear_héroes()
    consultar_héroes()
    # modificar_héroes()
    # eliminar_héroes()
    # eliminar_héroes_edad_NULL()


main()
