
import json
import random
import os
import time

def extract_json_data():
    try:
        stored_data = json.loads(open("mainframe_data.json").read())
        return stored_data

    except:
        print("File error: json file not found.")

def main():
    #Extract data from file.
    kernel_messages = extract_json_data()
    
    # Randomize and shuffle the messages.
    random.seed = (os.urandom(1024))
    random.shuffle(kernel_messages)
    
    for message in kernel_messages:
        print(message)
        time.sleep(0.2)


main()
