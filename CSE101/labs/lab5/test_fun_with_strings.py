from fun_with_strings import hullabaloo, is_palindrome


def testing():

    # Testing hullabaloo()
    input_word1 = 'plane'
    shuffled_word1 = hullabaloo(input_word1)
    print(shuffled_word1)

    input_word2 = 'bonbon'
    shuffled_word2 = hullabaloo(input_word2)
    print(shuffled_word2)

    # add more test cases as needed

    # Testing is_palindrome()
    input_str1 = 'racecar'
    print(is_palindrome(input_str1)) # should print True

    input_str2 = 'Hello, World!'
    print(is_palindrome(input_str2)) # should print False

    # add more test cases as needed

testing()