#!/usr/bin/python3
"""
     Tte employee ID,will returns all information about the TODO list of this employee.
"""
import requests
import sys


def fetch_employee_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    if user_response.status_code != 200:
        print(f"Error: Could not fetch user data for employee ID {employee_id}")
        return None, None

    user_info = user_response.json()
    employee_name = user_info['name']

    # Fetch todo list for the user
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    if todo_response.status_code != 200:
        print(f"Error: Could not fetch TODO data for employee ID {employee_id}")
        return None, None

    todos = todo_response.json()

    return employee_name, todos


def display_task_progress(employee_name, todos):
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task['completed']]
    total_done_tasks = len(done_tasks)

    # Print task progress
    print(f"Employee {employee_name} is done with tasks({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_name, todos = fetch_employee_data(employee_id)

    if employee_name and todos:
        display_task_progress(employee_name, todos)
