# willy
An awesome webradio written in Python and AngularJS<br>
<br>
RESTful backend: REST endpoints SHALL be in the following format:<br>

| URL   |      Req      |  Body | Result |
|----------|:-------------|:------|:------|
| http://0.0.0.0/api/stations | GET  | *None* | Return all station |
| http://0.0.0.0/api/stations | POST  | JSON String | Adds a new station |
| http://0.0.0.0/api/stations/:id | GET  | *None* | Return a single station |
| http://0.0.0.0/api/stations/:id | POST  | JSON String | Updates the entry |
| http://0.0.0.0/api/stations/:id | DELETE  | *None* | Deletes a station |

# Installation
Before getting started, make sure you have Python 2.7 installed in your system. Install Flask using PIP python package manager.

<code>pip install flask</code>

# Features
* Radio streaming
* Local music streaming [clarify]
* Playlist management [NFC tags?]
