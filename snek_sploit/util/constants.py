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
EXPLOITS = b"exploits"  # int
AUXILIARY = b"auxiliary"  # int
POST = b"post"  # int
ENCODERS = b"encoders"  # int
NOPS = b"nops"  # int
PAYLOADS = b"payloads"  # int
EVASIONS = b"evasions"  # int
VERSION = b"version"  # str
RUBY = b"ruby"  # bytes
API = b"api"  # bytes
STATUS = "status"  # bytes
CRITICAL = "critical"  # bool
NAME = "name"  # str
STARTED = "started"  # str (datetime Y-m-d H:m:s TZ) | (2023-11-13 08:47:35 +0000)

# Response values
SUCCESS = b"success"  # -
FAILURE = b"failure"  # -
UP = b"UP"  # -

# Error response keys
ERROR = "error"  # bool
ERROR_CLASS = "error_class"  # str
ERROR_STRING = "error_string"  # bytes
ERROR_BACKTRACE = "error_backtrace"  # list[str]
ERROR_MESSAGE = "error_message"  # bytes
