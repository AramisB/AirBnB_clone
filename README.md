AirBnB CLI: Manage Your AirBnB Objects Efficiently

This project provides a command-line interpreter (CLI) to manage your AirBnB objects, forming the foundation for building a full AirBnB clone application. It utilizes a file-based storage engine and adheres to best practices for object serialization and deserialization.

Command Interpreter Overview
The CLI allows you to perform various operations on your AirBnB objects, including:

Creating objects: Users, States, Cities, Places, etc.
Retrieving objects: Fetch specific objects based on ID.
Updating objects: Modify attributes of existing objects.
Deleting objects: Remove unwanted objects from storage.

Getting Started
1. Prerequisites:
Python 3.x installed on your system.
A basic understanding of Python and command-line interfaces.

2. Installation:
Clone this repository or download the project files.

3. Usage:

Navigate to the project directory in your terminal and execute:

Bash
python main.py
This will launch the CLI and display the available commands.

How to Use the CLI
The CLI provides several commands with specific options. Here are some examples:

Create a new User:
Bash
(airbnb_cli)> create user name="Alice" email="alice@example.com"

List all Users:
Bash
(airbnb_cli)> show users

Get details of a User with ID 1:
Bash
(airbnb_cli)> show user id=1

Update the email address of User with ID 1:
Bash
(airbnb_cli)> update user id=1 email="new_email@example.com"

Delete a User with ID 1:
Bash
(airbnb_cli)> destroy user id=1

Further Exploration:

Refer to the source code within the commands directory for details on individual commands and their available options.

Future Development
This project serves as the groundwork for your AirBnB clone application. Future steps can involve:

Implementing additional object types (e.g., Bookings, Reviews).
Expanding the command set for more complex operations.
Integrating a database for persistent storage (beyond file-based storage).
Building a user interface (web or mobile) to interact with the CLI functionalities.
By effectively utilizing this CLI and extending its capabilities, you can create a robust system for managing your AirBnB listings and user data.