def count_words(text):
    result = {}
    for word in text.lower().split():
        result[word] += 1
    return result


def test_simple():
    text = 'one'
    res = count_words(text)
    assert res['one'] == 1
    assert len(res) == 1


def test_count_words():
    # Given
    text = 'one two Two three THREE three'
    # When
    res = count_words(text)
    # Then
    assert res['one'] == 1
    assert res['two'] == 2
    assert res['three'] == 3


if __name__ == '__main__':
    test_count_words()
