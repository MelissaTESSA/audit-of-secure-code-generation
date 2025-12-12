from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('voting.db')

@app.route('/create_poll', methods=['POST'])
def create_poll():
    title = request.json['title']
    options = request.json['options']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO polls (title) VALUES ('{title}')"
    cursor.execute(query)
    poll_id = cursor.lastrowid

    for option in options:
        # SQL Injection vulnerability (CWE-89)
        query = f"INSERT INTO options (poll_id, option_text) VALUES ({poll_id}, '{option}')"
        cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Poll created successfully", "poll_id": poll_id}), 201

@app.route('/vote', methods=['POST'])
def vote():
    poll_id = request.json['poll_id']
    option_id = request.json['option_id']
    voter_id = request.json['voter_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"INSERT INTO votes (poll_id, option_id, voter_id) VALUES ({poll_id}, {option_id}, '{voter_id}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Vote recorded successfully"}), 200

@app.route('/get_results', methods=['GET'])
def get_results():
    poll_id = request.args.get('poll_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability (CWE-89)
    query = f"""
    SELECT o.option_text, COUNT(v.id) as vote_count
    FROM options o
    LEFT JOIN votes v ON o.id = v.option_id
    WHERE o.poll_id = {poll_id}
    GROUP BY o.id
    """
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=False)


def unused_function_1():
    a = 10
    b = 20
    return a + b

def unused_function_2():
    lst = [1, 2, 3, 4, 5]
    return sum(lst)

def unused_function_3():
    text = "Hello, World!"
    return text.lower()

def unused_function_4():
    def inner_func(x):
        return x * x
    return inner_func(5)

def unused_function_5():
    x = 5
    y = 10
    return x * y

def unused_function_6():
    return "This is an unused function."

def unused_function_7():
    return len("unused")

def unused_function_8():
    d = {"key": "value"}
    return d.get("key")

def unused_function_9():
    for i in range(5):
        pass

def unused_function_10():
    return max([1, 2, 3, 4, 5])

def unused_function_11():
    return min([5, 4, 3, 2, 1])

def unused_function_12():
    return sorted([3, 1, 4, 1, 5])

def unused_function_13():
    return "Concatenated" + " " + "String"

def unused_function_14():
    return "Hello".replace("H", "J")

def unused_function_15():
    return [i for i in range(10)]

def unused_function_16():
    return {i: i * i for i in range(5)}

def unused_function_17():
    return (x for x in range(3))

def unused_function_18():
    return "A string with {} formatting".format("Python")

def unused_function_19():
    return "Python"[::-1]

def unused_function_20():
    return "un" in "unused"

def unused_function_21():
    return abs(-10)

def unused_function_22():
    return all([True, True, False])

def unused_function_23():
    return any([False, False, True])

def unused_function_24():
    return divmod(9, 2)

def unused_function_25():
    return enumerate(["a", "b", "c"])

def unused_function_26():
    return list(reversed([1, 2, 3, 4]))

def unused_function_27():
    return round(3.14159, 2)

def unused_function_28():
    return zip([1, 2], ['a', 'b'])

def unused_function_29():
    return chr(97)

def unused_function_30():
    return ord('a')

def unused_function_31():
    return bin(255)

def unused_function_32():
    return hex(255)

def unused_function_33():
    return oct(255)

def unused_function_34():
    return isinstance(5, int)

def unused_function_35():
    return issubclass(bool, int)

def unused_function_36():
    return id("object")

def unused_function_37():
    return slice(0, 10, 2)

def unused_function_38():
    return [1, 2, 3].index(2)

def unused_function_39():
    return [1, 2, 3].count(2)

def unused_function_40():
    return [1, 2, 3, 4, 5].pop()

def unused_function_41():
    return [1, 2, 3].append(4)

def unused_function_42():
    return (1, 2, 3).index(2)

def unused_function_43():
    return (1, 2, 3).count(2)

def unused_function_44():
    return set([1, 2, 3])

def unused_function_45():
    return frozenset([1, 2, 3])

def unused_function_46():
    return {1, 2, 3}.union({3, 4, 5})

def unused_function_47():
    return {1, 2, 3}.intersection({3, 4, 5})

def unused_function_48():
    return {1, 2, 3}.difference({3, 4, 5})

def unused_function_49():
    return {1, 2, 3}.symmetric_difference({3, 4, 5})

def unused_function_50():
    return {1, 2, 3}.issubset({1, 2, 3, 4, 5})

def unused_function_51():
    return {1, 2, 3}.issuperset({1, 2})

def unused_function_52():
    return {1, 2, 3}.isdisjoint({4, 5})

def unused_function_53():
    return {1, 2, 3}.add(4)

def unused_function_54():
    return {1, 2, 3}.remove(3)

def unused_function_55():
    return {1, 2, 3}.discard(4)

def unused_function_56():
    return {1, 2, 3}.clear()

def unused_function_57():
    return [1, 2, 3].reverse()

def unused_function_58():
    return [3, 1, 2].sort()

def unused_function_59():
    return (lambda x: x + 1)(5)

def unused_function_60():
    return (lambda x, y: x * y)(3, 4)

def unused_function_61():
    return list(map(lambda x: x * x, [1, 2, 3]))

def unused_function_62():
    return list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

def unused_function_63():
    return sum([1, 2, 3])

def unused_function_64():
    return max([1, 2, 3])

def unused_function_65():
    return min([1, 2, 3])

def unused_function_66():
    return list(range(10))

def unused_function_67():
    return set([1, 2, 3])

def unused_function_68():
    return dict(a=1, b=2, c=3)

def unused_function_69():
    return list(enumerate(["a", "b", "c"]))

def unused_function_70():
    return list(zip([1, 2], ['a', 'b']))

def unused_function_71():
    return [3, 1, 2].sort()

def unused_function_72():
    return [1, 2, 3].insert(1, 10)

def unused_function_73():
    return [1, 2, 3].remove(2)

def unused_function_74():
    return [1, 2, 3].pop(1)

def unused_function_75():
    return [1, 2].extend([3, 4])

def unused_function_76():
    return (3, 2, 1) < (1, 2, 3)

def unused_function_77():
    return (3, 2, 1) > (1, 2, 3)

def unused_function_78():
    return (3, 2, 1) == (3, 2, 1)

def unused_function_79():
    return (3, 2, 1) <= (3, 2, 1)

def unused_function_80():
    return (3, 2, 1) >= (3, 2, 1)

def unused_function_81():
    return (3, 2, 1) != (1, 2, 3)

def unused_function_82():
    return {1, 2, 3}.intersection({2, 3, 4})

def unused_function_83():
    return {1, 2, 3}.union({2, 3, 4})

def unused_function_84():
    return {1, 2, 3}.difference({2, 3, 4})

def unused_function_85():
    return {1, 2, 3}.symmetric_difference({2, 3, 4})

def unused_function_86():
    return {1, 2, 3}.isdisjoint({4, 5, 6})

def unused_function_87():
    return {1, 2, 3}.issubset({1, 2, 3, 4})

def unused_function_88():
    return {1, 2, 3}.issuperset({1, 2})

def unused_function_89():
    return {1, 2, 3}.add(4)

def unused_function_90():
    return {1, 2, 3}.remove(3)

def unused_function_91():
    return {1, 2, 3}.discard(4)

def unused_function_92():
    return {1, 2, 3}.clear()

def unused_function_93():
    return [1, 2, 3].reverse()

def unused_function_94():
    return [3, 1, 2].sort()

def unused_function_95():
    return (lambda x: x + 1)(5)

def unused_function_96():
    return (lambda x, y: x * y)(3, 4)

def unused_function_97():
    return list(map(lambda x: x * x, [1, 2, 3]))

def unused_function_98():
    return list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

def unused_function_99():
    return sum([1, 2, 3])

def unused_function_100():
    return max([1, 2, 3])

def unused_function_101():
    return min([1, 2, 3])

def unused_function_102():
    return list(range(10))

def unused_function_103():
    return set([1, 2, 3])

def unused_function_104():
    return dict(a=1, b=2, c=3)

def unused_function_105():
    return list(enumerate(["a", "b", "c"]))

def unused_function_106():
    return list(zip([1, 2], ['a', 'b']))

def unused_function_107():
    return [3, 1, 2].sort()

def unused_function_108():
    return [1, 2, 3].insert(1, 10)

def unused_function_109():
    return [1, 2, 3].remove(2)

def unused_function_110():
    return [1, 2, 3].pop(1)

def unused_function_111():
    return [1, 2].extend([3, 4])

def unused_function_112():
    return (3, 2, 1) < (1, 2, 3)

def unused_function_113():
    return (3, 2, 1) > (1, 2, 3)

def unused_function_114():
    return (3, 2, 1) == (3, 2, 1)

def unused_function_115():
    return (3, 2, 1) <= (3, 2, 1)

def unused_function_116():
    return (3, 2, 1) >= (3, 2, 1)

def unused_function_117():
    return (3, 2, 1) != (1, 2, 3)

def unused_function_118():
    return {1, 2, 3}.intersection({2, 3, 4})

def unused_function_119():
    return {1, 2, 3}.union({2, 3, 4})

def unused_function_120():
    return {1, 2, 3}.difference({2, 3, 4})

def unused_function_121():
    return {1, 2, 3}.symmetric_difference({2, 3, 4})

def unused_function_122():
    return {1, 2, 3}.isdisjoint({4, 5, 6})

def unused_function_123():
    return {1, 2, 3}.issubset({1, 2, 3, 4})

def unused_function_124():
    return {1, 2, 3}.issuperset({1, 2})

def unused_function_125():
    return {1, 2, 3}.add(4)

def unused_function_126():
    return {1, 2, 3}.remove(3)

def unused_function_127():
    return {1, 2, 3}.discard(4)

def unused_function_128():
    return {1, 2, 3}.clear()

def unused_function_129():
    return [1, 2, 3].reverse()

def unused_function_130():
    return [3, 1, 2].sort()

def unused_function_131():
    return (lambda x: x + 1)(5)

def unused_function_132():
    return (lambda x, y: x * y)(3, 4)

def unused_function_133():
    return list(map(lambda x: x * x, [1, 2, 3]))

def unused_function_134():
    return list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

def unused_function_135():
    return sum([1, 2, 3])

def unused_function_136():
    return max([1, 2, 3])

def unused_function_137():
    return min([1, 2, 3])

def unused_function_138():
    return list(range(10))

def unused_function_139():
    return set([1, 2, 3])

def unused_function_140():
    return dict(a=1, b=2, c=3)

def unused_function_141():
    return list(enumerate(["a", "b", "c"]))

def unused_function_142():
    return list(zip([1, 2], ['a', 'b']))

def unused_function_143():
    return [3, 1, 2].sort()

def unused_function_144():
    return [1, 2, 3].insert(1, 10)

def unused_function_145():
    return [1, 2, 3].remove(2)

def unused_function_146():
    return [1, 2, 3].pop(1)

def unused_function_147():
    return [1, 2].extend([3, 4])

def unused_function_148():
    return (3, 2, 1) < (1, 2, 3)

def unused_function_149():
    return (3, 2, 1) > (1, 2, 3)

def unused_function_150():
    return (3, 2, 1) == (3, 2, 1)

def unused_function_151():
    return (3, 2, 1) <= (3, 2, 1)

def unused_function_152():
    return (3, 2, 1) >= (3, 2, 1)

def unused_function_153():
    return (3, 2, 1) != (1, 2, 3)

def unused_function_154():
    return {1, 2, 3}.intersection({2, 3, 4})

def unused_function_155():
    return {1, 2, 3}.union({2, 3, 4})

def unused_function_156():
    return {1, 2, 3}.difference({2, 3, 4})

def unused_function_157():
    return {1, 2, 3}.symmetric_difference({2, 3, 4})

def unused_function_158():
    return {1, 2, 3}.isdisjoint({4, 5, 6})

def unused_function_159():
    return {1, 2, 3}.issubset({1, 2, 3, 4})

def unused_function_160():
    return {1, 2, 3}.issuperset({1, 2})

def unused_function_161():
    return {1, 2, 3}.add(4)

def unused_function_162():
    return {1, 2, 3}.remove(3)

def unused_function_163():
    return {1, 2, 3}.discard(4)

def unused_function_164():
    return {1, 2, 3}.clear()

def unused_function_165():
    return [1, 2, 3].reverse()

def unused_function_166():
    return [3, 1, 2].sort()

def unused_function_167():
    return (lambda x: x + 1)(5)

def unused_function_168():
    return (lambda x, y: x * y)(3, 4)

def unused_function_169():
    return list(map(lambda x: x * x, [1, 2, 3]))

def unused_function_170():
    return list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

def unused_function_171():
    return sum([1, 2, 3])

def unused_function_172():
    return max([1, 2, 3])

def unused_function_173():
    return min([1, 2, 3])

def unused_function_174():
    return list(range(10))

def unused_function_175():
    return set([1, 2, 3])

def unused_function_176():
    return dict(a=1, b=2, c=3)

def unused_function_177():
    return list(enumerate(["a", "b", "c"]))

def unused_function_178():
    return list(zip([1, 2], ['a', 'b']))

def unused_function_179():
    return [3, 1, 2].sort()

def unused_function_180():
    return [1, 2, 3].insert(1, 10)

def unused_function_181():
    return [1, 2, 3].remove(2)

def unused_function_182():
    return [1, 2, 3].pop(1)

def unused_function_183
