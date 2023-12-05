FUN_MESSAGES = [
    ("Ready to test your knowledge?", "🎥"),
    ("PWC QuizMaker welcomes you!", "🚀"),
    ("Think you caught all the details? Let's find out!", "🔍"),
    ("It's quiz time! No spoilers allowed.", "⏳"),
    ("Popped in for a quiz? You're in the right place!", "🍿"),
    ("Your next challenge awaits!", "🏆"),
    ("Another Topic, another quiz!", "🔄"),
    ("Did you pay attention? It's quiz o'clock!", "⏰"),
    ("Unleash your Knowledge prowess here!", "🦸"),
    ("Knowledge check: Engage!", "🚦"),
    ("Transform your watch time into quiz time!", "🔄"),
    ("Here to validate your knowledge expertise?", "🔍")
]

def get_random_toast():
    """Returns a random fun message and icon."""
    import random
    return random.choice(FUN_MESSAGES)