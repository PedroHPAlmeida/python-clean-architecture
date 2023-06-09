from faker import Faker
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from .register import RegisterPet


faker = Faker()


def test_register():
    """Testing register method in RegisterPet"""
    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_pet.register(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # Testing inputs
    assert pet_repo.insert_pet_param["name"] == attributes["name"]
    assert pet_repo.insert_pet_param["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_param["age"] == attributes["age"]

    # Testing FindUser inputs
    assert (
        find_user.by_id_and_name_params["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_params["name"]
        == attributes["user_information"]["user_name"]
    )

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]
