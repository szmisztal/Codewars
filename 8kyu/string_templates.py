"""Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template feature, Help Timmy with his string template so it works as he expects!"""


def build_string(*args):
    return f"I like {', '.join([i for i in args])}!"

