#!/usr/bin/python3
"""
Gather data from an API and export to JSON format
"""
import json
import requests
import sys


def main():
    user_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users" + f'/{user_id}'
    todos_list = requests.get(todos_url)
    user_list = requests.get(user_url)

    if (user_list.status_code == 200):
        user = user_list.json()
        username = user['username']
        todos = todos_list.json()
        all_task = []
        for task in todos:
            if (task['userId'] == user_id):
                temp = {}
                temp['task'] = task['title']
                temp['completed'] = task['completed']
                temp['username'] = username
                all_task.append(temp)
        with open(f"{user_id}.json", "w")as f:
            json.dump({user_id: all_task}, f)


if __name__ == '__main__':
    main()

