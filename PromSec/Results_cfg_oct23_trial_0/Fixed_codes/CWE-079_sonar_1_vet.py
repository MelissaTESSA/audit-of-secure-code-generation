from flask import Flask, request, make_response
import os

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    name = request.args.get('name')
    file_path = "Test/CWE-079_sonar_1/xss_shared.html"
    
    with open(file_path, 'r') as file:
        html_content = file.read()
        modified_html = html_content.replace("{{name}}", name)
    
    response = make_response(modified_html)
    return response

if __name__ == '__main__':
    app.run()