#!/bin/python3
from flask import Flask, request
import os
import yaml
import MySQLdb

app = Flask(__name__)

# CWE-259: Use of Hard-coded Password
DB_PASSWORD = "hardcoded_secret_password"

def get_db_connection():
    return MySQLdb.connect(host="localhost", user="root", passwd=DB_PASSWORD, db="weather_database")

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # CWE-20: Improper Input Validation
    yaml_payload = request.args.get('payload', '')
    
    # Using yaml.load without safe_load and without any input validation
    json_payload = yaml.load(yaml_payload)
    
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']

    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s", (date, latitude, longitude))
    temp = c.fetchone()
    db.close()

    return str(temp[0]) if temp else "Temperature not found"

@app.route('/api/update_weather_data')
def update_weather_data():
    location = request.args.get('location', '')
    
    # CWE-78: OS Command Injection
    os.system(f"weather_update_script.py --location {location}")
    
    return f"Weather data updated for {location}"

if __name__ == '__main__':
    app.run(debug=False)


def unused_function_1():
    x = 10
    y = 20
    z = x + y
    return z

def unused_function_2():
    name = "Alice"
    greeting = f"Hello, {name}!"
    return greeting

def unused_function_3():
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    return total

def unused_function_4():
    def inner_function():
        return "Inner function result"
    result = inner_function()
    return result

def unused_function_5():
    x = 50
    y = 100
    if x < y:
        return "x is less than y"
    else:
        return "x is not less than y"

def unused_function_6():
    text = "Python"
    if text.startswith("P"):
        return "Text starts with P"
    return "Text does not start with P"

def unused_function_7():
    a = 3
    b = 7
    return a * b

def unused_function_8():
    fruits = ["apple", "banana", "cherry"]
    return fruits[0]

def unused_function_9():
    value = 42
    return value ** 2

def unused_function_10():
    data = {"key": "value"}
    return data.get("key")

def unused_function_11():
    def helper():
        return 100
    return helper()

def unused_function_12():
    for i in range(5):
        pass
    return "Loop complete"

def unused_function_13():
    x = 10
    y = 2
    return x / y

def unused_function_14():
    return "This is a constant string"

def unused_function_15():
    flag = True
    return not flag

def unused_function_16():
    a = 10
    b = 5
    c = a - b
    return c

def unused_function_17():
    def nested():
        return "Nested"
    return nested()

def unused_function_18():
    items = [10, 20, 30]
    return len(items)

def unused_function_19():
    text = "Hello"
    return text.lower()

def unused_function_20():
    number = 25
    if number > 0:
        return "Positive"
    return "Negative"

def unused_function_21():
    x = 5
    y = 25
    return y % x

def unused_function_22():
    string = "abcdef"
    return string[::-1]

def unused_function_23():
    def utility():
        return 42
    return utility()

def unused_function_24():
    value = None
    if value is None:
        return "Value is None"

def unused_function_25():
    return 3.14

def unused_function_26():
    animals = {"cat", "dog", "bird"}
    return "cat" in animals

def unused_function_27():
    value = "test"
    return value.isalpha()

def unused_function_28():
    numbers = [2, 4, 6, 8]
    return min(numbers)

def unused_function_29():
    a, b = 1, 1
    return a == b

def unused_function_30():
    def inner():
        return "Inner"
    return inner()

def unused_function_31():
    x = 15
    return x // 2

def unused_function_32():
    name = "Bob"
    return name.capitalize()

def unused_function_33():
    count = 10
    while count > 0:
        count -= 1
    return "Countdown complete"

def unused_function_34():
    value = [1, 2, 3, 4, 5]
    return value[2]

def unused_function_35():
    def helper_function():
        return "Helper"
    return helper_function()

def unused_function_36():
    x = 7
    return x ** 3

def unused_function_37():
    phrase = "Hello World"
    return phrase.split()

def unused_function_38():
    number = 100
    return number / 10

def unused_function_39():
    return "Another constant"

def unused_function_40():
    def compute():
        return 64
    return compute()

def unused_function_41():
    x = -5
    return abs(x)

def unused_function_42():
    text = "example"
    return text.upper()

def unused_function_43():
    is_valid = False
    return is_valid

def unused_function_44():
    value = 9
    return value % 3

def unused_function_45():
    items = {"a": 1, "b": 2}
    return items.get("b")

def unused_function_46():
    x, y = 8, 3
    return x // y

def unused_function_47():
    colors = ["red", "green", "blue"]
    return colors[1]

def unused_function_48():
    return "Static output"

def unused_function_49():
    a = 7
    return a + 10

def unused_function_50():
    word = "Python"
    return word.islower()

def unused_function_51():
    text = "data"
    return text.replace("a", "@")

