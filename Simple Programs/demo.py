def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    original_word = word[:-4:]
    if original_word[-1] == 'i':
        original_word = original_word[:-2:]
        original_word = original_word + 'y'
        return original_word
    else:
        return original_word
print(remove_suffix_ness('sadness'))