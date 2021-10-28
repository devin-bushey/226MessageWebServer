from django.db import models
from django.core.exceptions import ValidationError

# PURPOSE:
# Given a key, check if it is alphanumeric
#
# PARAMETERS:
# key: is a string
#
# RETURN/SIDE EFFECTS:
# Raise django validation error if the key is not validated
#
def validate_key_alphanum(key):
    key = str(key)
    if not key.isalnum():
        raise ValidationError('Key is not alphanumeric', code='key_value')


# PURPOSE:
# Given a key, check if it's length is exactly 8 characters
#
# PARAMETERS:
# key: is a string
#
# RETURN/SIDE EFFECTS:
# Raise django validation error if the key is not validated
#
def validate_key_length(key):
    key = str(key)
    if len(key) != 8:
        raise ValidationError('Key must have a length of 8', code='key_length')


# PURPOSE:
# Given a key, check all of the other keys on the server to validate if it is unique
#
# PARAMETERS:
# key: is a string
#
# RETURN/SIDE EFFECTS:
# Raise django validation error if the key is not validated
#
def validate_key_unique(key):
    key = str(key)
    for msg in Message.objects.all():
        if str(msg.key) == key:
            raise ValidationError('Key already exists', code='duplicate')
    

# PURPOSE:
# Given a message, check if it is between 1-160 characters in length
#
# PARAMETERS:
# msg: is a string
#
# RETURN/SIDE EFFECTS:
# Raise django validation error if the msg is not validated
#
def validate_msg_length(msg):
    if len(msg) < 1 or len(msg) > 160:
        raise ValidationError('Message must have a length between 1-160', code='msg_length')
        
# PURPOSE:
# Create a Message model/class that consists of a key and a message
# key: string (char field) with a max length of 8 characters (user cannot enter more than 8 characters in the field)
# msg: string (text field)
#
# PARAMETERS:
# models.Model: django specific code used for setting up the model/mapping to database tables
#
# RETURN/SIDE EFFECTS:
# Call on itself returns the key and the message, separated by a semi colon, as a string
# Example "<key>: <msg>" 
#
# NOTES:
# key and msg are passed to the validation methods described in this file
# 
class Message(models.Model):
    key = models.CharField(primary_key=True,max_length=8, validators=[validate_key_alphanum, validate_key_length, validate_key_unique])
    msg = models.TextField(validators=[validate_msg_length])

    def __str__(self):
        #x = {"key": self.key, "msg": self.msg}
        #return json.dumps(x)
        return self.key + ": " + self.msg



