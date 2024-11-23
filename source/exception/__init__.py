class TooManyRequestException(Exception):
    def __str__(self):
        return "Too Many Request"


class UnauthorizedException(Exception):
    def __str__(self):
        return "401 Unauthorized"


class NoCookiesAvailableException(Exception):
    def __str__(self):
        return "No Cookies Available"


class UnknownAuthenticationException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class MediaNotAvailableException(Exception):
    def __str__(self):
        return "Media not available"


class CommentIsUnavailable(Exception):
    def __str__(self):
        return "Comment is unavailable"


class NotFoundException(Exception):
    def __str__(self):
        return "Link not found"


class CookiesIncorrectException(Exception):
    def __str__(self):
        return "Cookies incorrect"


class TokenException(Exception):
    def __init__(self, error):
        super(TokenException, self).__init__(error.get("message"))
        self.message = error.get("message")
        self.type = error.get("type")
        self.code = error.get("code")
        self.error_subcode = error.get("error_subcode")
        self.error_user_title = error.get("error_user_title")
        self.error_user_msg = error.get("error_user_msg")
        self.fbtrace_id = error.get("fbtrace_id")
        self.sleep = error.get("sleep")
