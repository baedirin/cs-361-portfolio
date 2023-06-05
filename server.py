# Brittaney Nico Davis
# CS 361, Spring 2023
# Assignment 13 - Portfolio

import zmq
import requests
import json
import multiprocessing


# Utilizing a ZeroMQ socket, initialize the microservice
def run_microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = receive_request(socket)
        result = fetch_data_from_api(message)

        if handle_error(result, socket):
            continue

        item_price = result[message]['price']
        send_response(socket, message, item_price)


# Receive requests from client, confirm via message
def receive_request(socket):
    message = socket.recv()
    message = message.decode()
    print("Received request: %s" % message)
    return message


# Fetch data from API, return JSON
def fetch_data_from_api(item_name):
    response_API = requests.get('https://api.weirdgloop.org/exchange/history/osrs/latest?name=' + item_name + '&lang=en')
    data = response_API.text
    return json.loads(data)


# Send response with search information for user
def send_response(socket, message, item_price):
    wiki_lookup = message.replace(" ", '_')
    reply_back = {'item_name': message, 'price': item_price,
                  'wiki_page': 'https://oldschool.runescape.wiki/w/Exchange:' + wiki_lookup}
    json_data = json.dumps(reply_back)
    socket.send(bytes(json_data, encoding="utf-8"))


# Handle errors for untradeable items
def handle_error(result, socket):
    if 'error' in result:
        if result['error'] == 'Item(s) not found in the database':
            error_reply = {'error_message': 'Item is not tradeable'}
            error_reply = json.dumps(error_reply)
            socket.send(bytes(error_reply, encoding="utf-8"))
            return True
    return False


# Run concurrently with client.py via multiprocessing
if __name__ == '__main__':
    microservice_process = multiprocessing.Process(target=run_microservice)
    microservice_process.start()