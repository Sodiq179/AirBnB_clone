# AirBnB Clone

## Description
This is the first step towards building my first full web application: the AirBnB clone. This project aims at creating a basic clone of the AirBnB console. 

#### Command Interpreter Usage
---
| Commands  | Functions                                          |
| --------- | -------------------------------------------------- |
| `quit`    | exits                                              |
| `create`  | creates a new object                               |
| `update`  | updates an instance based on the class name and id |
| `destroy` | destroys specified object based on name and id     |
| `show`    | Prints the string representation of an instance    |
| `all`     | display all string representation of all instances |
| `count`   | returns the number of objects in a class           |
| `help`    | displays nformation about specific command         |

#### Installation
Start by cloning the repository and then run console.py
```
git clone https://github.com/Sodiq179/AirBnB_clone.git
```

#### Execution
```
Your shell should work like this in interactive mode:
``` 
cd AirBnB_clone

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: 
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

### Environment
* Language: Python3

### Authors
Babawale Sodiq