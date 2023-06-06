# OldSchool RuneScape Exchange Portal

Thanks for your interest in The OldSchool RuneScape (OSRS) Exchange Portal! This application was created to optimize the use of the Grand Exchange during gaming sessions. A user can tab from the game to this application and easily view an item's price, the OSRS Wiki link for the item, and the OSRS Exchange Wiki link for the item. The application will also inform the user if an item they are searching is tradeable or a quest item. This application also uses the RuneScape Microservice written by my dev partner Sabrina Estrada. This microservice uses ZeroMQ sockets to send and receive data.

# Dependencies

To properly run the OSRS Exchange Portal, you will need the following dependencies:

- ZeroMQ Python
- Requests Python
- Beautiful Soup Python
- Python 3

# Running the application

To run the application,follow these steps:

1. Clone this repository to your local environment.
2. In an IDE with the proper dependencies installed, open two separate terminal windows.
3. In one terminal window, type:
```
python server.py
```
4. In the other terminal window, type:
```
python client.py
```
This will immediately execute the application for use. Enter an item.

5. From the client, the item input will send a request to the microservice using ZeroMQ.
6. Once the microservice receives the request, it process the request and fetches the appropriate info from the API.
7. Once the appropriate API information has been found, the microservice will send the response back to the client.
8. This process can be repeated as necessary for as many items as the user needs.

# Credits

The OldSchool RuneScape Exchange Portal was built by Brittaney Nico Davis for CS 361 at Oregon State University, spring quarter of 2023. The RuneScape Microservice was built by Sabrina Estrada for CS 361 at Oregon State University, spring quarter of 2023. 

# UML Diagram

![OldSchool RuneScape Exchange Portal-2](https://github.com/baedirin/cs-361-portfolio/assets/16569870/34a7b65c-9c88-415f-aa4d-79fb99a276ce)

