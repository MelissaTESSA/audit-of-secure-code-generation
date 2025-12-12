import os
import traceback
from flask import Flask

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def bad_route():
    try:
        do_computation()
    except Exception as e:
        traceback.print_exc()
        return str(e), 500

if __name__ == '__main__':
    app.run()