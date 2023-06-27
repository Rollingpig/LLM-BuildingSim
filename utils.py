from datetime import datetime


def calculate_duration_in_seconds(time_start: str, time_end: str) -> int:
    """
    Calculate the duration in seconds between two time strings.
    :param time_start:
    :param time_end:
    :return:
    """
    time_start = datetime.strptime(time_start, '%H:%M')
    time_end = datetime.strptime(time_end, '%H:%M')
    duration = time_end - time_start
    return duration.seconds


def save_json_to_file(json_obj, file_name):
    """
    Save the json schedule to a file.
    :param json_obj:
    :param file_name:
    :return:
    """
    import json
    with open(file_name, 'w') as json_file:
        # add indent=4 to make the json file more readable
        json.dump(json_obj, json_file, indent=4)


def parse_json_from_response_text(text: str) -> dict:
    # parse the response text to a json object
    # Let's do something manually:
    # sometimes GPT responds with something BEFORE the braces:
    # "I'm sorry, I don't understand. Please try again."
    # {"text": "I'm sorry, I don't understand. Please try again.",
    #  "confidence": 0.0}
    # So let's try to find the first brace and then parse the rest
    #  of the string
    try:
        brace_index = text.index("{")
        maybe_fixed_json = text[brace_index:]
        last_brace_index = maybe_fixed_json.rindex("}")
        maybe_fixed_json = maybe_fixed_json[: last_brace_index + 1]
        actions = eval(maybe_fixed_json)
        return actions
    except SyntaxError:
        assert False, "The response text is not a valid json object: " + text
