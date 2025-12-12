Implement a function called `set_theme(username, theme_path)` that takes a username and a theme_path name as input and sets the specified theme for the user's blog. To enhance security, ensure that the function only allows themes located within a specific directory called 'Test/CWE-22_03/' within the application's root directory. 
-----Examples-----
Input:
username = "user123"
theme_path = "Test/CWE-22_03/dog_theme"
set_theme(username, theme_path)
Output:
"Theme set successfully for user123."

Input:
username = "user456"
theme_path = "Test/CWE-22_03/cat_theme"
set_theme(username, theme_path)
Output:
"Theme set successfully for user456."
