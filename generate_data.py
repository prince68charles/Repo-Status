import json
import random
from datetime import datetime, timedelta
import string

#Storage of commits
commits = []

AUTHORS = ["Alice", "Bob", "Alex", "David", "Danny", "Xander "]


for i in range(0, 200):

    #Fake commit message

    commit = {

        "sha": ''.join(random.choices(string.hexdigits.lower(), k=7)),
        "author": random.choices(AUTHORS),
        "timestamp": (datetime.now() - timedelta(random.randint(0,90))).isoformat(),
        "lines-added": random.randint(0,500),
        "files-changed": random.randint(1,15),
        "lines-deleted": random.randint(0,300),
        "message": "Added ..."
        

    }

    commits.append(commit)

with open ("data.json", "w") as file:

    json.dump(commits, file, indent=4)

