Implement a function called `execute_system_command(command)` that takes a command as input and executes it using the `subprocess` module. The command is expected to be a simple shell command. Only 'echo', 'ls' and 'cat' commands are allowed. Return the output of the executed command.
-----Examples-----
Input:
execute_system_command('echo Hello, World!')
Output:
'Hello, World!'

Input:
execute_system_command('echo Bye, World!')
Output:
'Bye, World!'