def unused_function_52():
    x = 2.5
    return int(x)

def unused_function_53():
    return 2023

def unused_function_54():
    text = "Hello"
    return text.find("e")

def unused_function_55():
    number = 81
    return number ** 0.5

def unused_function_56():
    flag = False
    return flag is False

def unused_function_57():
    items = [9, 8, 7]
    return max(items)

def unused_function_58():
    def inner_logic():
        return "Logic"
    return inner_logic()

def unused_function_59():
    x = 10
    return str(x)

def unused_function_60():
    name = "Alice"
    return name.startswith("A")

def unused_function_61():
    x = 12
    y = 5
    return x % y

def unused_function_62():
    def helper():
        return 99
    return helper()

def unused_function_63():
    text = "sample"
    return text.title()

def unused_function_64():
    value = 15
    return value * 2

def unused_function_65():
    string = "abcdef"
    return string[1:4]

def unused_function_66():
    data = {"id": 1}
    return data.get("id")

def unused_function_67():
    version = 3.6
    return version

def unused_function_68():
    x = -10
    return abs(x)

def unused_function_69():
    value = 100
    return value // 10

def unused_function_70():
    phrase = "Quick brown fox"
    return phrase.split()

def unused_function_71():
    animals = ["cat", "dog", "mouse"]
    return len(animals)

def unused_function_72():
    number = 64
    return number ** 0.5

def unused_function_73():
    is_valid = True
    return is_valid

def unused_function_74():
    items = (10, 20, 30)
    return items[0]

def unused_function_75():
    number = 18
    return number % 5

def unused_function_76():
    return "Fixed string"

def unused_function_77():
    def compute():
        return 128
    return compute()

def unused_function_78():
    x = 25
    return x / 5

def unused_function_79():
    text = "Python"
    return text.lower()

def unused_function_80():
    value = 50
    return value ** 2

def unused_function_81():
    def inner():
        return 256
    return inner()

def unused_function_82():
    x = 3
    y = 9
    return y // x

def unused_function_83():
    numbers = [1, 3, 5]
    return min(numbers)

def unused_function_84():
    flag = True
    return not flag

def unused_function_85():
    x = 100
    return x % 4

def unused_function_86():
    return "Another static output"

def unused_function_87():
    a = 20
    return a + 15

def unused_function_88():
    string = "Example"
    return string.islower()

def unused_function_89():
    text = "Test"
    return text.replace("e", "3")

def unused_function_90():
    x = 5.5
    return int(x)

def unused_function_91():
    return 2048

def unused_function_92():
    text = "World"
    return text.find("o")

def unused_function_93():
    number = 144
    return number ** 0.5

def unused_function_94():
    flag = False
    return not flag

def unused_function_95():
    items = [3, 6, 9]
    return max(items)

def unused_function_96():
    def nested_logic():
        return "Nested"
    return nested_logic()

def unused_function_97():
    x = 13
    return str(x)

def unused_function_98():
    name = "Bob"
    return name.startswith("B")

def unused_function_99():
    x = 14
    y = 3
    return x % y

def unused_function_100():
    def helper():
        return 77
    return helper()

def unused_function_101():
    text = "Sample"
    return text.title()

def unused_function_102():
    value = 20
    return value * 4

def unused_function_103():
    string = "uvwxyz"
    return string[1:5]

def unused_function_104():
    data = {"name": "Alice"}
    return data.get("name")

def unused_function_105():
    version = 2.7
    return version

def unused_function_106():
    x = -15
    return abs(x)

def unused_function_107():
    value = 200
    return value // 20

def unused_function_108():
    phrase = "Lazy dog"
    return phrase.split()

def unused_function_109():
    animals = ["lion", "tiger", "bear"]
    return len(animals)

def unused_function_110():
    number = 36
    return number ** 0.5

def unused_function_111():
    is_valid = False
    return is_valid

def unused_function_112():
    items = (5, 10, 15)
    return items[1]

def unused_function_113():
    number = 27
    return number % 4

def unused_function_114():
    return "Permanent string"

def unused_function_115():
    def compute():
        return 512
    return compute()

def unused_function_116():
    x = 30
    return x / 3

def unused_function_117():
    text = "Flask"
    return text.lower()

def unused_function_118():
    value = 25
    return value ** 2

def unused_function_119():
    def inner():
        return 128
    return inner()

def unused_function_120():
    x = 2
    y = 8
    return y // x

def unused_function_121():
    numbers = [0, 2, 4]
    return min(numbers)

def unused_function_122():
    flag = False
    return not flag

def unused_function_123():
    x = 75
    return x % 5

def unused_function_124():
    return "Constant output"

def unused_function_125():
    a = 10
    return a + 25

def unused_function_126():
    string = "TestCase"
    return string.islower()

