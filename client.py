#!/usr/bin/env python3

import requests
import sys
import random
import string

KEY_LENGTH = 8
# GET response has the format "12345678: ABC12345This is a message"
KEY_LENGTH_SVR_FORMAT = KEY_LENGTH * 2 + len(": ")
BLANK = ''
OK = 200
URL = 'http://127.0.0.1:8000/msgserver/'
GET = 'get/'
CREATE = 'create/'

#
# PURPOSE:
# Given an array of command line arguments, validate whether there are the correct number of arguments
# and validate the key input
#
# PARAMETERS:
# 'args' is the array of command line arguments used when running the program
#
# RETURN/SIDE EFFECTS:
# Terminates the program if validation fails
#
# NOTES:
#
def validate_arguments(args):
    if len(sys.argv) != 2:
        print(f'{sys.argv[0]} needs a key to transmit')
        sys.exit(-1)

    key = args[1]

    if key.isalnum() == False:
        print('Key must be alphanumeric')
        sys.exit(-1)

    if len(key) != KEY_LENGTH:
        print(f'Key length must be {KEY_LENGTH}')
        sys.exit(-1)

#
# PURPOSE:
# Given an a key from the command line (assumed to be valid), print all associated messages in the thread, 
# then prompt the user for a new message. This new message will be paired with a randomly generated key
# Finally, the new message and key are sent to the server by a PUT request
#
# PARAMETERS:
# 'key' is a string, which is an argument from the commandline.
# Assume the key has been validated as an alphanumeric string with a length of 8
#
# NOTES:
# If there is a message returned from the server, assume that meesage consists of
# of an 8-character key and a message body
#
def client(key):
    get_result = send_get(key)
    # GET response has the format "12345678: ABC12345This is a message"
    msg = get_result.strip()[KEY_LENGTH_SVR_FORMAT:]
    while len(msg) > 0:
        key = get_result.strip()[KEY_LENGTH + len(": "):KEY_LENGTH_SVR_FORMAT]
        print(f'Message: {msg}')
        get_result = send_get(key)
        msg = get_result.strip()[KEY_LENGTH_SVR_FORMAT:]
    
    next_key = ''.join(random.choices(string.digits, k=KEY_LENGTH))

    new_msg = input(f'Please enter a message for key {next_key}: ')
    new_msg = next_key + new_msg

    send_post(key, new_msg)

#
# PURPOSE:
# Given a valid key, send a GET request with given key to the server
#
# PARAMETERS:
# 'key' is a string which is the key to be sent to the server
#
# RETURN/SIDE EFFECTS:
# Returns the response by the server. If the response does not have a 200 status code, return blank
# Assume GET response has the format "12345678: ABC12345This is a message"
#
# NOTES:
#
def send_get(key):
    #print('[SEND GET]')
    client = requests.session()
    url = URL + GET + key
    client.get(url)
    
    r = requests.get(url)

    if r.status_code == OK:
        return r.text

    return BLANK


#
# PURPOSE:
# Given a valid key and message, send a POST request with given key and message to the server
# to create a new key/message on the server
#
# PARAMETERS:
# 'key' is a string which is the key to be sent to the server
# 'msg' is the associated message for the key
#
# RETURN/SIDE EFFECTS:
# Returns the response by the server, which is in the following format:
# <key>: <msg> --> example: 123456AB: This is a message
#
# NOTES:
# Requires csrf token validation 
#
def send_post(key, msg):
    #print('[SEND POST]')
    client = requests.session()
    url = URL + CREATE
    client.get(url)

    if 'csrftoken' in client.cookies:
        #print('Token Found')
        elements = { 
                'key': key, 
                'msg': msg,
                'csrfmiddlewaretoken':client.cookies['csrftoken']
                }
        post = client.post(url, data = elements, headers = {'Referer' : url})


#
# MAIN
#
validate_arguments(sys.argv)
client(sys.argv[1])




