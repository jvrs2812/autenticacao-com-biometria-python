from genericpath import exists

from modules.users.data.external.repository.userrepository import UserRepository
from modules.users.data.external.usecases.compare import Compare
from modules.users.data.external.usecases.validator import Validator


class Authentication:
    @staticmethod
    def auth(path):
        Validator.validate(path=path)

        user = Compare.biometric(path, UserRepository.getAllUsers())

        if (user == None):
            raise Exception("Usuário não encontrado !!")

        return user
