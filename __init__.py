from mycroft import MycroftSkill, intent_handler
from mycroft.util import LOG
from adapt.intent import IntentBuilder

class MyHomey(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("")
        .require("action")
        .require("device")
    def handle_action_device(self, message):
        action = message.data.get("action")
        device = message.data.get("device")
        self.log.info(F"Action = {action} , Device = {device}")

def create_skill():
    return MyHomey()


# {action} {item} {channel}


# Watch nbc {action:watch} {media:nbc}
# Turn to nbc
# Turn on nbc
# Turn nbc on
# Switch to nbc
# Change to nbc


# {Action}

# Watch NBC
# Watch Channel NBC
# Watch NBC Channel
# Turn On NBC
# Turn NBC On
# Turn on NBC Channel
# Turn

# Watch TV
# Turn On TV
# Turn TV On
