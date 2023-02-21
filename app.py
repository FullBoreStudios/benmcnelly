# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Welcome to BenMcNelly.com',
        content="Welcome to BenMcNelly.com")


@app.route('/why')
def why():
    return render_template(
        'why.html',
        title='Why?',
        content="If what you are doing is not important, then why are you doing it? Work on problems that might have"
                " a future of becoming important to solve. ~Ben")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


# eof