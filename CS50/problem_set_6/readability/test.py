from readability import main


def test1():
    text = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"'
    return print(True if main(text) == "Grade 8" else False)

def test2():
    text = "When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh."
    return print(True if main(text) == "Grade 8" else False)

def test3():
    text = "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy."
    return print(True if main(text) == "Grade 9" else False)

def test4():
    text = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."
    return print(True if main(text) == "Grade 10" else False)

def test5():
    text = "A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains."
    return print(True if main(text) == "Grade 16+" else False)

def test6():
    text = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."
    return print(True if main(text) == "Grade 5" else False)

def test7():
    text = "In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."
    return print(True if main(text) == "Grade 7" else False)


test1()
test2()
test3()
test4()
test5()
test6()
test7()