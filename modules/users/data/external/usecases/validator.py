from genericpath import exists
import pathlib


class Validator:

    @staticmethod
    def validate(path):
        extensions = [".tif"]

        if (not exists(path)):
            raise Exception("Arquivo não Encontrado")
        else:
            ext = pathlib.Path(path).suffix

            if (not extensions.__contains__(ext)):
                raise Exception("Arquivo com extensão não permitida")
