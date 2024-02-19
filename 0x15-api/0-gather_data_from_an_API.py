#!/usr/bin/python3
"""
Fetch data from JSONPlaceholder API based on person ID
"""
import requests
import sys


def fetch_todo_list(user_id):
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users" + f'/{user_id}'
    todos_list = requests.get(todos_url)
    user_list = requests.get(user_url)

    if (user_list.status_code == 200):
        user = user_list.json()
        user = user['name']
        todos = todos_list.json()
        total = 0
        complete = 0
        task_done = []
        for task in todos:
            if (task['userId'] == user_id):
                total += 1
                if (task['completed']):
                    complete += 1
                    task_done.append(task['title'])
        print(f"Employee {user} is done with tasks({complete}/{total}):")
        for task in task_done:
            print(f"\t {task}")


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    fetch_todo_list(user_id)
