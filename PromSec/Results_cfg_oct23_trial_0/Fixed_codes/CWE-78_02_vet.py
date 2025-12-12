import subprocess

def count_lines(filename):
    try:
        result = subprocess.run(['wc', '-l', filename], capture_output=True, text=True)
        count = int(result.stdout.split()[0])
        return count
    except:
        return "Error"

print(count_lines("example1.txt"))