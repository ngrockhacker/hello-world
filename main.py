from flask import Flask, render_template

app = FLask(__name__)

@app.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    app.run()

