import openai

from activitySchedule import get_schedule
from actionPlan import create_actions_for_schedule
from agent import Agent
from builtEnvironment import BuiltEnvironment
from utils import save_json_to_file
from llm.base import init_openai_key


def main(key: str):
    # configure openai
    init_openai_key()

    # create agent, environment, and day setting
    agent = Agent()
    environment = BuiltEnvironment()
    day_setting = 'Saturday'

    # get schedule and save to file
    agent_schedule = get_schedule(agent, day_setting, environment)
    save_json_to_file(agent_schedule, 'results/agent_schedule.json')

    # get actions for each activity in the schedule
    # and save to file
    create_actions_for_schedule(agent, environment, agent_schedule)


if __name__ == '__main__':
    main()
