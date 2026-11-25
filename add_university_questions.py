
from database import get_db_connection

YEAR = "3rd Year"
SUBJECT = "Python Programming"
CHAPTER = "Unit 1: Introduction"

unit2_questions = [
    {
        "question": "Which function is used to find the length of a string in Python?",
        "options": ["size()", "length()", "len()", "count()"],
        "answer": "C",
        "explanation": "The len() function returns the number of characters in a string.",
        "exam": "The len() function is used to determine the number of characters present in a string."
    },
    {
        "question": "Which operator is used for string concatenation in Python?",
        "options": ["*", "+", "-", "/"],
        "answer": "B",
        "explanation": "The + operator joins two strings.",
        "exam": "String concatenation in Python is performed using the + operator."
    },
    {
        "question": "Which method converts a string into uppercase?",
        "options": ["upper()", "uppercase()", "capitalize()", "big()"],
        "answer": "A",
        "explanation": "The upper() method converts all characters to uppercase.",
        "exam": "The upper() method returns a copy of the string with all lowercase characters converted to uppercase."
    },
    {
        "question": "Which method removes whitespace from both ends of a string?",
        "options": ["remove()", "strip()", "trim()", "delete()"],
        "answer": "B",
        "explanation": "The strip() method removes leading and trailing whitespace.",
        "exam": "The strip() method removes whitespace from the beginning and end of a string."
    },
    {
        "question": "Which method replaces a substring in Python?",
        "options": ["change()", "replace()", "modify()", "update()"],
        "answer": "B",
        "explanation": "The replace() method replaces occurrences of a substring.",
        "exam": "The replace() method returns a new string in which the specified substring is replaced."
    },
    {
        "question": "What is a class in Python?",
        "options": ["A loop", "A blueprint for objects", "A variable", "A function"],
        "answer": "B",
        "explanation": "A class is a blueprint used to create objects.",
        "exam": "A class is a user-defined blueprint that defines attributes and methods for creating objects."
    },
    {
        "question": "Which keyword is used to define a class in Python?",
        "options": ["function", "object", "class", "define"],
        "answer": "C",
        "explanation": "The class keyword is used to define a class.",
        "exam": "The class keyword is used to create a class in Python."
    },
    {
        "question": "What is an object in Python?",
        "options": ["An instance of a class", "A loop", "A module", "A keyword"],
        "answer": "A",
        "explanation": "An object is an instance of a class.",
        "exam": "An object is an instance of a class containing data and behaviour defined by that class."
    },
    {
        "question": "Which method is called automatically when an object is created?",
        "options": ["start()", "main()", "__init__()", "create()"],
        "answer": "C",
        "explanation": "The __init__() method initializes a newly created object.",
        "exam": "The __init__() method is a special initializer method automatically called when an object is instantiated."
    },
    {
        "question": "What does self represent in a Python class?",
        "options": ["Current instance", "Parent class", "Module", "Global variable"],
        "answer": "A",
        "explanation": "self refers to the current instance of the class.",
        "exam": "The self parameter represents the current instance of a class and is used to access its attributes and methods."
    }
]

