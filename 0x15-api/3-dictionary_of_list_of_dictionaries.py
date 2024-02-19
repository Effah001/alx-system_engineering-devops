#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
import sys


def fetch_user_tasks(user_id):
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_list = requests.get(todos_url)
    user_list = requests.get(user_url)

    if (user_list.status_code == 200):
        user = user_list.json()
        username = user['username']
        todos = todos_list.json()
        user_tasks = []
        for task in todos:
            if (task['userId'] == user_id):
                temp = {}
                temp['username'] = username
                temp['task'] = task['title']
                temp['completed'] = task['completed']
                user_tasks.append(temp)
        return user_tasks


def main():
    all_users_tasks = {}
    for i in range(1, 11):
        all_users_tasks[i] = fetch_user_tasks(i)
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_users_tasks, f)


if __name__ == '__main__':
    main()

