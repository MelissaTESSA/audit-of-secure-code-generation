from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/render')
def render_template():
    name = request.args.get('name')
    return render_template('Test/CWE-079_codeql_1/template.html', name=name)

if __name__ == '__main__':
    app.run()