from mycroft import MycroftSkill, intent_handler
from mycroft.util import LOG
from adapt.intent import IntentBuilder

class MyHomey(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('').require('action_on').require('device'))
    def handle_device_on(self, message):
        action = message.data.get("action_on")
        device = message.data.get("device")
        self.log.info(F"Action = {action} , Device = {device}")

    # @intent_handler(IntentBuilder('').require('action_off').require('device'))
    # def handle_device_off(self, message):
    #     action = message.data.get("action_off")
    #     device = message.data.get("device")
    #     self.log.info(F"Action = {action} , Device = {device}")

def create_skill():
    return MyHomey()
