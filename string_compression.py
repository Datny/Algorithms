# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'


def compress(s):
    word_dict = dict()
    for letter in s:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    return "".join("".join((str(k), str(v))) for k, v in word_dict.items())

compress('AAAAABBBBCCCC')


from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED- string compression')

# Run Tests
t = TestCompress()
t.test(compress)