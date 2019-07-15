"""A little program that spits out technobabble. It would be fun to continue adding to it to make it more and more awesome."""

import json
import random
import os
import time

boot_file = "boot.json"
mainframe_file = "mainframe.json"

time_standard = 0.2


def extract_json_data(file):
    try:
        return json.loads(open(file).read())

    except:
        print("File error: json file not found.")


def print_messages_with_time_gaps(messages, t):
    for message in messages:
        print(message)
        time.sleep(t)


def shuffle(data):
    random.seed = os.urandom(1024)
    return random.shuffle(data)


def main():
    # Load .json and other data files into program.
    boot_data = extract_json_data(boot_file)
    mainframe_data = extract_json_data(mainframe_file)

    # Display the boot sequence.
    print_messages_with_time_gaps(shuffle(boot_data), time_standard)

    # Display hacking messages.
    print_messages_with_time_gaps(shuffle(mainframe_data), time_standard)


if __name__ == "__main__":
    main()
