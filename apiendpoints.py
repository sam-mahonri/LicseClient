from samenv import getenv

LICSE_VERIFY_SSL = getenv('LICSE_FLASK_VERSSL')
LICSE_API_LINK = getenv('LICSE_API_LINK')

LICSE_GET_CURRENT_USER = LICSE_API_LINK + "/licsedb/user/read"
LICSE_LOGIN = LICSE_API_LINK + "/auth/login"
LICSE_REGISTER = LICSE_API_LINK + "/auth/register"
LICSE_SENDEMAIL_VER = LICSE_API_LINK + "/auth/send_email_verification"

