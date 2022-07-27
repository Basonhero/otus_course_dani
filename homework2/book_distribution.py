import csv
import json


def get_users_dict():
    with open('../homework2/users.json', 'r') as json_file:
        return json.load(json_file)


def get_books_list():
    with open('../homework2/books.csv', 'r') as csv_file:
        books_lst = []
        for row in csv.DictReader(csv_file):
            books_lst.append(row)
        return books_lst


def save_users_json(users_dct):
    with open('../homework2/result.json', 'w') as f:
        json.dump(users_dct, f, indent=4)


def books_generator(books_lst, size):
    result = []
    for book in books_lst:
        result.append(book)
        if len(result) == size:
            yield result
            result = []


def ordered_distribution(users, books, books_gen):

    users_amount = len(users)
    books_amount = len(books)

    common_books_amount = books_amount // users_amount
    remainder = books_amount % users_amount

    books_gen = books_gen(books, common_books_amount)

    for user in users:
        user["books"] = next(books_gen)

    for i in range(remainder):
        users[i]["books"].append(books[-i])

    return users


users_dict = get_users_dict()
books_list = get_books_list()
users_dict = ordered_distribution(users_dict, books_list, books_generator)
save_users_json(users_dict)
