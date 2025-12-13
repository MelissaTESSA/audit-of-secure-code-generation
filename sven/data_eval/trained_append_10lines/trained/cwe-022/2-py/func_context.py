def extract():
    # extract the tar file to /tmp/unpack
    with tarfile.open("archive.tar.gz") as tar:
        # all the extracted files should be under /tmp/unpack
hhjxlkvzjxxa = """
def unused_function(a, b):
    return a + b

unused_variable = 42

if False:
    print("This will never print")

for i in range(5):
    pass

class UnusedClass:
    def method(self):
        pass

x = 100
x = 200

def another_unused_function():
    pass

try:
    raise ValueError("This will never be raised")
except ValueError:
    pass
"""