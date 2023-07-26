# ChatGPTBot
Contains implementation of ChatGPTBotAPI class with all specified methods for assessment purpose

# Flask API
In order to run flask api on local server, execute this command

`python3 ./PythonAssesment/flaskapp/run.py`

# Documentation

## Base URL
`http://127.0.0.1:5000`

## 1. Create Prompt
### Route: `/createprompt` (POST)
This route allows you to create a new prompt by providing the InputPrompt parameter as a string. Upon successful creation, the API will respond with a Response message indicating the status of the operation
### JSON Schema:
```json
{
  "type": "object",
  "properties": {
    "InputPrompt": {"type": "string"}
  },
  "required": ["InputPrompt"],
  "additionalProperties": False
}
```

## 2. Get Response
### Route: `/getresponse` (POST) 
Use this route to get the response associated with a specific prompt index. Provide the Index parameter as an integer representing the prompt's index. The API will return the corresponding Response for the given index.
### JSON Schema:
```json
{
  "type": "object",
   "properties": {
       "Index": {"type": "number"}
   },
   "required": ["Index"],
   "additionalProperties": False
}
```

## 3. Update Prompt
### Route: `/updateprompt` (POST)
This route allows you to update an existing prompt by providing both the Index (the index of the prompt to be updated) and the InputPrompt (the new string for the prompt). The API will respond with a Response message indicating the status of the update operation.
### JSON Schema:
```json
{
  "type": "object",
   "properties": {
       "Index": {"type": "number"},
       "InputPrompt": {"type": "string"}
   },
   "required": ["Index", "InputPrompt"],
   "additionalProperties": False
}
```

## 4. Delete Prompt
### Route: `/deleteprompt` (POST)
Use this route to delete a prompt by providing its Index as an integer. The API will remove the prompt and respond with a Response message indicating the status of the delete operation
### JSON Schema:
```json
{
  "type": "object",
   "properties": {
       "Index": {"type": "number"}
   },
   "required": ["Index"],
   "additionalProperties": False
}
```
## Error Handling
If any error occurs during the API calls, the response will include relevant error information to assist with debugging. Also you can see logs stored at `PythonAssesment/flaskapp/logs`

