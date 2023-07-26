HOST = "127.0.0.1"
PORT = "5000"
OPENAI_KEY = ""

PROMPT_SCHEMA = {"type": "object",
                 "properties": {
                     "InputPrompt": {"type": "string"}
                 },
                 "required": ["InputPrompt"],
                 "additionalProperties": False}

RESPONSE_SCHEMA = {"type": "object",
                   "properties":{},
                   "required":[],
                   "additionalProperties": False
                   }

UPDATE_SCHEMA = {"type": "object",
                 "properties": {
                     "Index": {"type": "number"},
                     "InputPrompt": {"type": "string"}
                 },
                 "required": ["Index", "InputPrompt"],
                 "additionalProperties": False}

DELETE_SCHEMA = {"type": "object",
                 "properties": {
                     "Index": {"type": "number"}
                 },
                 "required": ["Index"],
                 "additionalProperties": False}
