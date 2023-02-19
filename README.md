# Explanation

It is a framework in Python language that serves for a web application. This project is a simple text manipulation application that allows the user to perform certain text operations.

The codes in the project provide various functions (letter_counter, word_counter, sentence_counter, most_frequent_character, scan_letter, scan_word, scan_sentence, remove_letter, remove_word, remove_sentence, remove_space, remove_newline) to analyze the texts entered by the user and present the results to the user.

These functions allow to scan the number of letters, words, sentences in the text, the most frequently used character, a specific letter, word or phrase, remove letters, words, sentences, spaces or new lines. Flask allows users to analyze their text and view the results using these functions.

In addition, this project provides a web interface for the texts that users enter, allowing them to perform text manipulation directly in their web browser. This project might start out as a simple text processing application, but with Flask's scalable nature, it can be expanded into a larger application with more advanced functionality added in the future.

# Flow Diagram
    +--------+        +-------------+        +------------+        +----------+
    | index  | -----> | letter.html | -----> | /letter    | -----> | Letter   |
    +--------+        +-------------+        +------------+        +----------+

    +--------+        +-----------+        +-----------+        +--------+
    | index  | -----> | word.html | -----> | /word    | -----> | Word   |
    +--------+        +-----------+        +-----------+        +--------+

    +--------+            +---------------+            +----------------+        +---------+
    | index  | ---------> | sentence.html | ---------> | /sentence      | -----> | Sentence|
    +--------+            +---------------+            +----------------+        +---------+

    +--------+             +----------------------+             +---------------+        +-------------+
    | index  | ----------> | most-frequent-word.html| ----------> | /most-word-numbers|-----> | Frequent    |
    +--------+             +----------------------+             +---------------+        +-------------+

    +--------+             +-----------------------+             +-------------+        +----------+
    | index  | ----------> | scan-letter.html       | ----------> | /scan-letter|-----> | ScanLetter|
    +--------+             +-----------------------+             +-------------+        +----------+

    +--------+             +-----------------------+             +-------------+        +--------+
    | index  | ----------> | scan-word.html         | ----------> | /scan-word  |-----> | ScanWord|
    +--------+             +-----------------------+             +-------------+        +--------+

    +--------+             +--------------------------+             +---------------+        +--------------+
    | index  | ----------> | scan-sentence.html        | ----------> | /scan-sentence|-----> | ScanSentence |
    +--------+             +--------------------------+             +---------------+        +--------------+

    +--------+             +------------------------+             +---------------+        +--------------+
    | index  | ----------> | remove-letter.html      | ----------> | /remove-letter|-----> | RemoveLetter |
    +--------+             +------------------------+             +---------------+        +--------------+

    +--------+             +------------------------+             +-------------+        +------------+
    | index  | ----------> | remove-word.html        | ----------> | /remove-word|-----> | RemoveWord |
    +--------+             +------------------------+             +-------------+        +------------+

    +--------+             +---------------------------+             +----------------+        +-----------------+
    | index  | ----------> | remove-sentence.html       | ----------> | /remove-sentence|-----> | RemoveSentence |
    +--------+             +---------------------------+             +----------------+        +-----------------+

    +--------+             +------------------------+             +-------------+        +--------------+
    | index  | ----------> | remove-space.html       | ----------> | /remove-space|-----> | RemoveSpace |
    +--------+             +------------------------+             +-------------+        +--------------+

    +--------+             +---------------------------+             +------------------+        +-----------------+
    | index  | ----------> | remove-newline.html        | ----------> | /remove-newline|-----> | RemoveNewLine |
    +--------+             +---------------------------+             +------------------+        +-----------------+

The continuation of the flow diagram contains other operations that the user can do. The user can search for any letter or word in the text. This is done on the "Scan Letter", "Scan Word" and "Scan Sentence" pages.

- On the "Scan Letter" page, it counts the number of times the user wants the letter in the text. The user can count by entering the letter he entered.

- On the "Scan Word" page, it counts the number of times the user wants the word in the text. User can count by entering the word entered.

- On the "Scan Sentence" page, it counts the number of times the sentence requested by the user occurs in the text. The user can count by entering the sentence he entered.

The user can remove unwanted letters, words or sentences from the text. This is done on the "Remove Letter", "Remove Word" and "Remove Sentence" pages.

- On the "Remove Letter" page, the user's desired letter is removed from the text.

- On the "Remove Word" page, the user's desired word is removed from the text.

- On the "Remove Sentence" page, the user's desired sentence is removed from the text.

- On the "Remove Space" page, the user removes the spaces in the text.

- On the "Remove Newline" page, the user removes the carriage return in the article.

The result of all operations, the user sees the result on the "Result" page.

# UML Class Diagram
    +---------------------------------+
    |              Routes             |
    +---------------------------------+
    | index()                         |
    | letter()                        |
    | word()                          |
    | sentence()                      |
    | most_word()                     |
    | scan_letter()                   |
    | scan_word()                     |
    | scan_sentence()                 |
    | remove_letter()                 |
    | remove_word()                   |
    | remove_sentence()               |
    | remove_space()                  |
    | remove_newline()                |
    +---------------------------------+
                /|\
                |
    +--------------+----------------+
    |              |                |
    |     Counters |   MostFrequent |
    |              |                |
    +--------------+----------------+
    | letter_counter()              |
    | word_counter()                |
    | sentence_counter()            |
    +--------------------------------+
    | most_frequent_character()      |
    +--------------------------------+
                /|\
                |
    +--------------+----------------+
    |              |                |
    |         Scanners              |
    |              |                |
    +--------------+----------------+
    | scan_letter()                 |
    | scan_word()                   |
    | scan_sentence()               |
    +-------------------------------+
                /|\
                |
    +--------------+----------------+
    |              |                |
    |          Removers             |
    |              |                |
    +--------------+----------------+
    | remove_letter()               |
    | remove_word()                 |
    | remove_sentence()             |
    | remove_space()                |
    | remove_new_line()             |
    +--------------------------------+

This diagram shows the classes, methods and relationships between them in the Flask application. The Routes class contains the web application's routers and determines which page the user will access. The Counters class includes the letter_counter(), word_counter() and sentence_counter() methods required to count the number of words, letters, and sentences. The MostFrequent class includes the most_frequent_character() method to find the most frequently used character.

The Scanners class includes the scan_letter(), scan_word(), and scan_sentence() methods to enable the user to search for a specific letter, word, or phrase. The Removers class includes the remove_letter(), remove_word(), remove_sentence(), remove_space(), and remove_new_line() methods to remove the user's skipping of a letter, word, sentence, space, or line.

# Install
This file indicates that the application has a dependency on the Flask web framework version and that version will be installed. You can store this file in a separate text file and use the command <b>pip install -r requirements.txt</b> to start the application.
# How Do I Run
    #!bin/bash
    git clone https://github.com/Batuhanaydn/simple-string-editor.git
    cd simple-string-editor
    pip install -r requirements.txt
    python main.py
or

    git clone https://github.com/Batuhanaydn/simple-string-editor.git
    cd simple-string-editor
    ./run.sh

# Follow Me
<p>You can follow me on my social media accounts below:</p><ul><li>GitHub: <a href="https://github.com/batuhanaydn">Batuhanaydn</a></li><li>Twitter: <a href="https://twitter.com/telumak" target="_new">@telumak</a></li><li>LinkedIn: <a href="https://www.linkedin.com/in/batuhan-aydinn/" target="_new">Muhammed Batuhan Aydın</a></li></ul><p>You can easily access my articles, projects and posts, follow me and stay in touch with me...</p>
