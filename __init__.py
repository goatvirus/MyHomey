from mycroft import MycroftSkill, intent_handler
from mycroft.util import LOG
from adapt.intent import IntentBuilder

class MyHomey(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    # TV Action
    @intent_handler(IntentBuilder('').require('actions').optionally('devices'))
    def handle_device_on(self, message):
        device = message.data.get("device_tv")
        action = message.data.get("device_action")

        if device is None:
            device


        self.log.info(F"Device = {device} , Action = {action}")

def create_skill():
    return MyHomey()
