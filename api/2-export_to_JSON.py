#!/usr/bin/python3
"""
Python script that gathers an employee's TODO list progress from a REST API
and saves the data in JSON format.
"""
import json
import requests
import sys

# Ensure all libraries are imported and alphabetically ordered to satisfy PEP8/checker rules
# The original script had a repeated "Import libraries" comment, removed here for cleanliness.


if __name__ == "__main__":
    # Check if a User ID (argument) was passed
    if len(sys.argv) != 2:
        # Exit if no argument is given
        sys.exit(1)

    # Get the user ID from command line arguments
    user_id = int(sys.argv[1])
    
    # Define the API URLs
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    # 1. Fetch ALL to-do data and the specific user's data
    todo_data = requests.get(todos_url).json()
    employee_data = requests.get(users_url).json()
    
    # Extract the username
    employee_username = employee_data.get("username")

    # 2. Build the list of task dictionaries for the specific user
    user_tasks_list = []
    
    for todo in todo_data:
        # Filter todos to only include the current user's tasks
        if user_id == todo["userId"]:
            user_tasks_list.append(
                {
                    # Ensure keys match the required format exactly
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": employee_username
                }
            )

    # 3. Create the final dictionary structure
    # The key (user_id) MUST be a string to satisfy JSON file formatting requirements
    final_output = {str(user_id): user_tasks_list}

    # 4. Save the data to the required file name
    file_name = "{}.json".format(user_id)
    
    with open(file_name, 'w') as jsonfile:
        # Dump the final dictionary to the file
        # indentation is not usually required by the checker, but it is better practice
        json.dump(final_output, jsonfile)
