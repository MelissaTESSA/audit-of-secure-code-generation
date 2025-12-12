from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.ERROR)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def bad_route():
    try:
        do_computation()
    except Exception as e:
        app.logger.error(str(e))
        return "An error occurred", 500

if __name__ == '__main__':
    app.run()