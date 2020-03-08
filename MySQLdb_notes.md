# Notes on MySQLdb (for Python 2):

```
$ sudo apt install python-mysqldb

# ...

$ python
Python 2.7.15+ (default, Oct  7 2019, 17:39:04) 
[GCC 7.4.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import MySQLdb as ms
>>> db=ms._mysql.connect('127.0.0.1', 'root', 'mypasswd', 'trdb')
>>> db.query('SELECT name FROM users WHERE id < 8')
>>> res = db.store_result()
>>> res.fetch_row()
(('John Richard Lynch',),)
>>> res.fetch_row(maxrows=0, how=1)
({'name': 'Albert Einstein'}, {'name': 'Liam Corkery'}, {'name': 'Kermit the Frog'}, {'name': 'Zaphod Beeblebrox'}, {'name': 'Nelson Mandela'}, {'name': 'Father Ted'})
>>> db.query('SELECT country FROM results WHERE country LIKE `Spain`')
>>> db.query("SELECT country FROM results WHERE country LIKE 'Spain'")
>>> s_lands = db.store_result()
>>> s_lands.fetch_row(maxrows=0, how=1)
({'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'})
>>> db.query("SELECT country FROM results WHERE country LIKE 'S'")
>>> s_lands = db.store_result()
>>> s_lands.fetch_row(maxrows=0, how=1)
()
>>> db.query("SELECT country FROM results WHERE country LIKE 's'")
>>> s_lands = db.store_result()
>>> s_lands.fetch_row(maxrows=0, how=1)
()
>>> db.query("SELECT country FROM results WHERE country LIKE '^s%'")
>>> s_lands = db.store_result()
>>> s_lands.fetch_row(maxrows=0, how=1)
()
>>> db.query("SELECT country FROM results WHERE country LIKE 'S%'")
>>> s_lands = db.store_result()
>>> s_lands.fetch_row(maxrows=0, how=1)
({'country': 'Switzerland'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Sweden'}, {'country': 'Sweden'}, {'country': 'Spain'}, {'country': 'Switzerland'}, {'country': 'Switzerland'}, {'country': 'Switzerland'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Sweden'}, {'country': 'Singapore'}, {'country': 'Spain'}, {'country': 'Spain'}, {'country': 'Singapore'}, {'country': 'Singapore'}, {'country': 'Singapore'}, {'country': 'Spain'}, {'country': 'Singapore'}, {'country': 'Singapore'}, {'country': 'Singapore'}, {'country': 'Spain'}, {'country': 'Singapore'}, {'country': 'Switzerland'}, {'country': 'Singapore'})
>>> 
``` 