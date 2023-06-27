import json


class BuiltEnvironment:
    environment = {
        'name': 'house',
        'room': [
            {
                'name': 'living room',
                'furniture': ['sofa', 'chair', 'cabinet', 'coffee table'],
                'appliance': ['tv', 'speaker', 'lamp', 'fan', 'air conditioner'],
                'others': [],
            },
            {
                'name': 'bedroom',
                'furniture': ['bed', 'chair', 'cabinet', 'desk'],
                'appliance': ['tv', 'speaker', 'lamp', 'fan', 'air conditioner'],
                'others': [],
            },
        ],
    }
    name = 'house'

    def __init__(self, env: dict = None):
        if env is not None:
            self.environment = env
            self.name = env['name']
        else:
            # read the json from default file
            json_file = open('inputs/house.json', 'r')
            house = json.load(json_file)
            json_file.close()

            self.environment = house
            self.name = self.environment['name']

    def describe(self):
        """
            Describe the environment to the agent, the output is a string
            :return:
            """
        environment_description = ''
        environment_description += 'This is a ' + self.environment['name'] + '. '
        for component in self.environment['room']:
            # if nothing in the room, then describe the component as empty
            if len(component['furniture']) == 0 and len(component['appliance']) == 0 and len(component['others']) == 0:
                environment_description += component['name'] + ' is empty. '
            else:
                environment_description += component['name'] + ' has '
                for furniture in component['furniture']:
                    environment_description += furniture + ', '
                for appliance in component['appliance']:
                    environment_description += appliance + ', '
                for other in component['others']:
                    environment_description += other + ', '
                environment_description += '. '
        return environment_description

    def describe_room(self, room_name: str):
        """
        Describe the room to the agent, the output is a string
        :param room_name:
        :return:
        """
        # if the room is not in the environment, then return an error message
        for component in self.environment['room']:
            if component['name'] == room_name:
                room_description = ''
                room_description += component['name'] + ' has '
                for furniture in component['furniture']:
                    room_description += furniture + ', '
                for appliance in component['appliance']:
                    room_description += appliance + ', '
                for other in component['others']:
                    room_description += other + ', '
                room_description += '. '
                return room_description
        else:
            return 'The room ' + room_name + ' is not in the environment.'


if __name__ == '__main__':
    house_env = BuiltEnvironment()
    print(house_env.describe())
    print(house_env.describe_room('living room'))
