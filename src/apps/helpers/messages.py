from django.template.loader import render_to_string

logo_url = "https://i.postimg.cc/Z5XmrWds/logo.png"


def mail_registration(username, code):
    email_data = {
        "to_email": f"{username}",
        "email_body": render_to_string("accounts/register_code_email.html",
                                       {
                                           "data": {
                                               "username": username,
                                               "code": code,
                                               "logo": logo_url
                                           }
                                       }),
    }
    return email_data


def phone_registration(code):
    sms_data = f"Ваш код для активации аккаунта в Business KG: {code}"
    return sms_data


def mail_forgot(email, password):
    email_data = {
        "to_email": f"{email}",
        "email_body": render_to_string("accounts/forgot_password_email.html",
                                       {
                                           "data": {
                                               "email": email,
                                               "code": password,
                                               "logo": logo_url
                                           }
                                       }),
    }
    return email_data

def phone_forgot(password):
    sms_data = f"Ваш новый пароль аккаунта в Business KG: {password}"
    return sms_data