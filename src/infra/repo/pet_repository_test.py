from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import AnimalTypes
from .pet_repository import PetRepository


faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """Should insert pet in Pet table and return it"""
    name = faker.name()
    specie = AnimalTypes.fish.value
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=1)

    # SQL Commands
    new_pet = pet_repository.insert_pet(
        name=name, specie=specie, age=age, user_id=user_id
    )
    engine = db_connection_handler.get_engine()
    query_pet = engine.execute(
        f"SELECT * FROM pets WHERE id='{new_pet.id}';"
    ).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id

    engine.execute(f"DELETE FROM pets WHERE id='{new_pet.id}';")
