from mycroft import MycroftSkill, intent_file_handler


class MorningUpdate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('update.morning.intent')
    def handle_update_morning(self, message):
        self.speak_dialog('update.morning')


def create_skill():
    return MorningUpdate()

