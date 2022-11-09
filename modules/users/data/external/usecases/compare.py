from modules.users.data.external.usecases.validatorbiometric import ValidatorBiometric


class Compare:

    @staticmethod
    def biometric(path, users):
        for user in users:
            result = ValidatorBiometric.validator(path, user['url_biometria'])

            if (result):
                return user
            else:
                continue

        return
