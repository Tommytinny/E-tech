#!/usr/bin/python3


class User(BaselModel):
    """ User Details
    Attributes:
        first_name (str): User first name.
        last_name (str): User last name.
        email (str): User email address.
        password (str): User password.
        position (str): User position.
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
    position = ""
