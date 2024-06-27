#!/usr/bin/python3

import requests
import sys
import csv

def fetch_employee_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    if user_response.status_code != 200:
        print(f"Error: Could not fetch user data for employee ID {employee_id}")
        return None, None
    
    user_info = user_response.json()
    username = user_info['username']
    
    # Fetch todo list for the user
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    if todo_response.status_code != 200:
        print(f"Error: Could not fetch TODO data for employee ID {employee_id}")
        return None, None
    
    todos = todo_response.json()
    
    return username, todos

def export_to_csv(employee_id, username, todos):
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })
    
    print(f"CSV data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    username, todos = fetch_employee_data(employee_id)
    
    if username and todos:
        export_to_csv(employee_id, username, todos)
