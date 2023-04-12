from MyUser import MyUser
from SpeedUser import SpeedUser
import requests


def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()


def get_user():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()
    return data['results'][0]


def get_user_by_name(name):
    users = get_users()
    for user in users:
        if user['name'] == name:
            return MyUser(user['id'], user['name'], user['username'], user['email'])
        else:
            print('User not found!')
            return None


def get_closest_user(latitude):
    users = get_users()
    closest_diff = None
    closest_user = users[0]
    formatted_latitude = abs(float(latitude))

    for user in users:
        latitude_diff = abs(
            float(user['address']['geo']['lat'])) - formatted_latitude
        if closest_diff is None:
            closest_diff = latitude_diff
        elif closest_diff > latitude_diff:
            closest_diff = latitude_diff
            closest_user = user

    return SpeedUser(closest_user)


def print_users_by_number(number):
    for x in range(number):
        user = get_user()
        print(f'{user["name"]["title"]} {user["name"]["first"]} {user["name"]["last"]}')


username = input("Enter your name please: ")
user = get_user_by_name(username)
if user:
    print(user)


latitude = int(input("Enter your latitude please: "))
closest_user = get_closest_user(latitude)
if closest_user:
    print(closest_user)

print_users_count = int(input("How many times to print a user? (1-99) "))
print_users_by_number(print_users_count)
