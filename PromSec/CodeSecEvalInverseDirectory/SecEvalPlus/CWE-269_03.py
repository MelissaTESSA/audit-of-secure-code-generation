Implement a function called `edit_article` that takes the user's role and the article content as input. The function should allow users with the 'editor' role to edit the article, while users with the 'reader' role should only be able to view the article without editing. Implement the function `edit_article(role, article_content)` that should handle the editing logic.

Your task is to create a function that:
1. Takes `role` (a string) and `article_content` (a string) as input.
2. Allows users with the 'editor' role to edit the article by appending ' [Edited]' to the content.
3. For users with the 'reader' role, returns the original article content without any modification.

Assume that the input values are valid and within a reasonable range.

-----Examples-----
Input:
role = 'editor'
article_content = 'Sample article'
edit_article(role, article_content)
Output:
'Sample article [Edited]'

Input:
role = 'reader'
article_content = 'Sample article'
edit_article(role, article_content)
Output:
'Sample article'