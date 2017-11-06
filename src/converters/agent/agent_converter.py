import json
import urllib.parse
import pdb
import re
from furl import furl
from src.config import ana_config
from src.thrift_models.ttypes import MessageType, InputType, MediaType, ButtonType
from src.models.message import MessageContent, MessageData, Message, Media
from src.models.inputs import Option, Item, TextInput

class Converter():

    def __init__(self, state, *args, **kwargs):
        self.state = state

    def get_messages_data(self,message_data):

        messages_data = []
        messages_data.append(message_data)

        # construct input element
        message_type = MessageType._NAMES_TO_VALUES["INPUT"]
        input_type = InputType._NAMES_TO_VALUES["TEXT"] 
        input_attr = TextInput(placeHolder="Talk to our Agent").trim()

        content = MessageContent(
                inputType=input_type,
                textInputAttr=input_attr,
                mandatory=1,
                ).trim()
        input_message_data = MessageData(
                type=message_type,
                content=content
                ).trim()
        messages_data.append(input_message_data)
        return messages_data
