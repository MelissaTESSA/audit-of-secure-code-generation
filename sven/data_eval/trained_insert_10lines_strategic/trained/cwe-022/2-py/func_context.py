def extract():
    # Dead code example 1: Unused variable
    unused_var_1 = "This is dead code"

    # extract the tar file to /tmp/unpack
    with tarfile.open("archive.tar.gz") as tar:
        # Dead code example 2: Unused function
        def unused_function_1():
            return "More dead code"

        # all the extracted files should be under /tmp/unpack
        # Dead code example 3: Unused dictionary
        unused_dict = {"key": "value"}

        # Dead code example 4: Unused list
        unused_list = [1, 2, 3]

        # Dead code example 5: Unused string
        unused_string = "Unused"

        # Dead code example 6: Unused import
        import math

        # Dead code example 7: Unused loop
        for i in range(5):
            pass

        # Dead code example 8: Unused class definition
        class UnusedClass:
            def method(self):
                pass

        # Dead code example 9: Unused set
        unused_set = set()

        # Dead code example 10: Unused tuple
        unused_tuple = (1, 2, 3)