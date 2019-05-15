from app import app, db
from app.models import User

if __name__ == "__main__":
    u = User.query.first()

    if u is None:
        user = User(name='Admin', email='admin@admin.com')
        user.set_password('admin123')
        db.session.add(u)
        db.session.commit()

    app.run(debug=True)
