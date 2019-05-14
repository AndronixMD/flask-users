from app import app, db
from flask import render_template, request, redirect, url_for, make_response
from flask_login import login_required, current_user
from app.models.user import User


@app.route('/', methods=['GET', 'DELETE'])
@login_required
def index():
    if request.method == 'DELETE':
        id = request.args.get('user_id')
        if id is not None:
            user = User.query.get(id)
            if current_user.admin_id is not None:
                teachers = User.query.filter_by(teacher_id=user.id)
                for t in teachers.all():
                    User.query.filter_by(student_id=t.id).delete()
                teachers.delete()
                User.query.filter_by(student_id=user.id).delete()

            db.session.delete(user)
            db.session.commit()

        return ''

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
