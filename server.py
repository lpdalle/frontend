from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    title = 'lpdalle picture generator'
    content = 'Wellcome to lpdalle picture generator'
    return render_template('index.html', page_title=title, page_content=content)


if __name__ == '__main__':
   app.run(debug=True)
