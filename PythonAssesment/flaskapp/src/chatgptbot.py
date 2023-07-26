import openai


class ChatGPTBotAPI:
    """
        This class performs CRUD operations on user prompts for ChatGPT\n
        Key Features:
        - Create Prompt: Stores user provided prompts in a list
        - Get Response: Returns responses from OpenAI API based on prompts added by the user
        - Update Prompt: Updates the prompt at the provided index of list
        - Delete Prompt: Deletes the prompt at the provided index of list
    """

    def __init__(self, openai_api_key) -> None:
        openai.api_key = openai_api_key
        self.chat_completion = None
        self.input_prompt_list = list()

    def create_prompt(self, prompt: str):
        if not isinstance(prompt, str):
            return False
        self.input_prompt_list.append(prompt)
        return True

    def get_response(self, prompt_index: int):
        if not isinstance(prompt_index, int):
            return False
        self.chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": self.input_prompt_list[0]}])
        print(self.chat_completion.choices[0].message.content)

    def update_prompt(self, prompt_index: int, new_prompt: str):
        if not (isinstance(prompt_index, int) and isinstance(new_prompt, str)):
            return 0
        if prompt_index >= 0 and prompt_index < len(self.input_prompt_list):
            self.input_prompt_list[prompt_index] = new_prompt
            return 1
        else:
            return 2

    def delete_prompt(self, prompt_index: int):
        if not isinstance(prompt_index, int):
            return 0
        if prompt_index >= 0 and prompt_index < len(self.input_prompt_list):
            del self.input_prompt_list[prompt_index]
            return 1
        else:
            return 2
