from hello import hello_you


def test_hello_you():
    assert "Your Silly: Jim" == hello_you("Jim")
