from mycroft import MycroftSkill, intent_handler
from mycroft.util import LOG
from adapt.intent import IntentBuilder

class MyHomey(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    # Turn tv on
    @intent_handler(IntentBuilder('').require('tv_action_on').require('tv_device'))
    def handle_device_on(self, message):
        action = message.data.get("tv_action_on")
        device = message.data.get("tv_device")
        self.log.info(F"Action = {action} , Device = {device}")

    # Watch channel
    @intent_handler(IntentBuilder('').require('tv_action_channel').require('tv_channel').optionally('tv_device'))
    def handle_device_on(self, message):
        action = message.data.get("tv_action_channel")
        channel = message.data.get("tv_channel")
        self.log.info(F"Action = {action} , Channel = {channel}")

def create_skill():
    return MyHomey()
