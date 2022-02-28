def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
      calculate_letters = {}

      for letter in phrase:
          calculate_letters[letter] = calculate_letters.get(letter , 0) + 1

                return calculate_letters
