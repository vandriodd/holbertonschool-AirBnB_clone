<div align="center">

<img src="https://github.com/vandriodd/holbertonschool-AirBnB_clone/assets/110431271/16e8dbdd-c2b9-46a8-ad80-2d0b8729618a" alt="AirBnB" width=600 />
<h1> AirBnB clone: The console </h1>

> This repository contains a command interpreter for manipulating [AirBnB](https://es.airbnb.com/) clone data.

</div>

<div align="center">

![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png)

</div>

<br>

## Table of contents
* [About](#about)
* [Resources](#resources)
* [Requirements](#requirements)
* [Files](#files)
* [Usage](#usage)
* [Authors](#authors)

## About 
This project is about the initial phase of creating a simple and functional clone of the [AirBnB](https://es.airbnb.com/) website. Here is a clearer visualization of our position:

<br>

<div align="center">

<img src="https://github.com/vandriodd/holbertonschool-AirBnB_clone/assets/110431271/0bc71d0c-413e-48bb-8a20-528a5adbc7e8" alt="First step backend" width=700 />

</div>

<br>

The main objective of this stage is to create a **storage system** through the development of a data model and a command interpreter where:

* Python objects will be managed.
* These objects will be stored in a JSON file.

All of this is aimed at creating an abstraction between *"My object"* and *"How it is stored and persisted"*, which allows for efficient changes in storage types. The console included in this repository **serves as a tool to validate this storage engine.**

## Resources
* [cmd module](https://docs.python.org/3/library/cmd.html)
* Python packages concept page, specifically [packages](https://docs.python.org/3.4/tutorial/modules.html#packages) and [circular import](https://www.stefaanlippens.net/circular-imports-type-hints-python.html)
* Serialization/Deserialization
* [uuid module](https://docs.python.org/3/library/uuid.html)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [unittest module](https://docs.python.org/3/library/unittest.html)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Requirements
* Ubuntu 20.04 LTS
* Python3 version 3.8.5
* Pycodestyle (PEP8) version 2.7
* Use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* Shell should work in both interactive and non-interactive mode
* All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

## Files
### Root directory
[console.py](console.py) - The `console` module provides a command-line interface for managing and manipulating objects within the application. It includes the `HBNBCommand` class, extending `cmd.Cmd`, to implement commands for creating, showing, updating, and deleting instances of various classes.

Methods:

* `do_quit()`: Exit the program.
* `do_EOF()`: Exit the program on end-of-file.
* `emptyline`: Ignore empty lines.
* `do_create()`: Create and save a new instance of the specified class.
* `do_show()`: Print details of an instance by class name and id.
* `do_destroy()`: Delete an instance by class name and id.
* `do_all()`: Print string representations of instances by class or all.
* `do_update()`: Update instance attribute by class and id.

### [/models](./models/) directory

[base_model.py](./models/base_model.py) - The `base_model` module implements the `BaseModel` class, which serves as the foundation for other model classes. It handles instance initialization, string representation, saving updates, and conversion to dictionary format.

Methods:

* `init()`: Initializes a `BaseModel` class.
* `str()`: Overrides str method for specific string representation.
* `save()`: Update `updated_at` attribute with current datetime and save changes.
* `to_dict()`: Converts instance to dictionary format.

The classes that inherit from `BaseModel` are:

* [User](./models/user.py)
* [State](./models/state.py)
* [City](./models/city.py)
* [Amenity](./models/amenity.py)
* [Place](./models/place.py)
* [Review](./models/review.py)


### [/models/engine](./models/engine/) directory

[file_storage.py](./models/engine/file_storage.py) - The `file_storage` module provides functionality for storing and retrieving objects in a JSON file. It includes the `FileStorage` class with methods for managing objects, serializing, deserializing, and saving data. The module maintains a dictionary of objects and defines the file path and supported classes.

Methods:

* `all()`: Retrieves all stored objects.
* `new()`: Adds a new object to the storage.
* `save()`: Serializes and saves objects to the JSON file
* `reload()`: Deserializes objects from the JSON file and reloads them into storage.


### [/tests](./tests/) directory
The test files in the `/test` directory contain test cases for different classes in the project. Each test file focuses on testing specific functionalities of the corresponding class. The test files ensure that the classes are created correctly, have the proper attributes, and important methods work correctly. Here is a summary of each test file:

[test_base_model.py](./tests/test_models/test_base_model.py) - Contains tests for the `BaseModel` class. It verifies instance creation, attributes, attribute types, `save()` and `to_dict()` methods, and attribute update functionality.

[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) - Contains tests for the `FileStorage` class. It verifies attributes, `all()`, `save()`, and `reload()` methods.

[test_user.py](./tests/test_models/test_user.py) - Contains tests for the `User` class. It verifies instance creation, attributes, and attribute types.

[test_state.py](./tests/test_models/test_state.py) - Contains tests for the `State` class. It verifies instance creation, attributes, and attribute types.

[test_city.py](./tests/test_models/test_city.py) - Contains tests for the `City` class. It verifies instance creation, attributes, and attribute types.

[test_amenity.py](./tests/test_models/test_amenity.py) - Contains tests for the `Amenity` class. It verifies instance creation, attributes, and attribute types.

[test_place.py](./tests/test_models/test_place.py) - Contains tests for the `Place` class. It verifies instance creation, attributes, and attribute types.

[test_review.py](./tests/test_models/test_review.py) - Contains tests for the `Review` class. It verifies instance creation, attributes, and attribute types.

## Usage
### Installation
To use the console, follow these steps:

1. Clone the repository using `git clone https://github.com/vandriodd/holbertonschool-AirBnB_clone` or download the source code.
2. Ensure that Python3 is installed on your system.
3. Navigate to the project directory using `cd holbertonschool-AirBnB_clone`.
4. Start having fun by running the console script!

### How it works
As mentioned above, the `console` module allows you to interact with application objects through a command-line interface. It also provides a **non-interactive** mode for automation and scripting.

To start the console in **interactive mode**, run the following command:

``` bash
./console.py
```

Once in the console, you can enter commands and interact with the available functionality.

To use the console in **non-interactive mode**, you can pipe commands into the script or provide commands from a file. For example:

``` bash
echo "help" | ./console.py
```

https://github.com/vandriodd/holbertonschool-AirBnB_clone/assets/110431271/9acc46b7-d4a8-43ff-9512-925f17947f52

### Testing
To run the unit tests for the console, you can use the following command:

``` bash
python3 -m unittest discover tests
```

This will execute all the tests defined in the `/tests` directory and provide the test results. Ensure that the required dependencies are installed before running the tests.

It is also possible to run the tests in **non-interactive mode** by piping the test command into the script:

``` bash
echo "python3 -m unittest discover tests" | bash
```

<div align="center">

## Authors
  
&ensp;[<img src="https://img.shields.io/badge/vandriodd-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/vandriodd)
&ensp;[<img src="https://img.shields.io/badge/LuisinaLlugdar-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/LuisinaLlugdar)

<br>

![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png)

<br>

_Last updated: July 9, 2023_

</div>
