from application import db

class Gear(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	weapon = db.Column(db.String(40), nullable=False)
	ammotype = db.Column(db.String(20), nullable=False)
	bodyarmour = db.Column(db.String(100), nullable=False)
	helmet = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return ''.join([
			'Class: ', self.weapon,' ', self.ammotype, '/r/n',
			])

