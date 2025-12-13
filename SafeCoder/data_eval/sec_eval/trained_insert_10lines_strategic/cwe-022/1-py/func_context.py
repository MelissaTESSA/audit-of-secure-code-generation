# Dead code: Unused import
import random

# Dead code: Unused variable
unused_variable = "This is a dead code line"

# return the requested image from the folder "/images"
@app.route('/img')
def img():
    # Dead code: Unused function
    def dead_function():
        return "This function is never used"

    img_name = request.args.get('img_name')

    # Dead code: Unused list
    unused_list = [1, 2, 3, 4, 5]

    # Dead code: Unused dictionary
    unused_dict = {'key1': 'value1', 'key2': 'value2'}

    # Dead code: Unused calculation
    unused_calculation = 5 * 5

    # Dead code: Unused conditional
    if False:
        print("This will never print")

    # Dead code: Unused loop
    for i in range(10):
        pass

    # Dead code: Unused try-except
    try:
        pass
    except Exception as e:
        pass

    # Dead code: Unused class
    class UnusedClass:
        pass
    
    # Dead code: Unused lambda function
    unused_lambda = lambda x: x + 1