# AIRBNB CLONE
## Introduction
This project was given by Holberton School for us to understand multiple concepts for back-end applications. Concepts that we learned about this project are:

- Json serialization and deserialization
- Args/Kwargs for formatting datetimes
- Class/Instances attributes
- Global scope variables
- cmd to create a command line interpreter

## Usage of this program:

First, clone this repo in your terminal:

```
git@github.com:KevinTMO/AirBnB_clone.git
cd AirBnB_clone/
```
After getting the repo in your terminal, just get inside the repo and execute the console:
```
./console.py
```
This will open our command line interpreter. In here we can use multiple commands like:
- **create** (will create a new instance for the specify class and then print the id)
- **all** (will print all instances of the specify class or all classes)
- **show** (will show all the current instances created for an specify class)
- **update** (will update a class with a new instance)
- **destroy** (will delete an instance)
- **quit** (exit the console)
- **EOF** (It just implement the CTRL-D for exit the console)
- **help** (will show you how to use any other command. Usage: help <command> Ex. help quit)

## Examples of using the console
### create command
```
(07:37:28) vagrant@vagrant-ubuntu-trusty-64:AirBnB_clone(main)
 --> ./console.py
Welcome to HBNB shell interpreter! Type ? to list commands
(hbnb) help create
Create a new instance of BaseModel
(hbnb) create BaseModel
20599d57-c730-4d45-a1ec-68747c85c48f
(hbnb)
```
### show command
```
(07:42:17) vagrant@vagrant-ubuntu-trusty-64:AirBnB_clone(main)
 --> ./console.py
Welcome to HBNB shell interpreter! Type ? to list commands
(hbnb) help show
Show a string representation of an instance
(hbnb) show BaseModel 20599d57-c730-4d45-a1ec-68747c85c48f
[BaseModel] (20599d57-c730-4d45-a1ec-68747c85c48f) {'updated_at': datetime.datetime(2021, 11, 15, 7, 38, 42, 595026), 'id': '20599d57-c730-4d45-a1ec-68747c85c48f', 'created_at': '2021-11-15T07:38:42.595018'}
(hbnb)
```
### update command
```
(07:58:53) vagrant@vagrant-ubuntu-trusty-64:AirBnB_clone(main)
 --> ./console.py
Welcome to HBNB shell interpreter! Type ? to list commands
(hbnb) help update
Updates an instance -> USAGE: <Class Name> <id> <attribute name> "<attribute value>"
(hbnb) create BaseModel
f4345d35-c2e3-44f6-80d0-73fedcfae65e
(hbnb) update BaseModel f4345d35-c2e3-44f6-80d0-73fedcfae65e First_Name "Betty"
(hbnb) show BaseModel f4345d35-c2e3-44f6-80d0-73fedcfae65e
[BaseModel] (f4345d35-c2e3-44f6-80d0-73fedcfae65e) {'updated_at': datetime.datetime(2021, 11, 15, 7, 59, 1, 395345), 'created_at': datetime.datetime(2021, 11, 15, 7, 59, 1, 395336), 'id': 'f4345d35-c2e3-44f6-80d0-73fedcfae65e', 'First_Name': '"Betty"'}
(hbnb)
```
### destroy command
```
(08:00:39) vagrant@vagrant-ubuntu-trusty-64:AirBnB_clone(main)
 --> ./console.py
Welcome to HBNB shell interpreter! Type ? to list commands
(hbnb) help destroy
Deletes an instance based on the class name and id
(hbnb) show BaseModel f4345d35-c2e3-44f6-80d0-73fedcfae65e
[BaseModel] (f4345d35-c2e3-44f6-80d0-73fedcfae65e) {'id': 'f4345d35-c2e3-44f6-80d0-73fedcfae65e', 'updated_at': '2021-11-15T07:59:01.395345', 'created_at': datetime.datetime(2021, 11, 15, 7, 59, 1, 395336)}
(hbnb) destroy BaseModel f4345d35-c2e3-44f6-80d0-73fedcfae65e
(hbnb) show BaseModel f4345d35-c2e3-44f6-80d0-73fedcfae65e
** no instance found **
(hbnb)
```
### quit command
```
(08:01:48) vagrant@vagrant-ubuntu-trusty-64:AirBnB_clone(main)
 --> ./console.py
Welcome to HBNB shell interpreter! Type ? to list commands
(hbnb) help quit
Quit command to exit the program
(hbnb) quit
(08:02:04) vagrant@vagrant-ubuntu-trusty-64:AirBnB_clone(main)
 -->
 ```

And that's it, guys. I wish we had more time for this project. There's still many things to fix but we did our best and will continue to develop this program so it can work as it should. Until next time!