questions = [
    {
        "question": "What is Python?",
        "options": ["A programming language", "An operating system", "A database", "A web browser"],
        "answer": "A",
        "explanation": "Python is a high-level, general-purpose programming language.",
        "exam": "Python is a high-level, interpreted, general-purpose programming language supporting procedural, object-oriented and functional programming."
    },
    {
        "question": "Who created Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "answer": "B",
        "explanation": "Guido van Rossum created Python.",
        "exam": "Python was created by Guido van Rossum and first released in 1991."
    },
    {
        "question": "Which extension is commonly used for Python source files?",
        "options": [".html", ".java", ".py", ".css"],
        "answer": "C",
        "explanation": "Python source files commonly use the .py extension.",
        "exam": "The .py extension is commonly used for Python source-code files."
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["input()", "print()", "show()", "displayText()"],
        "answer": "B",
        "explanation": "The print() function displays output.",
        "exam": "The print() function is used to display output in Python."
    },
    {
        "question": "Which symbol begins a single-line comment in Python?",
        "options": ["//", "/*", "#", "<!--"],
        "answer": "C",
        "explanation": "The # symbol begins a single-line comment.",
        "exam": "Python uses the hash symbol (#) to begin a single-line comment."
    },
    {
        "question": "When was Python first released?",
        "options": ["1985", "1991", "2000", "2005"],
        "answer": "B",
        "explanation": "Python was first released in 1991.",
        "exam": "Python was first released in 1991 by Guido van Rossum."
    },
    {
        "question": "Which organization supports and maintains Python?",
        "options": ["Microsoft", "Python Software Foundation", "Apple", "IBM"],
        "answer": "B",
        "explanation": "The Python Software Foundation supports the Python language.",
        "exam": "The Python Software Foundation (PSF) supports and promotes the Python programming language."
    },
    {
        "question": "Python is which type of programming language?",
        "options": ["Low-level", "High-level", "Machine-level", "Assembly-level"],
        "answer": "B",
        "explanation": "Python is a high-level programming language.",
        "exam": "Python is a high-level programming language with simple and readable syntax."
    },
    {
        "question": "Which of the following is a major feature of Python?",
        "options": ["Difficult syntax", "Readable syntax", "Hardware dependency", "No libraries"],
        "answer": "B",
        "explanation": "Python is known for its readable and simple syntax.",
        "exam": "Python provides simple, readable syntax that makes programs easier to develop and maintain."
    },
    {
        "question": "Python is a ______ language.",
        "options": ["General-purpose", "Markup", "Query-only", "Hardware description"],
        "answer": "A",
        "explanation": "Python is used in many areas of software development.",
        "exam": "Python is a general-purpose language used for web development, automation, scientific computing and more."
    },
    {
        "question": "Which symbol is used for assignment in Python?",
        "options": ["==", "=", "!=", ">"],
        "answer": "B",
        "explanation": "The = operator assigns a value to a variable.",
        "exam": "The assignment operator (=) assigns a value to a variable."
    },
    {
        "question": "Which of the following is a valid Python identifier?",
        "options": ["2name", "my-name", "my_name", "class"],
        "answer": "C",
        "explanation": "Identifiers can contain letters, digits and underscores, but cannot start with a digit.",
        "exam": "A valid identifier begins with a letter or underscore and may contain letters, digits and underscores. Reserved keywords cannot be used."
    },
    {
        "question": "Python is a ______ typed language.",
        "options": ["Statically", "Dynamically", "Hardware", "Assembly"],
        "answer": "B",
        "explanation": "Python determines variable types at runtime.",
        "exam": "Python is dynamically typed because the type of a variable is determined during execution."
    },
    {
        "question": "Which function accepts input from the user?",
        "options": ["print()", "input()", "display()", "scan()"],
        "answer": "B",
        "explanation": "The input() function accepts data from the user.",
        "exam": "The input() function reads data entered by the user and returns it as a string."
    },
    {
        "question": "What is the default return type of input()?",
        "options": ["Integer", "Float", "String", "Boolean"],
        "answer": "C",
        "explanation": "The input() function returns a string by default.",
        "exam": "The input() function returns the entered data in string format by default."
    },
    {
        "question": "Which function is used to identify the data type of an object?",
        "options": ["type()", "data()", "check()", "typeof()"],
        "answer": "A",
        "explanation": "The type() function returns an object's type.",
        "exam": "The type() function is used to identify the data type of an object."
    },
    {
        "question": "Which data type stores whole numbers?",
        "options": ["float", "str", "int", "list"],
        "answer": "C",
        "explanation": "The int data type stores integer values.",
        "exam": "The int data type represents whole numbers without decimal points."
    },
    {
        "question": "Which data type stores decimal numbers?",
        "options": ["int", "float", "str", "bool"],
        "answer": "B",
        "explanation": "The float data type stores floating-point values.",
        "exam": "The float data type represents numbers that contain decimal points."
    },
    {
        "question": "Which data type is used to store text?",
        "options": ["int", "float", "str", "bool"],
        "answer": "C",
        "explanation": "The str data type stores text.",
        "exam": "The str data type represents a sequence of characters or text."
    },
    {
        "question": "Which two values are used by the Boolean data type?",
        "options": ["Yes and No", "True and False", "1 and 2", "On and Off"],
        "answer": "B",
        "explanation": "Boolean values are True and False.",
        "exam": "The Boolean data type represents two logical values: True and False."
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C",
        "explanation": "The def keyword defines a function.",
        "exam": "The def keyword is used to define a function in Python."
    },
    {
        "question": "Which keyword is used to define a class?",
        "options": ["object", "class", "struct", "define"],
        "answer": "B",
        "explanation": "The class keyword creates a class.",
        "exam": "The class keyword is used to define a class in Python."
    },
    {
        "question": "Which keyword is used for conditional statements?",
        "options": ["if", "when", "check", "condition"],
        "answer": "A",
        "explanation": "The if keyword checks a condition.",
        "exam": "The if statement executes a block of code when its condition is true."
    },
    {
        "question": "Which keyword is used to iterate over a sequence?",
        "options": ["repeat", "for", "loop", "iterate"],
        "answer": "B",
        "explanation": "The for loop iterates over a sequence.",
        "exam": "The for loop executes a block of statements for each item in an iterable."
    },
    {
        "question": "Which loop executes while a condition is true?",
        "options": ["for", "if", "while", "repeat"],
        "answer": "C",
        "explanation": "The while loop repeats while its condition is true.",
        "exam": "The while loop repeatedly executes statements as long as its condition remains true."
    },
    {
        "question": "What does case-sensitive mean in Python?",
        "options": ["Uppercase and lowercase are different", "Spaces are ignored", "Only uppercase is allowed", "Only lowercase is allowed"],
        "answer": "A",
        "explanation": "Python treats uppercase and lowercase letters differently.",
        "exam": "Python is case-sensitive, so identifiers such as name and Name are considered different."
    },
    {
        "question": "How many spaces are recommended for one indentation level by PEP 8?",
        "options": ["One", "Two", "Four", "Eight"],
        "answer": "C",
        "explanation": "PEP 8 recommends four spaces per indentation level.",
        "exam": "PEP 8 recommends using four spaces for each indentation level."
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "**", "//", "%%"],
        "answer": "B",
        "explanation": "The ** operator performs exponentiation.",
        "exam": "The ** operator raises a number to the power of another number."
    },
    {
        "question": "Which operator performs floor division?",
        "options": ["/", "%", "//", "**"],
        "answer": "C",
        "explanation": "The // operator performs floor division.",
        "exam": "The // operator performs floor division and returns the quotient rounded down."
    },
    {
        "question": "Which operator returns the remainder after division?",
        "options": ["/", "%", "//", "**"],
        "answer": "B",
        "explanation": "The % operator returns the remainder.",
        "exam": "The modulo operator (%) returns the remainder after division."
    },
    {
        "question": "Which operator checks whether two values are equal?",
        "options": ["=", "==", "!=", ">="],
        "answer": "B",
        "explanation": "The == operator compares two values for equality.",
        "exam": "The equality operator (==) checks whether two values are equal."
    },
    {
        "question": "Which logical operator returns True when both conditions are true?",
        "options": ["or", "not", "and", "is"],
        "answer": "C",
        "explanation": "The and operator requires both conditions to be true.",
        "exam": "The and operator returns True only when both operands are true."
    },
    {
        "question": "Which logical operator returns True when at least one condition is true?",
        "options": ["and", "or", "not", "in"],
        "answer": "B",
        "explanation": "The or operator returns True if at least one condition is true.",
        "exam": "The or operator returns True when at least one of its conditions is true."
    },
    {
        "question": "Which operator reverses a Boolean condition?",
        "options": ["and", "or", "not", "is"],
        "answer": "C",
        "explanation": "The not operator performs logical negation.",
        "exam": "The not operator reverses a Boolean result, changing True to False and False to True."
    },
    {
        "question": "Which brackets are used to create a list?",
        "options": ["()", "{}", "[]", "<>"],
        "answer": "C",
        "explanation": "Lists are created using square brackets.",
        "exam": "A list is an ordered and mutable collection created using square brackets."
    },
    {
        "question": "Which brackets are commonly used to create a tuple?",
        "options": ["[]", "()", "{}", "<>"],
        "answer": "B",
        "explanation": "Tuples are commonly represented using parentheses.",
        "exam": "A tuple is an ordered and immutable collection commonly represented using parentheses."
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "String"],
        "answer": "C",
        "explanation": "A dictionary stores data as key-value pairs.",
        "exam": "A dictionary stores data in key-value pairs, where each key maps to a value."
    },
    {
        "question": "Which collection stores unique elements?",
        "options": ["List", "Set", "Tuple", "String"],
        "answer": "B",
        "explanation": "A set stores unique elements.",
        "exam": "A set is an unordered collection of unique elements."
    },
    {
        "question": "Which of the following collections is mutable?",
        "options": ["Tuple", "String", "List", "Integer"],
        "answer": "C",
        "explanation": "A list can be changed after creation.",
        "exam": "A list is mutable, meaning its elements can be modified after creation."
    },
    {
        "question": "Which of the following collections is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "D",
        "explanation": "A tuple cannot be modified after creation.",
        "exam": "A tuple is immutable, so its elements cannot be changed after creation."
    },
    {
        "question": "What is the index of the first element in a Python sequence?",
        "options": ["1", "-1", "0", "2"],
        "answer": "C",
        "explanation": "Python indexing starts from zero.",
        "exam": "Python uses zero-based indexing, so the first element has index 0."
    },
    {
        "question": "Which function returns the number of elements in an object?",
        "options": ["count()", "size()", "len()", "total()"],
        "answer": "C",
        "explanation": "The len() function returns the length of an object.",
        "exam": "The len() function returns the number of items in a sequence or collection."
    },
    {
        "question": "Which function generates a sequence of numbers?",
        "options": ["numbers()", "range()", "sequence()", "generate()"],
        "answer": "B",
        "explanation": "The range() function generates a sequence of integers.",
        "exam": "The range() function generates a sequence of integers, commonly used in loops."
    },
    {
        "question": "Which keyword is used to import a module?",
        "options": ["include", "using", "import", "module"],
        "answer": "C",
        "explanation": "The import keyword makes module functionality available.",
        "exam": "The import statement is used to access modules and their functionality."
    },
    {
        "question": "Which function converts a compatible value to an integer?",
        "options": ["str()", "float()", "int()", "bool()"],
        "answer": "C",
        "explanation": "The int() function converts a compatible value to an integer.",
        "exam": "The int() function converts a compatible value into an integer."
    },
    {
        "question": "Which function converts a compatible value to a floating-point number?",
        "options": ["int()", "float()", "str()", "type()"],
        "answer": "B",
        "explanation": "The float() function converts a compatible value to a float.",
        "exam": "The float() function converts a compatible value into a floating-point number."
    },
    {
        "question": "Which function converts a compatible value into a string?",
        "options": ["int()", "float()", "str()", "list()"],
        "answer": "C",
        "explanation": "The str() function converts an object to its string representation.",
        "exam": "The str() function converts a compatible object into its string representation."
    },
    {
        "question": "Which tool is commonly used to install Python packages?",
        "options": ["pip", "html", "mysql", "git"],
        "answer": "A",
        "explanation": "pip is the package installer for Python.",
        "exam": "pip is a package management tool used to install and manage Python packages."
    },
    {
        "question": "What is PEP 8?",
        "options": ["A database", "Python style guide", "An operating system", "A compiler"],
        "answer": "B",
        "explanation": "PEP 8 provides Python coding style recommendations.",
        "exam": "PEP 8 is the style guide that provides recommendations for writing readable Python code."
    },
    {
        "question": "Which mode allows Python statements to be executed one at a time?",
        "options": ["Batch mode", "Interactive mode", "Hardware mode", "Design mode"],
        "answer": "B",
        "explanation": "Interactive mode executes statements directly in the Python prompt.",
        "exam": "Interactive mode allows users to enter and execute Python statements one at a time."
    },
    {
        "question": "Which file extension is used for Python compiled bytecode files?",
        "options": [".py", ".html", ".pyc", ".txt"],
        "answer": "C",
        "explanation": "Python bytecode files commonly use the .pyc extension.",
        "exam": "Python compiled bytecode files commonly use the .pyc extension."
    },
    {
        "question": "What is the purpose of the break statement?",
        "options": ["Skip one iteration", "Exit a loop", "Start a function", "Import a module"],
        "answer": "B",
        "explanation": "The break statement terminates the nearest enclosing loop.",
        "exam": "The break statement immediately terminates the nearest enclosing loop."
    },
    {
        "question": "What is the purpose of the continue statement?",
        "options": ["Exit the program", "Skip the current iteration", "Stop Python", "Create a variable"],
        "answer": "B",
        "explanation": "The continue statement skips the rest of the current loop iteration.",
        "exam": "The continue statement skips the remaining statements in the current iteration and proceeds to the next iteration."
    },
]

