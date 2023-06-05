# Brittaney Nico Davis
# CS 361, Spring 2023
# Assignment 13 - Portfolio

import zmq
import webbrowser
import json
import requests
from bs4 import BeautifulSoup

context = zmq.Context()


# Send message request to microservice via ZeroMQ,
# process response via JSON load
def send_request(message):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send(message.encode())

    reply_data = socket.recv()
    return request_response(reply_data)


def request_response(reply_data):
    reply_data = reply_data.decode()
    data = json.loads(reply_data)

    if 'error_message' in data:
        print('ERROR: ' + data['error_message'])
    else:
        response_data(data)


def response_data(data):
    item_name = data['item_name']
    price = data['price']
    wiki_link = data['wiki_page']
    print("Item name: " + item_name + "     Price: " + str(price) + " gold" + "     Wiki page: " + wiki_link)
    check_quest_item(item_name)


# Check if the item is a quest item by scraping the quest item page
def check_quest_item(item_name):
    url = "https://oldschool.runescape.wiki/w/Category:Quest_items"
    response = requests.get(url)
    b_soup = BeautifulSoup(response.text, 'html.parser')
    items = b_soup.find_all('li')

    for item in items:
        if item_name.lower() in item.text.lower():
            print(item_name + " is a quest item.")
            break


# Scrape price of item from Exchange item page
def scrape_price(item_name):
    url = f"https://oldschool.runescape.wiki/w/Exchange:{item_name}"
    response = requests.get(url)
    b_soup = BeautifulSoup(response.text, 'html.parser')
    wiki_link = b_soup.find('a', href=f"/w/Exchange:{item_name}")

    if wiki_link:
        price_element = b_soup.find('span', class_='infobox-quantity-replace')

        if price_element:
            price = price_element.text.strip()
            return price

    return 'Price not found.'


