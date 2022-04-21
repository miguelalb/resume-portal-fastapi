import base64
from datetime import datetime

from jinja2 import BaseLoader, Environment


def fill_html_template(template_content: str, profile_data: dict) -> str:
    """
    Fills an HTML template with profile data and base64 encode it.
    Params:
    - template_content: str -> Base64 encoded HTML template.
    - data: dict -> User profile data to fill the template with.
    """
    content = base64.b64decode(template_content).decode("utf-8")
    rtemplate = Environment(loader=BaseLoader).from_string(content)
    filled_template = rtemplate.render(**profile_data)
    i = filled_template.encode("utf-8")
    return base64.b64encode(i).decode("utf-8")


def get_object_name_from_schema(obj: object) -> str:
    """
    Returns the name of an object based on type.
    This is used to return a userfriendly exception
    to the client on bulk update operations.
    """
    obj_name = type(obj).__name__
    to_remove = ["Base", "Create", "Update"]
    for item in to_remove:
        if item in obj_name:
            obj_name = obj_name.replace(item, "")
    return obj_name


def prettify_timestamp(value: str) -> str:
    """
    Returns a pretty version of a timestamp object.
    Current format:
    - %b short name of month like Mar, Jun
    - %d day of the month from 1 to 31
    - %Y year in 4 digit format
    """
    return datetime.utcfromtimestamp(float(value)).strftime("%b %d %Y")
