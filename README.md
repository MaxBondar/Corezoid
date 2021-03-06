# Corezoid SDK for Python 3.x
This module helps you sending and modifying tasks to Corezoid processes.

## Installation
```
pip install Corezoid
```

## Requirements 
```
pip install requests
```

## Quick Start
```
from Corezoid import Corezoid

# Insert Corezoid Process credentials
# Learn more about credentials: https://doc.corezoid.com/en/interface/access_management.html
API_KEY    = '<INSERT API KEY>' 
API_SECRET = '<INSERT API SECRET>'
PROCESS_ID = '<INSERT PROCESS ID>'

# Initialize Corezoid SDK
c = Corezoid(API_KEY, API_SECRET, PROCESS_ID)

# There are 2 methods available: send and modify tasks.
# Learn more about Corezoid API: https://doc.corezoid.com/en/api/upload_data/

# Input parameters:
# ref: string
# data: JSON

# Send a new task to Corezoid process
def send_task(ref, data):
    c.create_task(ref, data)

# Modify an existing task by ref at Corezoid process
def modify_task(ref, data):
    c.modify_task(ref, data)

```

## Important Notes
Max. task size: __128 000 bytes__.
If you have a large __data__ object try to split it into a few tasks.

### That's it! Let's start using Corezoid.


