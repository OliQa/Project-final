from application import db
from application.models import Gear

db.drop_all()
db.create_all()

