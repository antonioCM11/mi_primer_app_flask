from app.extensions import db
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    email = db.Column(db.Strinmg(120), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f'<Usuario es {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)