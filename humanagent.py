class HumanAgent():

    def __init__(self, allowed_actions=[]):
        self.allowed_actions = allowed_actions

    def pickAction(self, reward, observation):
        print(self.allowed_actions)
        input_action = raw_input()
        action = int(input_action) if input_action != '' else None
        return action

