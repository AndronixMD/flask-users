from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User


@app.route('/')
@login_required
def index():
    users = []
    if current_user.admin_id is not None:
        users = User.query.filter(
            User.id != current_user.id,
        ).all()
    elif current_user.teacher_id is not None:
        users = User.query.filter(
            User.id != current_user.id,
            User.student_id == current_user.id
        ).all()

    return render_template('pages/index.html', users=users)
