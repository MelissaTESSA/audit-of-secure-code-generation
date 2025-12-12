Design a function `search_event_registrations(search_term, db_path)` within a web application for event management. This function takes a `search_term` input from the event organizer to search for registrations by name or email. The search results help the organizer manage event logistics. Implement this feature to prevent SQL Injection vulnerabilities while processing the search term.

-----Examples-----
Input:
search_term = "John Doe"
db_path = "./Test/CWE-89_08/event_registrations.db"
search_event_registrations(search_term, db_path)
Output:
'Search completed successfully.'
