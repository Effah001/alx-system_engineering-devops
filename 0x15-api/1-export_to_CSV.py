#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
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
        user = user['name']
        todos = todos_list.json()

        with open(f"{user_id}.csv", "w") as f:
            fnames = ['user_id', 'username', 'completed', 'title']
            write = csv.DictWriter(f, fieldnames=fnames, quoting=csv.QUOTE_ALL)
            for task in todos:
                if (task['userId'] == user_id):
                    write.writerow({
                        'user_id': str(user_id),
                        'username': str(username),
                        'completed': str(task['completed']),
                        'title': str(task['title'])
                        })


if __name__ == '__main__':
    main()
