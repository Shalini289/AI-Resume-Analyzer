import os
import json
import re

from datetime import datetime


def clean_json_response(response_text):

    response_text = re.sub(
        r"```json|```",
        "",
        response_text
    ).strip()

    try:
        return json.loads(response_text)

    except Exception:

        return {
            "error":
            "Unable to parse response"
        }


def generate_timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


def create_directory(path):

    if not os.path.exists(path):
        os.makedirs(path)


def save_text_file(
    content,
    filename
):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    return filename


def load_text_file(filename):

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def calculate_match_percentage(
    matched,
    total
):

    if total == 0:
        return 0

    return round(
        (matched / total) * 100,
        2
    )


def safe_get(
    dictionary,
    key,
    default=None
):

    return dictionary.get(
        key,
        default
    )