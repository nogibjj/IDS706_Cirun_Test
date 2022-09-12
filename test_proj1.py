from proj1 import return_hello_world


def test_return_hello_world():
    """Test return_hello_world()"""
    assert return_hello_world() == "hello world"