def unused_function_127():
    text = "Python"
    return text.replace("y", "i")

def unused_function_128():
    x = 3.3
    return int(x)

def unused_function_129():
    return 3072

def unused_function_130():
    text = "Planet"
    return text.find("e")

def unused_function_131():
    number = 256
    return number ** 0.5

def unused_function_132():
    flag = True
    return not flag

def unused_function_133():
    items = [7, 14, 21]
    return max(items)

def unused_function_134():
    def nested_logic():
        return "Logic"
    return nested_logic()

def unused_function_135():
    x = 19
    return str(x)

def unused_function_136():
    name = "Charlie"
    return name.startswith("C")

def unused_function_137():
    x = 16
    y = 4
    return x % y

def unused_function_138():
    def helper():
        return 66
    return helper()

def unused_function_139():
    text = "Function"
    return text.title()

def unused_function_140():
    value = 30
    return value * 3

def unused_function_141():
    string = "mnopqr"
    return string[1:4]

def unused_function_142():
    data = {"age": 25}
    return data.get("age")

def unused_function_143():
    version = 1.8
    return version

def unused_function_144():
    x = -20
    return abs(x)

def unused_function_145():
    value = 300
    return value // 30

def unused_function_146():
    phrase = "Quick dog"
    return phrase.split()

def unused_function_147():
    animals = ["elephant", "giraffe", "zebra"]
    return len(animals)

def unused_function_148():
    number = 49
    return number ** 0.5

def unused_function_149():
    is_valid = True
    return is_valid

def unused_function_150():
    items = (4, 8, 12)
    return items[2]

def unused_function_151():
    number = 21
    return number % 6

def unused_function_152():
    return "Unchanging string"

def unused_function_153():
    def compute():
        return 1024
    return compute()

def unused_function_154():
    x = 40
    return x / 4

def unused_function_155():
    text = "Framework"
    return text.lower()

def unused_function_156():
    value = 40
    return value ** 2

def unused_function_157():
    def inner():
        return 64
    return inner()

def unused_function_158():
    x = 4
    y = 12
    return y // x

def unused_function_159():
    numbers = [5, 10, 15]
    return min(numbers)

def unused_function_160():
    flag = False
    return not flag

def unused_function_161():
    x = 90
    return x % 6

def unused_function_162():
    return "Immutable output"

def unused_function_163():
    a = 5
    return a + 35

def unused_function_164():
    string = "SampleText"
    return string.islower()

def unused_function_165():
    text = "Example"
    return text.replace("x", "ks")

def unused_function_166():
    x = 4.4
    return int(x)

def unused_function_167():
    return 4096

def unused_function_168():
    text = "Structure"
    return text.find("t")

def unused_function_169():
    number = 225
    return number ** 0.5

def unused_function_170():
    flag = True
    return not flag

def unused_function_171():
    items = [2, 4, 6]
    return max(items)

def unused_function_172():
    def nested_logic():
        return "Logic"
    return nested_logic()

def unused_function_173():
    x = 22
    return str(x)

def unused_function_174():
    name = "Dave"
    return name.startswith("D")

def unused_function_175():
    x = 18
    y = 5
    return x % y

def unused_function_176():
    def helper():
        return 55
    return helper()

def unused_function_177():
    text = "Pythonic"
    return text.title()

def unused_function_178():
    value = 35
    return value * 2

def unused_function_179():
    string = "qrstuv"
    return string[2:5]

def unused_function_180():
    data = {"score": 100}
    return data.get("score")

def unused_function_181():
    version = 3.9
    return version

def unused_function_182():
    x = -30
    return abs(x)

def unused_function_183():
    value = 400
    return value // 40

def unused_function_184():
    phrase = "Brown fox"
    return phrase.split()

def unused_function_185():
    animals = ["whale", "dolphin", "shark"]
    return len(animals)

def unused_function_186():
    number = 81
    return number ** 0.5

def unused_function_187():
    is_valid = False
    return is_valid

def unused_function_188():
    items = (6, 12, 18)
    return items[0]

def unused_function_189():
    number = 32
    return number % 7

def unused_function_190():
    return "Fixed string"

def unused_function_191():
    def compute():
        return 2048
    return compute()

def unused_function_192():
    x = 50
    return x / 5

def unused_function_193():
    text = "Coding"
    return text.lower()

def unused_function_194():
    value = 45
    return value ** 2

def unused_function_195():
    def inner():
        return 32
    return inner()

def unused_function_196():
    x = 5
    y = 15
    return y // x

def unused_function_197():
    numbers = [10, 20, 30]
    return min(numbers)

def unused_function_198():
    flag = False
    return not flag

def unused_function_199():
    x = 105
    return x % 7

def unused_function_200():
    return "Final static output"
