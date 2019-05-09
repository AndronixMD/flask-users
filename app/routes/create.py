from app import app
from flask import render_template
from flask_login import login_required


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    return render_template('pages/create.html')
