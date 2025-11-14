#!/usr/bin/python3
"""
Python script that gathers an employee's TODO list progress from a REST API
and saves the data in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    # 1. Fetch data
    todo_data = requests.get(todos_url).json()
    employee_data = requests.get(users_url).json()

    # Extract the username
    employee_username = employee_data.get("username")

    # 2. Build the list of task dictionaries
    user_tasks_list = []

    for todo in todo_data:
        # Filter todos
        if user_id == todo["userId"]:
            user_tasks_list.append(
                {
                    # Ensure keys match required format
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": employee_username
                }
            )

    # 3. Create the final dictionary structure with a string key
    final_output = {str(user_id): user_tasks_list}

    # 4. Save the data to the required file name
    file_name = "{}.json".format(user_id)

    with open(file_name, 'w') as jsonfile:
        json.dump(final_output, jsonfile)
