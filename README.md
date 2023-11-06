Airbnb project
The goal of the project is to deploy on your server a simple copy of the AirBnB website.

**our first feature to begin with is a command interpreter to manipulate data without a visual interface.
--The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler. Input lines are parsed into two parts. The command, and any other text on the line. If the user enters a command foo bar, and your class includes a method named do_foo(), it is called with "bar" as the only argument.

--The end-of-file marker is dispatched to do_EOF(). If a command handler returns a true value, the program will exit cleanly. So to give a clean way to exit your interpreter, make sure to implement do_EOF() and have it return True.
