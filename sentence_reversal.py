# Given a string of words, reverse all the words.
# remove all leading and trailing whitespace


def rev_word(s):
    word_list = s.split()
    word_list.reverse()
    return " ".join(word_list)


def rev_word2(s):
    words = []
    length = len(s)
    spaces = [" "]

    i = 0

    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1

    return " ".join(reversed(words))


from nose.tools import assert_equal


class ReversalTest(object):
    def test(self, sol):
        assert_equal(sol("    space before"), "before space")
        assert_equal(sol("space after     "), "after space")
        assert_equal(sol("   Hello John    how are you   "), "you are how John Hello")
        assert_equal(sol("1"), "1")
        print("ALL TEST CASES PASSED - Sentence Reversal")


# Run and test
t = ReversalTest()
t.test(rev_word)
