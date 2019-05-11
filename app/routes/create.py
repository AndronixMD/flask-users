from app import app, db
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.forms.admin import AdminForm
from app.forms.student import StudentForm
from app.models.user import User


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = None

    if current_user.parent_admin is not None:
        form = AdminForm()

        if form.validate_on_submit():
            user = User(
                name=form.name.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)

            if form.type_user.data == 'admin':
                user.admin_id = current_user.id
            elif form.type_user.data == 'teacher':
                user.teacher_id = current_user.id

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('create'))

    elif current_user.admin is not None:
        form = StudentForm()

        if form.validate_on_submit():
            user = User(
                name=form.name.data,
                address=form.address.data,
                age=int(form.age.data),
                student_id=current_user.id
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('create'))

    return render_template('pages/create.html', form=form)
