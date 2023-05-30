from typing import Type, Dict, List
from src.data.find_user import FindUser
from src.domain.test import mock_users, mock_pets
from src.domain.models import Pets, Users
from ..interfaces import PetRepositoryInterface as PetRepository


class RegisterPetSpy:
    """Class to define usecase: Register Pet"""

    def __init__(
        self, pet_repository: Type[PetRepository], find_user: Type[FindUser]
    ) -> None:
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.resgister_params = {}

    def register(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Register Pet"""

        self.resgister_params["name"] = name
        self.resgister_params["specie"] = specie
        self.resgister_params["user_information"] = user_information
        self.resgister_params["age"] = age

        response = None

        # Validating entry and trying to find and user
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pets()

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user infos and select user"""

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = mock_users()

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = mock_users()

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = mock_users()

        else:
            return {"Success": False, "Data": None}

        return {"Success": True, "Data": user_founded}
