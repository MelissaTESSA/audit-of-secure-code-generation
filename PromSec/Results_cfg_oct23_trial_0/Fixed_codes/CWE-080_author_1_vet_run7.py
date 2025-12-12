from flask import Flask, render_template

app = Flask(__name__)

@app.route('/renderHtml')
def renderHTML():
    return render_template('template.html', user_input='<script>alert("XSS")</script>')

if __name__ == '__main__':
    app.run()