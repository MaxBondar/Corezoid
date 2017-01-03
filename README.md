# Corezoid SDK for Python 3.x
======
This module helps you sending and modifying tasks to Corezoid processes.
------------------------------------------------------------------------
# Usage
```
from Corezoid import Corezoid

# Insert Corezoid Process credentials
# Learn more how to get the credentials: https://doc.corezoid.com/en/interface/users_groups.html
API_KEY    = '<INSERT API KEY>' 
API_SECRET = '<INSERT API SECRET>'
PROCESS_ID = '<INSERT PROCESS ID>'

c = Corezoid(API_KEY, API_SECRET, PROCESS_ID)

def send_task(ref, data):
    # ref: string. Can be a custom param. By default it's timestamp. 
    # data: JSON. Must be a JSON object.
  
    c.create_task(ref, data)


def modify_task(ref, data):
    # ref: string. Can be a custom param. By default it's timestamp. 
    # data: JSON. Must be a JSON object.

    c.modify_task(ref, data)

```

That's it! 
Let's start using Corezoid.


