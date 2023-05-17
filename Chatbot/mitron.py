import gradio as gr
import openai

openai.api_key = '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'

# Define a chatbot class that uses openai chat completion
class KissanChat:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.chat_history = [
            {
                "role": "system", 
                "content": "You are Kissan Mitra, a helpful farmer assistant. You help farmers deal with their agricultural problems and provide them with solutions. You are a friendly bot and you are here to help. You only talk about agriculture and farming and refuse to talk about anything else. You're catch phrase is 'Mitron! Abki baar, Kissan Mitra har Farm!'. You will use this catch phrase when greeting your user. You should be multilingual and talk to the user in their local language."
            }
        ]

    def respond(self, message):
        # Use openai chat completion to generate a bot message
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.chat_history + [{"role": "user", "content": message}]
        )
        # Get the content of the first choice
        bot_message = response["choices"][0]["message"]["content"]
        self.chat_history.append({"role": "user", "content": message})
        self.chat_history.append({"role": "assistant", "content": bot_message})
        return bot_message

    def clear(self):
        # Clear the chat history
        self.chat_history = [{"role": "system", "content": "You are Kissan Mitra, a helpful farmer assistant. You help farmers deal with their agricultural problems and provide them with solutions. You are a friendly bot and you are here to help. You only talk about agriculture and farming and refuse to talk about anything else."}]

# Create an instance of the chatbot class
kissan_chat = KissanChat()

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        # Use the kissan_chat instance to respond to the message
        bot_message = kissan_chat.respond(message)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: kissan_chat.clear(), None, chatbot, queue=False)

demo.launch(server_port=7000)
