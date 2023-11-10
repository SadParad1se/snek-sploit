# Response keys
ID = b"id"  # str
PROMPT = b"prompt"  # str
BUSY = b"busy"  # bool
DATA = b"data"  # bytes
CONSOLES = b"consoles"  # list[dict[bytes, str | bytes | bool]]
TABS = b"tabs"  # list[bytes]
WROTE = b"wrote"  # int
TOKEN = b"token"  # bytes
TOKENS = b"tokens"  # list[bytes]
RESULT = b"result"  # bytes

# Response values
SUCCESS = b"success"  # -
FAILURE = b"failure"  # -

# Error response keys
ERROR = "error"  # bool
ERROR_CLASS = "error_class"  # str
ERROR_STRING = "error_string"  # bytes
ERROR_BACKTRACE = "error_backtrace"  # list[str]
ERROR_MESSAGE = "error_message"  # bytes