software_unit1_questions = [
    {
        'question': 'What is software?',
        'options': ['A set of hardware devices', 'A collection of programs and related data', 'An operating system only', 'A computer network'],
        'answer': 'B',
        'explanation': 'Software is a collection of programs, procedures and related data.',
        'exam': 'Software is a collection of programs and related data used to perform specific tasks.'
    },
    {
        'question': 'What is Software Engineering?',
        'options': ['Writing code without planning', 'A systematic approach to software development', 'Only software testing', 'Hardware maintenance'],
        'answer': 'B',
        'explanation': 'Software Engineering applies systematic engineering principles to software development.',
        'exam': 'Software Engineering is a systematic, disciplined and measurable approach to software development.'
    },
    {
        'question': 'Who introduced the term Software Engineering?',
        'options': ['Charles Babbage', 'Friedrich Bauer', 'Bill Gates', 'Dennis Ritchie'],
        'answer': 'B',
        'explanation': 'Friedrich Bauer helped introduce the term Software Engineering.',
        'exam': 'The term Software Engineering was popularized at the 1968 NATO conference and is associated with Friedrich Bauer.'
    },
    {
        'question': 'What was the main reason for the software crisis?',
        'options': ['Lack of computers', 'Increasing software complexity', 'Availability of internet', 'Low hardware cost'],
        'answer': 'B',
        'explanation': 'Increasing software size and complexity caused many development problems.',
        'exam': 'The software crisis arose due to increasing software complexity, cost and difficulty in maintenance.'
    },
    {
        'question': 'Which of the following is a characteristic of software?',
        'options': ['It is manufactured physically', 'It does not wear out like hardware', 'It always needs raw materials', 'It has a limited physical life'],
        'answer': 'B',
        'explanation': 'Software does not physically wear out, although it can deteriorate due to changes and maintenance problems.',
        'exam': 'Software does not wear out physically like hardware, but may deteriorate because of modifications.'
    },
    {
        'question': 'Which of the following is NOT a software application?',
        'options': ['MS Word', 'Web browser', 'Keyboard', 'Calculator application'],
        'answer': 'C',
        'explanation': 'A keyboard is a hardware input device.',
        'exam': 'A keyboard is hardware, whereas MS Word, browsers and calculator applications are software.'
    },
    {
        'question': 'What is the primary objective of Software Engineering?',
        'options': ['To increase coding time', 'To develop reliable and quality software', 'To avoid documentation', 'To eliminate testing'],
        'answer': 'B',
        'explanation': 'Software Engineering aims to produce quality software within time and budget.',
        'exam': 'The primary objective is to develop reliable, maintainable and cost-effective software.'
    },
    {
        'question': 'Which is an example of system software?',
        'options': ['MS Excel', 'Operating System', 'PowerPoint presentation', 'Photo editor'],
        'answer': 'B',
        'explanation': 'An operating system manages computer resources and provides services to applications.',
        'exam': 'An operating system is system software that manages hardware and software resources.'
    },
    {
        'question': 'Which is an example of application software?',
        'options': ['Device driver', 'Compiler', 'MS Word', 'Operating system kernel'],
        'answer': 'C',
        'explanation': 'MS Word is application software used for word processing.',
        'exam': 'Application software performs user-oriented tasks, such as word processing.'
    },
    {
        'question': 'What is legacy software?',
        'options': ['Newly developed software', 'Old software still in use', 'Software without users', 'Temporary software'],
        'answer': 'B',
        'explanation': 'Legacy software is an older system that continues to support business or organizational needs.',
        'exam': 'Legacy software is an older software system that remains in operation.'
    },
    {
        'question': 'Which quality attribute describes how easily software can be modified?',
        'options': ['Portability', 'Maintainability', 'Efficiency', 'Usability'],
        'answer': 'B',
        'explanation': 'Maintainability refers to how easily software can be corrected or modified.',
        'exam': 'Maintainability is the ease with which software can be modified and maintained.'
    },
    {
        'question': 'What does software reliability mean?',
        'options': ['Attractive design', 'Ability to operate without failure for a specified period', 'Low development cost', 'Fast installation'],
        'answer': 'B',
        'explanation': 'Reliability measures the ability of software to perform correctly over time.',
        'exam': 'Software reliability is the probability of failure-free operation for a specified period.'
    },
    {
        'question': 'What is software portability?',
        'options': ['Ease of moving software to another environment', 'Speed of typing code', 'Ability to print documents', 'Software size'],
        'answer': 'A',
        'explanation': 'Portability means software can be transferred to different platforms or environments.',
        'exam': 'Portability is the ease with which software can be transferred between environments.'
    },
    {
        'question': 'Which quality attribute relates to ease of use?',
        'options': ['Usability', 'Reliability', 'Portability', 'Reusability'],
        'answer': 'A',
        'explanation': 'Usability describes how easily users can learn and operate software.',
        'exam': 'Usability is the degree to which software is easy to learn and use.'
    },
    {
        'question': 'What is software efficiency?',
        'options': ['Use of resources effectively', 'Number of developers', 'Number of pages', 'Software colour'],
        'answer': 'A',
        'explanation': 'Efficiency concerns performance and effective use of resources.',
        'exam': 'Software efficiency refers to performance in relation to resources and time.'
    },
    {
        'question': 'Which activity identifies what the customer needs?',
        'options': ['Coding', 'Requirement analysis', 'Deployment', 'Maintenance'],
        'answer': 'B',
        'explanation': 'Requirement analysis identifies and documents user needs.',
        'exam': 'Requirement analysis is the process of identifying and documenting customer requirements.'
    },
    {
        'question': 'What is the first major activity in many software development processes?',
        'options': ['Deployment', 'Requirement gathering', 'Maintenance', 'Coding'],
        'answer': 'B',
        'explanation': 'Requirement gathering helps understand the problem and user expectations.',
        'exam': 'Requirement gathering is an early activity used to understand user needs.'
    },
    {
        'question': 'What is the purpose of software design?',
        'options': ['To plan the software structure', 'To sell software', 'To remove requirements', 'To replace testing'],
        'answer': 'A',
        'explanation': 'Design converts requirements into an architecture and detailed solution.',
        'exam': 'Software design defines the architecture, components and interfaces of a system.'
    },
    {
        'question': 'Which activity converts design into executable instructions?',
        'options': ['Testing', 'Coding', 'Planning', 'Maintenance'],
        'answer': 'B',
        'explanation': 'Coding implements the software design using a programming language.',
        'exam': 'Coding is the implementation of software design using a programming language.'
    },
    {
        'question': 'What is the main purpose of software testing?',
        'options': ['To find defects', 'To increase file size', 'To avoid requirements', 'To replace design'],
        'answer': 'A',
        'explanation': 'Testing evaluates software to identify defects and check expected behaviour.',
        'exam': 'Software testing evaluates software to detect defects and verify requirements.'
    },
    {
        'question': 'What is software maintenance?',
        'options': ['Only writing new software', 'Modifying software after delivery', 'Buying hardware', 'Deleting documentation'],
        'answer': 'B',
        'explanation': 'Maintenance includes correcting, adapting and improving software after delivery.',
        'exam': 'Software maintenance is the modification of software after delivery to correct faults or improve it.'
    },
    {
        'question': 'Which type of maintenance fixes errors?',
        'options': ['Adaptive', 'Corrective', 'Perfective', 'Preventive'],
        'answer': 'B',
        'explanation': 'Corrective maintenance fixes defects found after software delivery.',
        'exam': 'Corrective maintenance modifies software to correct discovered faults.'
    },
    {
        'question': 'Which maintenance adapts software to a changed environment?',
        'options': ['Corrective', 'Adaptive', 'Perfective', 'Emergency'],
        'answer': 'B',
        'explanation': 'Adaptive maintenance makes software work in a changed environment.',
        'exam': 'Adaptive maintenance modifies software to keep it usable in a changed environment.'
    },
    {
        'question': 'Which maintenance improves software performance or functionality?',
        'options': ['Perfective', 'Corrective', 'Adaptive', 'Accidental'],
        'answer': 'A',
        'explanation': 'Perfective maintenance enhances performance or user-requested features.',
        'exam': 'Perfective maintenance improves software performance, maintainability or functionality.'
    },
    {
        'question': 'What is preventive maintenance?',
        'options': ['Fixing only visible errors', 'Making changes to reduce future problems', 'Installing hardware', 'Removing all features'],
        'answer': 'B',
        'explanation': 'Preventive maintenance reduces the possibility of future faults.',
        'exam': 'Preventive maintenance modifies software to prevent potential future problems.'
    },
    {
        'question': 'What is a software process?',
        'options': ['A set of activities used to develop software', 'A computer component', 'A programming language', 'A network cable'],
        'answer': 'A',
        'explanation': 'A software process defines activities and tasks involved in software development.',
        'exam': 'A software process is a structured set of activities used to develop and maintain software.'
    },
    {
        'question': 'Which of the following is a fundamental software process activity?',
        'options': ['Specification', 'Cooking', 'Printing', 'Scanning'],
        'answer': 'A',
        'explanation': 'Specification defines what the software should do and its constraints.',
        'exam': 'Software specification defines the required services and constraints of a system.'
    },
    {
        'question': 'What is software validation?',
        'options': ['Are we building the right product?', 'Are we writing the shortest code?', 'Is the computer switched on?', 'Are we using expensive hardware?'],
        'answer': 'A',
        'explanation': 'Validation checks whether the software meets user needs.',
        'exam': 'Software validation checks whether the developed system meets customer needs.'
    },
    {
        'question': 'What is software verification?',
        'options': ['Are we building the product right?', 'Is the software popular?', 'Is the user trained?', 'Is the hardware new?'],
        'answer': 'A',
        'explanation': 'Verification checks whether software work products meet specified requirements.',
        'exam': 'Software verification checks whether the software work products satisfy specified requirements.'
    },
    {
        'question': 'What is a software product?',
        'options': ['Only computer hardware', 'Software delivered to users with related documentation', 'Only a programming book', 'A network connection'],
        'answer': 'B',
        'explanation': 'A software product includes programs and may include documentation and configuration data.',
        'exam': 'A software product consists of programs and associated documentation and data.'
    },
    {
        'question': 'Which is a major challenge in software development?',
        'options': ['Managing complexity', 'Avoiding all users', 'Removing all testing', 'Using no documentation'],
        'answer': 'A',
        'explanation': 'Software systems can become complex and difficult to understand and maintain.',
        'exam': 'Managing software complexity is a major challenge in software development.'
    },
    {
        'question': 'What is scalability?',
        'options': ['Ability to handle increased workload', 'Ability to change font colour', 'Ability to delete files', 'Ability to print code'],
        'answer': 'A',
        'explanation': 'Scalability is the ability of a system to handle growth in workload or users.',
        'exam': 'Scalability is the ability of a system to handle increased workload or demand.'
    },
    {
        'question': 'What is reusability in software?',
        'options': ['Using software components again', 'Deleting old programs', 'Changing the computer', 'Avoiding documentation'],
        'answer': 'A',
        'explanation': 'Reusability allows existing components to be used in other software systems.',
        'exam': 'Reusability is the ability to use software components in multiple applications.'
    },
    {
        'question': 'Which document describes software requirements?',
        'options': ['SRS', 'CPU', 'RAM', 'HTML'],
        'answer': 'A',
        'explanation': 'SRS stands for Software Requirements Specification.',
        'exam': 'SRS is a document that specifies the functional and non-functional requirements of software.'
    },
    {
        'question': 'What is the full form of SRS?',
        'options': ['Software Requirement System', 'Software Requirements Specification', 'System Resource Software', 'Software Running Service'],
        'answer': 'B',
        'explanation': 'SRS stands for Software Requirements Specification.',
        'exam': 'SRS stands for Software Requirements Specification.'
    },
    {
        'question': 'Which requirement describes what a system should do?',
        'options': ['Functional requirement', 'Non-functional requirement', 'Hardware requirement', 'Physical requirement'],
        'answer': 'A',
        'explanation': 'Functional requirements specify system services and behaviour.',
        'exam': 'Functional requirements describe the functions and services that a system must provide.'
    },
    {
        'question': 'Which is an example of a non-functional requirement?',
        'options': ['User login', 'Generate a report', 'Response time', 'Calculate total'],
        'answer': 'C',
        'explanation': 'Response time is a performance constraint rather than a specific function.',
        'exam': 'Non-functional requirements specify quality attributes and constraints such as performance and security.'
    },
    {
        'question': 'What is project management in software engineering?',
        'options': ['Planning and controlling project activities', 'Only writing source code', 'Only designing logos', 'Repairing computers'],
        'answer': 'A',
        'explanation': 'Project management coordinates resources, schedules, cost and risks.',
        'exam': 'Software project management involves planning, organizing and controlling software development activities.'
    },
    {
        'question': 'What is a software development team?',
        'options': ['A group working to develop software', 'A group of computer parts', 'A collection of websites', 'A type of operating system'],
        'answer': 'A',
        'explanation': 'A software team includes people with different roles working toward a common goal.',
        'exam': 'A software development team is a group of professionals who work together to develop and maintain software.'
    },
    {
        'question': 'What is the role of a software engineer?',
        'options': ['Apply engineering principles to software', 'Manufacture keyboards', 'Only sell computers', 'Only operate printers'],
        'answer': 'A',
        'explanation': 'Software engineers design, develop, test and maintain software systems.',
        'exam': 'A software engineer applies engineering principles to design, develop, test and maintain software.'
    },
    {
        'question': 'What is a software defect?',
        'options': ['An error or flaw in software', 'A new feature', 'A computer monitor', 'A user manual'],
        'answer': 'A',
        'explanation': 'A defect is a flaw that can cause software to behave incorrectly.',
        'exam': 'A software defect is a flaw in a software work product that may cause incorrect behaviour.'
    },
    {
        'question': 'What is debugging?',
        'options': ['Finding and fixing defects in code', 'Installing an operating system', 'Creating a presentation', 'Formatting a hard disk'],
        'answer': 'A',
        'explanation': 'Debugging identifies the cause of errors and corrects them.',
        'exam': 'Debugging is the process of locating, analyzing and correcting software errors.'
    },
    {
        'question': 'What is software documentation?',
        'options': ['Written information about software', 'Only source code', 'A hardware device', 'An internet connection'],
        'answer': 'A',
        'explanation': 'Documentation describes software requirements, design, usage and maintenance.',
        'exam': 'Software documentation provides information about software development, operation and maintenance.'
    },
    {
        'question': 'What is open-source software?',
        'options': ['Software whose source code is available under an open-source license', 'Software that cannot be modified', 'Only paid software', 'Software without programs'],
        'answer': 'A',
        'explanation': 'Open-source software makes source code available under terms of an open-source license.',
        'exam': 'Open-source software is distributed under a license that permits access to and specified use or modification of its source code.'
    },
    {
        'question': 'What is proprietary software?',
        'options': ['Software controlled by its owner under restrictive terms', 'Always free software', 'Software without an owner', 'Only educational software'],
        'answer': 'A',
        'explanation': 'Proprietary software is controlled by its owner and has usage restrictions.',
        'exam': 'Proprietary software is owned and controlled by an individual or organization under specific licensing terms.'
    },
    {
        'question': 'What is a software license?',
        'options': ['Legal terms governing software use', 'A programming error', 'A hardware component', 'A testing technique'],
        'answer': 'A',
        'explanation': 'A software license defines permissions and restrictions for using software.',
        'exam': 'A software license is a legal agreement that specifies the conditions for using and distributing software.'
    },
    {
        'question': 'What is software evolution?',
        'options': ['Changes made to software over time', 'Deleting the operating system', 'Manufacturing hardware', 'Stopping all maintenance'],
        'answer': 'A',
        'explanation': 'Software evolves as requirements, technology and user needs change.',
        'exam': 'Software evolution refers to modifications made to software to meet changing requirements.'
    },
    {
        'question': 'Which factor helps improve software quality?',
        'options': ['Proper testing and review', 'Ignoring errors', 'Avoiding user feedback', 'Skipping requirements'],
        'answer': 'A',
        'explanation': 'Testing and reviews help identify defects and improve quality.',
        'exam': 'Software quality can be improved through reviews, testing and systematic development practices.'
    },
    {
        'question': 'Why is software engineering important?',
        'options': ['It helps manage complex software projects', 'It removes the need for users', 'It prevents all changes', 'It replaces computers'],
        'answer': 'A',
        'explanation': 'Software Engineering provides methods to develop and maintain complex systems effectively.',
        'exam': 'Software Engineering is important because it supports systematic development of reliable and maintainable software.'
    },
    {
        'question': 'What is the software crisis?',
        'options': ['Difficulty in developing reliable software within time and budget', 'Failure of computer hardware', 'Lack of programming languages', 'Shortage of internet connections'],
        'answer': 'A',
        'explanation': 'Software crisis refers to problems in developing quality software within the planned time and budget.',
        'exam': 'Software crisis refers to difficulties in developing reliable software within the specified time and budget.'
    },
]

