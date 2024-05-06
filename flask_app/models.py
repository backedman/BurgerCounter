from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


# TODO: implement
@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()
    pass

# TODO: implement fields
class User(db.Document, UserMixin):
    username = db.StringField(unique=True, required=True)
    email = db.EmailField(unique=True,required=True)
    password = db.StringField()
    burger_counter = db.IntField()
    calorie_counter = db.IntField()

    # Returns unique string identifying our object
    def get_id(self):
        # TODO: implement
        return self.username
        pass