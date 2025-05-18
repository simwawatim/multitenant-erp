import secrets
import string
import random

def generate_user_username(request):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    selection_list = letters + digits + special_chars

    username_len = 4

    username = ''

    for i in range(username_len):
        username += ''.join(secrets.choice(selection_list))

    return username