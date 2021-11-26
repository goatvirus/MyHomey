from mycroft import MycroftSkill, intent_handler
from mycroft.util import LOG
from adapt.intent import IntentBuilder

class MyHomey(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    # TV Action
    @intent_handler(IntentBuilder('').require('device_action').require('device_tv'))
    def handle_device_on(self, message):
        device = message.data.get("device_tv")
        action = message.data.get("device_action")
        self.log.info(F"Device = {device} , Action = {action}")

    # TV Action with Channel
    @intent_handler(IntentBuilder('').require('device_action').require('tv_channel').optionally('device_tv'))
    def handle_device_on(self, message):
        device = message.data.get("device_tv")
        action = message.data.get("device_action")
        channel = message.data.get("tv_channel")
        if device is None:
            device = "tv"
        self.log.info(F"Device = {device} , Action = {action} , Channel = {channel}")

def create_skill():
    return MyHomey()
