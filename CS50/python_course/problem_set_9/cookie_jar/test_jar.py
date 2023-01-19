from jar import Jar

def test_str():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪'
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar(100)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6
    jar.deposit(34)
    assert jar.size == 40

def test_withdraw():
    jar = Jar(100)
    jar.deposit(100)
    jar.withdraw(10)
    assert jar.size == 90
    jar.withdraw(20)
    assert jar.size == 70
    jar.withdraw(50)
    assert jar.size == 20
    jar.withdraw(20)
    assert jar.size == 0

def main():
    test_str()
    test_deposit()
    test_withdraw()

if __name__ == "__main__":
    main()


