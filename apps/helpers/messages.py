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
    sms_data = f"Ваш код для активации аккаунта в Hotel KG: {code}"
    return sms_data
