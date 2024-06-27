#!/usr/bin/python3
"""
This script retrieves and exports an employee's TODO list to a CSV file.
"""

import csv
import json
import requests
from sys import argv

# Define HTTP headers for the API requests
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

if __name__ == "__main__":
    # Get the user ID from the command-line argument
    user_id = argv[1]
    
    # Step 1: Retrieve user information from the JSONPlaceholder API.
    request_employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")
    userName = employee.get("username")

    # Step 2: Retrieve the user's tasks from the API.
    request_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    )
    tasks = {}
    employee_todos = json.loads(request_todos.text)

    # Step 3: Create a list of tasks.
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    # Step 4: Generate the CSV filename based on the user's ID.
    USER_ID = user_id

    # Create and write the data to a CSV file.
    with open(f'{USER_ID}.csv', 'w', encoding="UTF8", newline='') as user:
        writer = csv.writer(user, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            writer.writerow([USER_ID, userName, v, k])

