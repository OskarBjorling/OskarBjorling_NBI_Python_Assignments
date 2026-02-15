#1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.

def c_to_f(degree):
    if degree < -273.15:
        return None
    return round(degree * 9 / 5 + 32 ,2)

def test_c_to_f():
    assert c_to_f(0) == 32
    assert c_to_f(-273.151) == None
    assert c_to_f(-273.15) == -459.67
    assert c_to_f(10) == 50

test_c_to_f()