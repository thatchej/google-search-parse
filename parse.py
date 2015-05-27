import json
import os

new_file = open("searches.txt", 'w+')

for subdir, dirs, files in os.walk('.'):
    for file in files:
        if ".py" not in file:
            data = json.load(open(file))
            for i in range(0, len(data["event"])):
                new_file.write(data["event"][i]["query"]["query_text"].encode('utf-8') + "\n")

            

