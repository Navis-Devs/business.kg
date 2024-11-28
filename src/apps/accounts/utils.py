import re


def check_username(username):
    if username.startswith('+'):
        return {"type": "phone", "data": "+" + "".join(filter(str.isdigit, username))}
    return {"type": "email", "data": username.lower()}
    # if re.match(r'[\w\.-]+@[\w\.-]+', username):
    #     return {"type": "email", "data": username.lower()}

    # if re.match(r'\+996 \(\d{3}\) \d{2}-\d{2}-\d{2}', username):
    #     return {"type": "phone", "data": "+" + "".join(filter(str.isdigit, username))}

    # return False

# Format - +996 (220) 16-18-25 == +996220161825
