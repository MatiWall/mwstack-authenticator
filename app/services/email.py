import resend

from app.settings import config

def send_email(to_email: str, subject: str, body: str):
    
    resend.api_key = config.resend_token
    
    params: resend.Emails.SendParams = {
        "from": "MWStack <no-reply@mwstack.org>",
        "to": [to_email],
        "subject": subject,
        "html": body
        }
    
    email = resend.Emails.send(params)