"""
# 1. Consistency & Indentation:
  - The most important thing is to be consistent throughout your project. For 
  example: If you decide to use tabs with 2 spaces, make sure that all developers 
  on the project follow this convention.
  - In Python, you can use quotes in the following ways: ' ', " ", or """ """.
  - Basically, you can use in addition to these ways: ' " " ' and " ' ' ".
  - For formatting strings, it is recommended to use: " ".
  - Keep consistency throughout your code.
  - Follow the guidelines of your project's style guide, if there is one.
  - I personally prefer 2 tabs, as well as using a formatter and line breaks.
  - PEP 8, which is the official style guide for Python, recommends using 4 spaces 
  per indentation level to avoid mixing spaces and tabs.
  - Here are some reasons to follow this practice:
    1. Consistency: Using a fixed number of spaces for indentation helps keep code 
       consistent and readable, making it easier for different developers to 
       collaborate.
    2. Avoiding Errors: Mixing spaces and tabs can lead to indentation errors, 
       which are common in Python, since the language relies on indentation to 
       define code blocks.
    3. Readability: Using 4 spaces is a widely accepted convention in the Python 
       community, making code easier to read and understand for other developers 
       who are familiar with this practice.
    4. Formatting Tools: Many code formatting tools and text editors are 
       configured to use 4 spaces by default, which makes it easier to maintain 
       your coding style.
  - Always use descriptive variable and function names.
  - Use reduced forms of conditionals.
  - Comment carefully, and consider whether to use block comments or objective 
    comments.

# 2. Naming & Comments:
  - Option one - Use `snake_case` for variable and function names. Example: 
    `my_variable`, `calculate_average()`.
  - Option two - use `CamelCase` for class names. Example: `MyClass`.
  - Avoid: using special characters, numbers at the beginning of the variable 
    name, uppercase at the beginning / throughout the variable.
  - Use the code spell checker extension to help you avoid spelling mistakes.
  - Be clear; when choosing a name; naming what the variable does is essential 
    for the readability and maintainability of the code. Descriptive variable 
    names help other developers (or yourself in the future) to quickly 
    understand the purpose of the variable without having to decipher its 
    content or logic.
  - For example, instead of using generic names like `x` or `temp`, prefer 
    names like `usercounter` or `totalprice`. This makes the code more 
    intuitive and makes it easier to identify errors or implement new features. 
    In addition, following naming conventions, such as using `snake_case` for 
    variables in Python, contributes to code consistency and clarity.
  - Use comments only when necessary; when used incorrectly, they hinder more 
    than they help.
  - To explain parts of the code that may not be immediately clear, use `#` 
    for single-line comments and """ """ or ''' ''' for docstrings.

# 3. Code Structure & Avoid Duplicate Code:
  - Maintain a clear and organized structure.
  - Organize your imports at the beginning of the file. Follow the order: 
    standard libraries, third-party libraries, and finally your own libraries.
  - Separate functions and classes into modules and files as needed. If your 
    code is too large, it probably has more than one responsibility, which 
    violates the single responsibility rule of the **Single Responsibility 
    Principle (SRP)**, one of the fundamental principles of software design.
  - The SRP states that a class or module should have only one reason to change; 
    that is, it should have a single responsibility. When a file or module 
    contains many functions or classes that handle different responsibilities, 
    this can lead to code that is harder to understand, test, and maintain.
  - By dividing your code into smaller, more cohesive modules, you improve the 
    readability and maintainability of your project. In addition, this makes it 
    easier to reuse code and apply unit tests, since each module can be tested 
    in isolation. Therefore, whenever you notice that a file is becoming too 
    large or complex, consider refactoring it into smaller parts that focus on 
    specific responsibilities.
  - If you find yourself repeating code, consider creating functions or classes 
    to reuse that code. Not only does duplicating code make your program longer 
    and harder to maintain, it also increases the likelihood of errors. When 
    you need to make a change, you have to remember to update every instance of 
    the duplicated code, which can lead to inconsistencies and bugs.
  - By encapsulating repeated logic in functions or classes, you promote reuse 
    and modularity. This makes it easier to maintain, since any necessary 
    changes can be made in one place. Additionally, well-named functions and 
    classes can improve the readability of your code, making it easier for 
    other developers (or yourself in the future) to understand what the code 
    does.
  - For example, if you have a block of code that calculates the total price 
    of a product in multiple parts of your program, create a function called 
    `calculate_total_price`. That way, you can call this function whenever you 
    need to perform that calculation, instead of repeating the same code over 
    and over again. This not only reduces the amount of code, but also makes 
    your program more organized and easier to understand.

# 4. Avoid over-engineering
  - Simplicity is the ultimate state of sophistication. Of course, don’t 
    simplify to the point of incomprehensibility or vice versa. The goal is to 
    find a balance between simplicity and functionality.
  - Over-engineering occurs when you add unnecessary complexity to your code, 
    creating complicated solutions to simple problems. This can result in code 
    that is difficult to understand, maintain, and test. Instead, look for 
    solutions that meet the requirements of the problem clearly and directly.
  - On the other hand, over-simplifying can lead to a lack of clarity or 
    solutions that do not fully meet the needs of the project. It is important 
    to ensure that the solution is sufficiently robust and understandable, 
    without becoming overly complex.
  - Therefore, when designing your code, always ask yourself whether the 
    solution is as simple as possible, but still effective. Aim for clarity 
    and readability, and don't hesitate to refactor your code to make it 
    simpler and more straightforward, while still maintaining the necessary 
    functionality.

# 5. Error Handling:
  - Use exceptions to handle errors appropriately. Use `try`, `except`, 
    `finally` to manage exceptions. It is crucial to stay calm and try to 
    understand the root cause of the error by analyzing the logs.
  - When an error occurs, instead of allowing the program to crash abruptly, 
    using exceptions allows you to catch the error and take appropriate action. 
    The `try` block is where you place code that can throw an exception, while 
    the `except` block is where you handle the exception, allowing the program 
    to continue execution or providing a user-friendly error message.
  - The `finally` block is useful for ensuring that certain actions are 
    performed regardless of whether or not an exception occurred, such as 
    closing files or releasing resources.
  - Analyzing logs is a fundamental part of the debugging process. Logs can 
    provide valuable information about what was happening at the time the 
    error occurred, helping you identify the root cause. By understanding the 
    context of the error, you can implement more effective solutions and 
    prevent the same from happening again in the future.
  - Remember that exception handling should not be a way to ignore errors. 
    Instead, it should be a way to manage errors in a controlled and 
    informative way, ensuring that your code is robust and reliable.

# 6. Documentation:
  - Document your code effectively. This helps other developers (and yourself 
    in the future) understand what the code does. Good documentation is 
    essential for the maintainability and scalability of a project, as it 
    provides context and explanations about the logic and functionality of the 
    code.
  - Use clear and concise comments to explain code snippets that may be 
    complex or unintuitive. Avoid obvious comments that don't add value, but 
    focus on clarifying the intent behind specific design decisions or 
    implementations.
  - In addition to comments, consider using docstrings to document functions, 
    classes, and modules. Docstrings allow you to provide information about the 
    parameters, return values, and expected behavior of a function, making it 
    easier to understand its use. This is especially useful when other people 
    (or yourself) use libraries or modules that you have written.
  - Keep your documentation up to date as your code evolves. Outdated 
    documentation can be more harmful than no documentation at all, as it can 
    lead to misunderstandings and errors.
  - Finally, consider using documentation generation tools, such as Sphinx or 
    MkDocs, to create more formal and accessible documentation for your 
    project. This can include usage guides, examples, and references, making 
    your code more user-friendly and accessible to other developers.

"""
