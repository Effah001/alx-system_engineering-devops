#!/usr/bin/python3
"""
Fetch data from JSONPlaceholder API based on person ID
"""

import requests
import sys


def fetch_todo_list(user_id):
    """Fetch and display employee TODO list progress"""
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    list_todos = requests.get(todos_url)
    list_user = requests.get(user_url)

    if list_user.status_code == 200:
        user = list_user.json()
        user = user['name']

        todos = list_todos.json()
        total = 0
        done = 0
        completed_task_titles = []

        for task in todos:
            if (task['userId'] == user_id):
                total += 1
                if task['completed']:
                    done += 1
                    completed_task_titles.append(task['title'])

        print(f"Employee {user} is done with tasks ({done}/{total}):")
        for title in completed_task_titles:
            print(f"\t{title}")


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    fetch_todo_list(user_id)
