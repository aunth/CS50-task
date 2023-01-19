from my_file import main    

def test_1():
    assert main('43.34.21.2')==True

def test_2():
    assert main('433.34.21.2')==False

def test_3():
    assert main('43.0.0.21.2')==False

def test_4():
    assert main('43.34.21.22')==True

def test_5():
    assert main('0.0.0.0')==True
