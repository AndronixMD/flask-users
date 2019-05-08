from app import app


@app.route('/')
def index():
    print('hey')

    return 'ho'
