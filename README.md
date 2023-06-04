# avitrices-assistant
This is the female assistant which acts on your  voice commands .it is ais a voice-recognition Artificial Intelligence application
It takes the input of the user in the form of a voice or text and processes it and returns the feedback ind ifferent ways.

With continuous advancements in artificial intelligence, natural language processing, speechr ecognition, and text-to-speech technologies,virtual assistants are transforming the waycommercial organizations interact with customers.

For instance, product websites are increasingly implementing chat-bot assistants to answer frequently asked questions and common customer complaint. This system is designed to be used efficiently on desktops. Personal assistants software improves user productivity by managing routine tasks of the user and by providing information from an online source to the user. It is no longer a human who learns to communicate with a machine, but a machine learns to communicate with a human, exploring his actions, habits, behavior and trying to become his personalized assistant.

## MODULES

A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.
Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.
The syntax foe importing the module in python vs code is import module name before that module should be installed in vs code by running the command in terminal pip install module name.

These are the modules should be installed :

### SPEECH RECOGNITION: 
The voice module used this system is Google’s API i.e. “import speech_recognition as sr”. This module is used to recognize the sound waves given by the user as input. This is a loose API this is supplied and supported by Google. This is a totally mild API that facilitates in decreasing the scale of our application.

### PYTTSX3: 
To convert text into speech in python the pyttsx3 module is used. This is an offline module. The module provides run and wait functionality. It is used to allow how much time the system will wait for another input of user. This is a module available in the python community for free that can be installed using the pip command.

### DATETIME: 
The Date-Time module is imported to support the date and time. For example, the consumer wants to recognize the modern- day date and time or the person desires to time table a venture at a sure time. In brief this module helps instructions to manipulate date and time and carry out operations according to it handiest. This is a critical module, mainly in tasks in which we need to keep a track of time. This module could be very small in length and allows controlling the dimensions of our program. If the modules are too large or heavy then the system will lag and provide gradual responses.

### WIKIPEDIA: 
Wikipedia is an online library in python which it possible for the virtual assistant to process the queries on Wikipedia and display it to the users. This library needs an internet connection. The number of lines that the user wants to get as a result can be set manually.

 ### WEBBROWSER: 
Web-browser module is imported to display information from web to users. If the user wants to open browser and gives input as “Open Google”. Then input is processed using this module and the Google browser is opened. The browser which is set in code will open.

### OS MODULE: 
OS Module provides operating system dependent functionalities. If we want to perform operations of OS like data reading, data writing, or data manipulate paths then this types of functions are available in an OS module. When the these operations raise an error like “OSError” in case of any error like invalid names, paths, or arguments which may be incorrect or correct but just not accepted by the operating system.

### PYWHATKIT:
Is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it is one of the most popular library for WhatsApp and YouTube automation. New updates are released frequently with new features and bug fixes.

### SMTPLIB: 
SMTPLIB is python’s standard library which deals with emails. The SMTPLIB library sends mail using “SMTP”. This is done using steps that are - initialize, sendmail(), quit. When the optional parameters host and port are provided then connect method is called with these arguments during initialization.

### RANDOM:
This module implements pseudo-random number generators for various distributions. For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

### PHONENUMBER:
Phone numbers is one of the modules that provides numerous features like providing basic information of a phone number

### PYAUTOGUI:
PyAutoGUI is essentially a Python package that works across Windows, MacOS X and Linux which provides the ability to simulate mouse cursor moves and clicks as well as keyboard button presses.

## WORKING

Taking voice as a input from user. Conversion of the speech into text by the system The converted text is then processed to get the desired output.
The text contains some keywords that determine what queries are to be executed. If the keyword did not matched the queries in the program hence the assistant will ask the user to speak again. The output which is in the text form is converted to speech and is provided to the user. Above figure shows the flow of the voice assistant system. speech recognition is used to convert the input 

voice to text. This text is then sent to the processor, it detects the nature of the command and calls the related code for execution process.


![image](https://github.com/aaditeeshelke/avitrices-assistant/assets/135505964/e58ca497-0d29-4260-a284-95a503217cd4)





