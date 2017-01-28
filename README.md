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
