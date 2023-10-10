<h1>AirBnB_Clone</h1>

<p>This project is intended to create a clone of the AirBnB web application.
Most of the features found on the website will not be implemented in this clone,
however the fundamental components that defines the overall structure will be attempted
in this project. The purpose mainly is to gain a hands experience of how web applications
are built. Project by: <strong>Eric Acquah</strong> and <strong>Chioma Ukora</strong>;
Software Engineering Students of ALX SWE.
</p>

<h2>STRUCTURE</h2>

<h3>The Command interpreter:</h3>

<p1>
The Command interpreter basically will be used to manage(create, update, destroy) the objects that will
be used. It takes in a command, (provided it's a valid command) parse it and give it to the appropriate
command handler to handle the needed processes.

<h4>example:</h4>

<h4>Interactive mode => </h4>

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):

EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

<h4>Non-interactive mode => </h4>

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):

EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):

EOF  help  quit
(hbnb)
$
</p1>
