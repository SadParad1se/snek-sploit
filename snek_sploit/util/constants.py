# Response keys  (the comment says its possible types; probably unnecessary)
B_ID = b"id"  # str
B_PROMPT = b"prompt"  # str
B_BUSY = b"busy"  # bool
B_DATA = b"data"  # bytes
B_CONSOLES = b"consoles"  # list[dict[bytes, str | bytes | bool]]
B_TABS = b"tabs"  # list[bytes]
B_WROTE = b"wrote"  # int
B_TOKEN = b"token"  # bytes
B_TOKENS = b"tokens"  # list[bytes]
B_RESULT = b"result"  # bytes | dict[str, Any]
B_EXPLOITS = b"exploits"  # int
B_AUXILIARY = b"auxiliary"  # int
B_POST = b"post"  # int
B_ENCODERS = b"encoders"  # int
B_NOPS = b"nops"  # int
B_PAYLOADS = b"payloads"  # int | list[str]
B_EVASIONS = b"evasions"  # int
B_VERSION = b"version"  # str
B_RUBY = b"ruby"  # bytes
B_API = b"api"  # bytes
STATUS = "status"  # bytes
CRITICAL = "critical"  # bool
NAME = "name"  # str
STARTED = "started"  # str (datetime Y-m-d H:m:s TZ)/(2023-11-13 08:47:35 +0000)
PLUGINS = "plugins"  # list[str]
B_MODULES = b"modules"  # list[str]
B_TYPE = b"type"  # str | bytes
B_NAME = b"name"  # str
B_FULLNAME = b"fullname"  # str
B_RANK = b"rank"  # bytes
B_DISCLOSURE_DATE = b"disclosuredate"  # bytes
B_SESSIONS = b"sessions"  # list[???int???] TODO: unknown type
B_WAITING = b"waiting"  # list[bytes]
B_RUNNING = b"running"  # list[bytes]
B_RESULTS = b"results"  # list[bytes]
B_REQUIRED = b"required"  # bool
B_ADVANCED = b"advanced"  # bool
B_EVASION = b"evasion"  # bool
B_DESC = b"desc"  # bytes
B_DEFAULT = b"default"  # bytes
B_ENUMS = b"enums"  # list
JID = "jid"  # int
START_TIME = "start_time"  # int
DATASTORE = "datastore"  # dict[bytes, str]
B_JOB_ID = b"job_id"  # int
B_UUID = b"uuid"  # bytes
B_STATUS = b"status"  # bytes
B_ERROR = b"error"  # str
B_ENCODED = b"encoded"  # bytes

# Response values
B_SUCCESS = b"success"
B_FAILURE = b"failure"
B_UP = b"UP"
B_ERRORED = b"errored"
B_COMPLETED = b"completed"

# Other
ERRORED = "errored"
COMPLETED = "completed"
RUNNING = "running"
RESULT = "result"

# Error response keys
ERROR = "error"  # bool
ERROR_CLASS = "error_class"  # str
ERROR_STRING = "error_string"  # bytes
ERROR_BACKTRACE = "error_backtrace"  # list[str]
ERROR_MESSAGE = "error_message"  # bytes
