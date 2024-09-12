def mail_registration(username, code):
    email_data = {
        "email_body": "<div style='text-align: center;'>"
                      f"<span style='font-size: 18px' >Привет!"
                      f"</span><br><br>"
                      f"<span style='font-size: 18px'>Ваш код для активации аккаунта в Hotel KG:</span>"
                      f"<br><br>"
                      f"<b style='font-size: 25px'>{code}</b>"
                      "</div>",
        "to_email": f"{username}",
    }
    return email_data


def phone_registration(code):
    sms_data = f"Ваш код для активации аккаунта в Hotel KG: {code}"
    return sms_data

