from botbotme_plugins import base


def setup_function(function):
    # Monkey patch app and register plugin
    base.app = base.DummyApp(test_mode=True)
    import botbotme_plugins.plugins.bangmotivate


def test_motivate():
    responses = base.app.respond("!m BotBot")
    assert responses == ["You're doing good work, BotBot!"]


def test_nomotivate():
    responses = base.app.respond("shouldn't !m === false?")
    assert len(responses) == 0