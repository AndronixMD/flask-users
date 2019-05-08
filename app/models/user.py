from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer)
    address = db.Column(db.String(150))

    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    parent_admin = db.relationship('User',
                                   primaryjoin=('user.c.id==user.c.admin_id'),
                                   remote_side='User.id',
                                   backref=db.backref('admins'))

    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    admin = db.relationship('User',
                            primaryjoin=('user.c.id==user.c.teacher_id'),
                            remote_side='User.id',
                            backref=db.backref('teachers'))

    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    teacher = db.relationship('User',
                              primaryjoin=('user.c.id==user.c.student_id'),
                              remote_side='User.id',
                              backref=db.backref('students'))

    def __repr__(self):
        return 'User {}'.format(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
