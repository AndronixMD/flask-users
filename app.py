from app import app, db
from app.models import User

if __name__ == "__main__":
    user = User.query.first()

    if user is None:
        user = User(name='Admin', email='admin@admin.com')
        user.set_password('admin123')
        db.session.add(user)
        db.session.commit()

        user.admin_id = user.id
        db.session.commit()

    app.run(debug=True)
