import jsonschema
import traceback
import json
from flask import jsonify, request
from app import app
from app import config
from src.chatgptbot import ChatGPTBotAPI
from src.logger import SetupLogging


bot = ChatGPTBotAPI(openai_api_key=config.OPENAI_KEY)
app_log = SetupLogging()


@app.errorhandler(404)
def route_not_found(err):
    return jsonify({"Error": "Route not found"}), 404


@app.route("/createprompt", methods=['POST'])
def create_prompt():
    """Stores the prompt provided by user in a list
    Input Params:
        JSON - {"InputPrompt": str}
    Returns:
        JSON - {"Response": str}
    """
    try:
        data = json.loads(request.get_data(as_text=True))
        jsonschema.validate(instance=data, schema=config.PROMPT_SCHEMA)
        status = bot.create_prompt(prompt=data['InputPrompt'])
        if status:
            print(bot.input_prompt_list)
            return jsonify({"Response": "Prompt Saved Successfully"}), 200
        else:
            return jsonify({"Error": "Prompt must be a string"}), 400

    except json.JSONDecodeError:
        return jsonify({"Error": "Invalid JSON syntax"}), 400
    except jsonschema.ValidationError as e:
        return f"{e}", 400
    except Exception:
        app_log.log.error(
            f"Exception occured in create_prompt():\n{traceback.format_exc()}")
        return jsonify({"Error": "Internal Server Error"}), 500


@app.route("/getresponse", methods=['POST'])
def get_response():
    """Returns response from OpenAI API based on provided prompt
    Input Params:
        JSON - {"Index": int}
    Returns:
        JSON - {"Response": str}
    """
    try:
        data = json.loads(request.get_data(as_text=True))
        output = bot.get_response(prompt_index=data['Index'])
        return jsonify({"Response": output})
    
    except json.JSONDecodeError:
        return jsonify({"Error": "Invalid JSON syntax"}), 400
    except jsonschema.ValidationError as e:
        return f"{e}", 400
    except Exception:
        app_log.log.error(
            f"Exception occured in get_response():\n{traceback.format_exc()}")
        return jsonify({"Error": "Internal Server Error"}), 500


@app.route("/updateprompt", methods=['POST'])
def update_prompt():
    """Updates the prompt at provided index of list
    Input Params:
        JSON - {"Index": int, "InputPrompt": str}
    Returns:
        JSON - {"Response": str}
    """
    try:
        data = json.loads(request.get_data(as_text=True))
        jsonschema.validate(instance=data, schema=config.UPDATE_SCHEMA)
        status = bot.update_prompt(
            prompt_index=data['Index'], new_prompt=data['InputPrompt'])
        if status == 0:
            print(bot.input_prompt_list)
            return jsonify({"Error": "Provided Index must be an integer"}), 400
        elif status == 1:
            return jsonify({"Response": "Prompt Updated Successfully"}), 200
        else:
            return jsonify({"Error": "Provided Index is out of range"}), 400

    except json.JSONDecodeError:
        return jsonify({"Error": "Invalid JSON syntax"}), 400
    except jsonschema.ValidationError as e:
        return f"{e}", 400
    except Exception:
        app_log.log.error(
            f"Exception occured in update_prompt():\n{traceback.format_exc()}")
        return jsonify({"Error": "Internal Server Error"}), 500


@app.route("/deleteprompt", methods=['POST'])
def delete_prompt():
    """Deletes prompt at the provided index of list
    Input Params:
        JSON - {"Index": int}
    Returns:
        JSON - {"Response": str}
    """
    try:
        data = json.loads(request.get_data(as_text=True))
        status = bot.delete_prompt(prompt_index=data['Index'])
        if status == 0:
            return jsonify({"Error": "Provided Index must be an integer"}), 400
        elif status == 1:
            print(bot.input_prompt_list)
            return jsonify({"Response": "Prompt Deleted Successfully"}), 200
        else:
            return jsonify({"Error": "Provided Index is out of range"}), 400

    except json.JSONDecodeError:
        return jsonify({"Error": "Invalid JSON syntax"}), 400
    except jsonschema.ValidationError as e:
        return f"{e}", 400
    except Exception:
        app_log.log.error(
            f"Exception occured in delete_prompt():\n{traceback.format_exc()}")
        return jsonify({"Error": "Internal Server Error"}), 500
