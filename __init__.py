from mycroft import MycroftSkill, intent_handler
from mycroft.util import LOG
from adapt.intent import IntentBuilder

class MyHomey(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    # Turn tv on
    @intent_handler(IntentBuilder('').require('tv_action_on').require('tv_device').optionally('tv_filler'))
    def handle_device_on(self, message):
        action = message.data.get("action_on")
        device = message.data.get("device")
        self.log.info(F"Action = {action} , Device = {device}")

    # Turn tv on channel

def create_skill():
    return MyHomey()
