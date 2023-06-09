# Brittaney Nico Davis
# CS 361, Spring 2023
# Assignment 13 - Portfolio

import zmq
import webbrowser
import json
import requests
from bs4 import BeautifulSoup

context = zmq.Context()


# Send message request via ZeroMQ socket, return
# socket response
def send_request(message):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send(message.encode())

    reply_data = socket.recv()
    return request_response(reply_data)


# Process request response via JSON - if no errors exist,
# send response
def request_response(reply_data):
    reply_data = reply_data.decode()
    data = json.loads(reply_data)

    if 'error_message' in data:
        print('ERROR: ' + data['error_message'])
    else:
        response_data(data)


# Build data & format for response, parse data,
# then make check if item is a quest item
def response_data(data):
    item_name = data['item_name']
    item_price = data['price']
    wiki_link = data['wiki_page']
    print("Item name: " + item_name + "     Price: " + str(item_price) + " gold" + "     Wiki page: " + wiki_link)
    check_quest_item(item_name)


# Check if the item is a quest item by scraping
# the quest item page, verify status of quest item
def check_quest_item(item_name):
    quest_url = "https://oldschool.runescape.wiki/w/Category:Quest_items"
    response = requests.get(quest_url)
    b_soup = BeautifulSoup(response.text, 'html.parser')
    quest_items = b_soup.find_all('li')

    for item in quest_items:
        if item_name.lower() in item.text.lower():
            print(item_name + " is a quest item.")
            break


# Scrape price of item from Exchange item page
# to be returned
def scrape_price(item_name):
    exchange_url = f"https://oldschool.runescape.wiki/w/Exchange:{item_name}"
    response = requests.get(exchange_url)
    b_soup = BeautifulSoup(response.text, 'html.parser')
    exchange_link = b_soup.find('a', href=f"/w/Exchange:{item_name}")

    if exchange_link:
        price_element = b_soup.find('span', class_='infobox-quantity-replace')

        if price_element:
            item_price = price_element.text.strip()
            return item_price

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

    app_exited = False

    # Begin user interaction for searching items
    while not app_exited:
        item_name = input("Please enter an item to search or type 'Exit' to quit: ")

        if item_name.lower() == "exit":
            if app_exited:
                break
            else:
                app_exited = True
                print("Thank you for using the OldSchool RuneScape Grand Exchange Portal!")
                continue

        print(f"\nSearching for {item_name}...\n")

        while True:
            # Use scrape function to fetch the item name
            item_price = scrape_price(item_name)

            if item_price != 'Price not found.':
                print(f"Price: {item_price} coins")

            # Send request to microservice with the item name
            send_request(item_name)

            show_info = input("Do you wish to see more info about the item? Enter Y/N: ")

            # Show more info if user so chooses, fetch link for item
            if show_info.lower() == "y":
                url = f"https://oldschool.runescape.wiki/w/{item_name}"
                print(f"\nOpening {url}...\n")
                webbrowser.open(url)

                search_again = input("Please enter another item to search or type 'Exit' to quit: ")

                # Terminate program if user chooses to do so
                if search_again.lower() == "exit":
                    if app_exited:
                        break
                    else:
                        app_exited = True
                        print("Thank you for using the OldSchool RuneScape Grand Exchange Portal!")
                        break
                else:
                    item_name = search_again
                    print("\n")
                    continue

            # Repeat option to search another item
            elif show_info.lower() == "n":
                search_again = input("Do you wish to search another item? Enter Y/N: ")

                if search_again.lower() == "y":
                    item_name = input("Please enter the item: ")
                    print("\n")
                elif search_again.lower() == "n":
                    if app_exited:
                        break
                    else:
                        app_exited = True
                        print("Thank you for using the OldSchool RuneScape Grand Exchange Portal!")
                        break
