from modules.users.data.external.repository.database.database import get_database


class UserRepository:
    @staticmethod
    def getAllUsers():

        db = get_database()

        result = db.get_database('admin')

        cursor = result.get_collection('users').find({})

        return cursor
