from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import app
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'localhost'
db = SQLAlchemy(app)

class Song(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255))
	artist = db.Column(db.String(255))
	genre = db.Column(db.String(255))
	uploadTime = db.Column(db.DateTime)
	playTime = db.Column(db.DateTime)
	playCount = db.Column(db.Integer)

	def __init__ (self, title, artist, genre, uploadTime = None, playTime = None, playCount = -1):
		self.title = title
		self.artist = artist
		self.genre = genre
		if uploadTime is None:
			uploadTime = datetime.utcnow()
		self.uploadTime = uploadTime
		if playTime is None:
			playTime = datetime.utcnow()
		self.playTime = playTime
		if playCount is -1:
			playTime = 0
		self.playTime = playTime

	def __repr__(self):
		return '<Song %r>' % self.title



app.run()


'''
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
'''