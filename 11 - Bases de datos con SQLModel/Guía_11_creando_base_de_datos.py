from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class Héroe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    nombre_secreto: str
    edad: Optional[int] = None


sqlite_nombre = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_nombre}"
engine = create_engine(sqlite_url, echo=False)


def crear_héroes():
    héroe_1 = Héroe(nombre="Deadpond", nombre_secreto="Dive Wilson")
    héroe_2 = Héroe(nombre="Spider-Boy", nombre_secreto="Pedro Parqueador")
    héroe_3 = Héroe(nombre="Rusty-Man", nombre_secreto="Tommy Sharp", edad=48)

    with Session(engine) as session:
        session.add(héroe_1)
        session.add(héroe_2)
        session.add(héroe_3)
        session.commit()


def crear_db_y_tablas():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    crear_db_y_tablas()
    crear_héroes()
