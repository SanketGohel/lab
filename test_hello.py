from hello import hello_world


def test_hello_world():
    expected = "Hello World"
    result = hello_world()
    assert expected == result