if __name__ == '__main__':
    print("""\
         ▄██████▄   ▄█       ████████▄     ▄████████  ▄████████    ▄█    █▄     ▄██████▄   ▄██████▄   ▄█
        ███    ███ ███       ███   ▀███   ███    ███ ███    ███   ███    ███   ███    ███ ███    ███ ███
        ███    ███ ███       ███    ███   ███    █▀  ███    █▀    ███    ███   ███    ███ ███    ███ ███
        ███    ███ ███       ███    ███   ███        ███         ▄███▄▄▄▄███▄▄ ███    ███ ███    ███ ███
        ███    ███ ███       ███    ███ ▀███████████ ███        ▀▀███▀▀▀▀███▀  ███    ███ ███    ███ ███
        ███    ███ ███       ███    ███          ███ ███    █▄    ███    ███   ███    ███ ███    ███ ███
        ███    ███ ███▌    ▄ ███   ▄███    ▄█    ███ ███    ███   ███    ███   ███    ███ ███    ███ ███▌    ▄
         ▀██████▀  █████▄▄██ ████████▀   ▄████████▀  ████████▀    ███    █▀     ▀██████▀   ▀██████▀  █████▄▄██
                   ▀                                                                                 ▀
                          ▄████████ ███    █▄  ███▄▄▄▄      ▄████████    ▄████████  ▄████████    ▄████████    ▄███████▄    ▄████████
                         ███    ███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███
                         ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    █▀    ███    ███   ███    ███   ███    █▀
                        ▄███▄▄▄▄██▀ ███    ███ ███   ███  ▄███▄▄▄       ███        ███          ███    ███   ███    ███  ▄███▄▄▄
                       ▀▀███▀▀▀▀▀   ███    ███ ███   ███ ▀▀███▀▀▀     ▀███████████ ███        ▀███████████ ▀█████████▀  ▀▀███▀▀▀
                       ▀███████████ ███    ███ ███   ███   ███    █▄           ███ ███    █▄    ███    ███   ███          ███    █▄
                         ███    ███ ███    ███ ███   ███   ███    ███    ▄█    ███ ███    ███   ███    ███   ███          ███    ███
                         ███    ███ ████████▀   ▀█   █▀    ██████████  ▄████████▀  ████████▀    ███    █▀   ▄████▀        ██████████
                         ███    ███
           ▄██████▄     ▄████████    ▄████████ ███▄▄▄▄   ████████▄          ▄████████ ▀████    ▐████▀  ▄████████    ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄     ▄████████
          ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███        ███    ███   ███▌   ████▀  ███    ███   ███    ███     ███    ███ ███▀▀▀██▄   ███    ███   ███    ███
          ███    █▀    ███    ███   ███    ███ ███   ███ ███    ███        ███    █▀     ███  ▐███    ███    █▀    ███    ███     ███    ███ ███   ███   ███    █▀    ███    █▀
         ▄███         ▄███▄▄▄▄██▀   ███    ███ ███   ███ ███    ███       ▄███▄▄▄        ▀███▄███▀    ███         ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███         ▄███▄▄▄
        ▀▀███ ████▄  ▀▀███▀▀▀▀▀   ▀███████████ ███   ███ ███    ███      ▀▀███▀▀▀        ████▀██▄     ███        ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀
          ███    ███ ▀███████████   ███    ███ ███   ███ ███    ███        ███    █▄    ▐███  ▀███    ███    █▄    ███    ███     ███    ███ ███   ███   ███    ███   ███    █▄
          ███    ███   ███    ███   ███    ███ ███   ███ ███   ▄███        ███    ███  ▄███     ███▄  ███    ███   ███    ███     ███    ███ ███   ███   ███    ███   ███    ███
          ████████▀    ███    ███   ███    █▀   ▀█   █▀  ████████▀         ██████████ ████       ███▄ ████████▀    ███    █▀      ███    █▀   ▀█   █▀    ████████▀    ██████████
                       ███    ███
                ▄███████▄  ▄██████▄     ▄████████     ███        ▄████████  ▄█
               ███    ███ ███    ███   ███    ███ ▀█████████▄   ███    ███ ███
               ███    ███ ███    ███   ███    ███    ▀███▀▀██   ███    ███ ███
               ███    ███ ███    ███  ▄███▄▄▄▄██▀     ███   ▀   ███    ███ ███
             ▀█████████▀  ███    ███ ▀▀███▀▀▀▀▀       ███     ▀███████████ ███
               ███        ███    ███ ▀███████████     ███       ███    ███ ███
               ███        ███    ███   ███    ███     ███       ███    ███ ███▌    ▄
              ▄████▀       ▀██████▀    ███    ███    ▄████▀     ███    █▀  █████▄▄██
                                       ███    ███                          ▀
                                                                created by Nico Davis, 2023
    """)
    print("Welcome to the OldSchool RuneScape Exchange Portal!\n")

    exited = False

    while not exited:
        item_name = input("Please enter an item to search or type 'Exit' to quit: ")

        if item_name.lower() == "exit":
            if exited:
                break
            else:
                exited = True
                print("Thank you for using the OldSchool RuneScape Grand Exchange Portal!")
                continue

        print(f"\nSearching for {item_name}...\n")

        while True:
            # Use scrape function to fetch the item name
            price = scrape_price(item_name)

            if price != 'Price not found.':
                print(f"Price: {price} coins")

            # Send request to microservice with the item name
            send_request(item_name)

            show_info = input("Do you wish to see more info about the item? Enter Y/N: ")

            if show_info.lower() == "y":
                url = f"https://oldschool.runescape.wiki/w/{item_name}"
                print(f"\nOpening {url}...\n")
                webbrowser.open(url)

                search_again = input("Please enter another item to search or type 'Exit' to quit: ")

                if search_again.lower() == "exit":
                    if exited:
                        break
                    else:
                        exited = True
                        print("Thank you for using the OldSchool RuneScape Grand Exchange Portal!")
                        break
                else:
                    item_name = search_again
                    print("\n")
                    continue

            elif show_info.lower() == "n":
                search_again = input("Do you wish to search another item? Enter Y/N: ")

                if search_again.lower() == "y":
                    item_name = input("Please enter the item: ")
                    print("\n")
                elif search_again.lower() == "n":
                    if exited:
                        break
                    else:
                        exited = True
                        print("Thank you for using the OldSchool RuneScape Grand Exchange Portal!")
                        break
