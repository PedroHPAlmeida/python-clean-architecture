from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import UserRepositorySpy, PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_pet_controller import RegisterPetController


faker = Faker()


def test_handle():
    """Testing handle method in RegisterPetController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_controller.handle(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.resgister_params["name"] == attributes["name"]
    assert register_pet_use_case.resgister_params["specie"] == attributes["specie"]
    assert register_pet_use_case.resgister_params["age"] == attributes["age"]
    assert (
        register_pet_use_case.resgister_params["user_information"]
        == attributes["user_information"]
    )

    # Testing Output
    assert response.status_code == 200
    assert "error" not in response.body
