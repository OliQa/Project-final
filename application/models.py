
from application import db
from application import login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))




class Users(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(500), nullable=False, unique=True)
        password = db.Column(db.String(500), nullable=False)

        def __repr__(self):
                return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])




class Gear(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        build_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        weapon = db.Column(db.String(40), nullable=True)
        ammotype = db.Column(db.String(40), nullable=True)
        bodyarmour = db.Column(db.String(100), nullable=True)
        helmet = db.Column(db.String(100), nullable=True)
        buildname = db.Column(db.String(50), nullable=False)
        comment = db.Column(db.String(250), nullable=True)

        def __repr__(self):
            return ''.join([
			'Title: ',self.buildname, '\r\n',
			'Comment: ',self.comment, '\r\n',
			'Weapon: ',self.weapon, '\r\n',
			'Ammo: ',self.ammotype, '\r\n',
			'Bodyarmour: ',self.bodyarmour, '\r\n',
			'Helmet: ',self.helmet, '\r\n'
			])
