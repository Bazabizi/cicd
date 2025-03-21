from cicd import hello

def test():
    assert hello("Nahom") == "Hello Nahom"
    assert hello("Nahom") != "Hello"