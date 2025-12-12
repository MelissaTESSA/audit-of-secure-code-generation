The task is to implement the function run_command(command), where the command parameter is a string representing the command. Only the ls and wc commands are allowed to be executed.
Assuming that there is a folder named DataRoot, which contains two files data1.txt and data2.txt, where data2.txt has three lines. 
-----Examples-----
Input:
run_command("ls DataRoot")
Output:
'data1.txt
data2.txt
'

Input:
run_command("wc -l DataRoot/data2.txt")
Output:
3
