from django import template

register = template.Library()

@register.filter
def starts_with(value, arg):
    """
    Checks if a string starts with a given prefix.
    Usage: {{ request.path|starts_with:'/services/' }}
    """
    if isinstance(value, str):
        return value.startswith(arg)
    return False