# Import Python Unit 1 and Software Engineering Unit 1.
# Python Unit 2 questions are kept in the file but are NOT imported by this run.
question_sets = [
    ("Python Programming", "Unit 1: Introduction", questions),
    ("Software Engineering", "Unit 1: The Nature of Software & Software Engineering", software_unit1_questions),
]

db = None
cursor = None

try:
    db = get_db_connection()
    cursor = db.cursor()

    for subject_name, chapter_name, question_list in question_sets:
        added = 0
        skipped = 0

        for q in question_list:
            cursor.execute("""
                SELECT id
                FROM questions
                WHERE year = %s
                  AND subject = %s
                  AND chapter = %s
                  AND question = %s
                LIMIT 1
            """, ("3rd Year", subject_name, chapter_name, q["question"]))

            if cursor.fetchone():
                skipped += 1
                continue

            if len(q["options"]) != 4 or q["answer"] not in ("A", "B", "C", "D"):
                raise ValueError(f"Invalid question/options/answer: {q['question']}")

            cursor.execute("""
                INSERT INTO questions (
                    question, option_a, option_b, option_c, option_d,
                    correct_answer, created_by, year, subject, chapter,
                    explanation, exam_answer
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                q["question"],
                q["options"][0],
                q["options"][1],
                q["options"][2],
                q["options"][3],
                q["answer"],
                2,
                "3rd Year",
                subject_name,
                chapter_name,
                q["explanation"],
                q["exam"]
            ))
            added += 1

        cursor.execute("""
            SELECT COUNT(*)
            FROM questions
            WHERE year = %s AND subject = %s AND chapter = %s
        """, ("3rd Year", subject_name, chapter_name))
        total = cursor.fetchone()[0]

        print(f"Subject: {subject_name}")
        print(f"Unit: {chapter_name}")
        print("New questions added:", added)
        print("Duplicate questions skipped:", skipped)
        print("Total questions in this unit:", total)
        print("-" * 40)

    db.commit()
    print("All selected question sets processed successfully.")

except Exception as e:
    if db:
        db.rollback()
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if db:
        db.close()
