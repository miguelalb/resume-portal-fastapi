import base64

from jinja2 import BaseLoader, Environment


def render_template(template_content: str, data: dict) -> str:
    content = base64.b64decode(template_content).decode("ascii")
    rtemplate = Environment(loader=BaseLoader).from_string(content)
    data = rtemplate.render(**data)
    i = data.encode("ascii")
    return base64.b64encode(i).decode("ascii")



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
