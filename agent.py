homer_simpson = {
    "name": "Abraham Simpson",
    "description": "He is cranky and old. He complains a lot. He is a veteran of World War II.",
    "needs": "food, beer, TV",
}


class Agent:
    name: str = 'Homer'

    # use sentences to describe the agent
    description: str = 'He is fat, lazy, stupid. He works in a nuclear power plant.'

    needs: str = 'food, beer, TV'

    current_room: str = 'bedroom'
    current_location: str = 'bed'
    current_time: str = '9:00'
    last_action: str = 'sleep'

    planned_activity: str = 'breakfast'
    planned_room: str = 'kitchen'
    activity_until: str = '9:30'

    def __init__(self, profile_dict: dict = None):
        if profile_dict is not None:
            self.name = profile_dict['name']
            self.description = profile_dict['description']
            self.needs = profile_dict['needs']
        else:
            self.name = homer_simpson['name']
            self.description = homer_simpson['description']
            self.needs = homer_simpson['needs']

    def describe_character(self):
        """
        Describe the agent to the environment, the output is a string
        :return:
        """
        agent_description = ''
        agent_description += f'The character is {self.name}. '
        agent_description += self.description
        agent_description += f'The need of this character is: {self.needs}. '
        return agent_description

    def describe_current_situation(self):
        """
        Describe the current situation of the agent, the output is a string
        :return:
        """
        description = ''
        description += f'Now the character is at the {self.current_location} of the {self.current_room}. '
        description += f'The character just did this: {self.last_action}. '
        description += f'Now the character is going to {self.planned_activity} at the {self.planned_room}. '
        description += f'The character will do this until from {self.current_time} to {self.activity_until}. '
        return description

    def update_current_info(self, action_plan: dict):
        """
        Update the agent status according to the action plan.
        :param action_plan:
        :return:
        """
        # do nothing if action plan is None
        if action_plan is None:
            return self

        # get the last action in the action plan
        last_action = action_plan["actions"][-1]

        # get the action, room, location, and use of the last action
        action = last_action["action"]
        room = last_action["room"]
        location = last_action["location"]

        # update the agent status
        self.last_action = action
        self.current_room = room
        self.current_location = location
        self.current_time = self.activity_until

        return self

    def update_planned_info(self, next_activity: dict):
        """
        Update the agent status according to the action plan.
        :param next_activity:
        :return:
        """
        # do nothing if next_activity is None
        if next_activity is None:
            return self

        # get the last action in the action plan
        planned_activity = next_activity["activity"]
        planned_room = next_activity["room"]
        activity_until = next_activity["end_time"]

        # update the agent status
        self.planned_activity = planned_activity
        self.planned_room = planned_room
        self.activity_until = activity_until

        return self
