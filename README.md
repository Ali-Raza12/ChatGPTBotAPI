# ChatGPTBot
Contains implementation of ChatGPTBotAPI class with all specified methods for assessment purpose

# Flask API Documentation
In order to run flask api on local server, execute this command

`python3 ./PythonAssesment/flaskapp/run.py`

## 1. Configuration
You can specify the Host Address, Port and OPENAI API key in `config.py` file. This file is located at `PythonAssesment/flaskapp/app/config.py`
### Base URL
By default the base url is set to `http://127.0.0.1:5000`

## 2. Create Prompt
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

## 3. Get Response
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

## 4. Update Prompt
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

## 5. Delete Prompt
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
## 6. Error Handling
If any error occurs during the API calls, the response will include relevant error information to assist with debugging. Also you can see logs stored at `PythonAssesment/flaskapp/logs`

