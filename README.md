# AirBnB Clone Project

## Description

The AirBnB Clone project is a part of a larger application designed to simulate the core functionalities of the popular Airbnb platform. The goal of the project is to implement a command-line interface (CLI) that interacts with a set of objects, which represent elements of the Airbnb platform such as users, places, states, and reviews. It serves as a foundation for building scalable web and mobile applications that offer vacation rental services.

This is a back-end portion of the AirBnB project that focuses on object-oriented programming, file storage, and a command interpreter. It does not implement any front-end or user interface (UI) elements.

## Command Interpreter

The Command Interpreter is the core part of the project. It allows users to interact with the system via the command line. The interpreter can perform various tasks related to creating, displaying, updating, and deleting objects that represent users, places, reviews, etc.

### How to Start the Command Interpreter

To run the command interpreter, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/<your_username>/AirBnB_clone.git
Navigate to the project directory:

bash
Copy code
cd AirBnB_clone
Run the command interpreter:

bash
Copy code
./console.py
How to Use the Command Interpreter
Once started, the command interpreter will display the following prompt:

scss
Copy code
(hbnb)
At the prompt, you can input commands to interact with the system. Some of the available commands include:

create <class_name>: Create a new instance of a class.

Example:
bash
Copy code
create User
show <class_name> <id>: Show the details of an instance based on its class name and ID.

Example:
bash
Copy code
show User 12345
destroy <class_name> <id>: Destroy an instance based on its class name and ID.

Example:
bash
Copy code
destroy User 12345
all <class_name>: Display all instances of a specific class.

Example:
bash
Copy code
all User
update <class_name> <id> <attribute_name> <attribute_value>: Update an instance with a new value for a specific attribute.

Example:
bash
Copy code
update User 12345 email "new_email@example.com"
Examples
Here’s an example session with the interpreter:

bash
Copy code
(hbnb) create User
12345
(hbnb) show User 12345
[User] (12345) {'id': '12345', 'created_at': '2024-11-16T12:00:00.000000', 'updated_at': '2024-11-16T12:00:00.000000', 'email': '', 'password': '', 'first_name': '', 'last_name': ''}
(hbnb) update User 12345 email "john.doe@example.com"
(hbnb) show User 12345
[User] (12345) {'id': '12345', 'created_at': '2024-11-16T12:00:00.000000', 'updated_at': '2024-11-16T12:01:00.000000', 'email': 'john.doe@example.com', 'password': '', 'first_name': '', 'last_name': ''}
(hbnb) destroy User 12345
Project Structure
The project contains the following key components:

console.py: The command-line interpreter responsible for processing user input.
models/: Contains the definition of all object models (e.g., User, State, City, etc.).
tests/: Contains unit tests for the project.
README.md: This file, which provides an overview of the project.
