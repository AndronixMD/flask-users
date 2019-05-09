from app import app
from flask import render_template
from flask_login import login_required, current_user
from sqlalchemy import or_
from app.models.user import User


@app.route('/')
@login_required
def index():
    users = User.query.filter(
        User.id != current_user.id,
        or_(
            User.admin_id == current_user.id,
            User.teacher_id == current_user.id,
            User.student_id == current_user.id
        )
    ).all()
    return render_template('pages/index.html', users=users)
