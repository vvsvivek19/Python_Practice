"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return list((number,number+1,number+2))

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    all_rounds = rounds_1 + rounds_2
    return all_rounds


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    total = sum(hand)
    length = len(hand)
    average = total/length
    return average

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    actual_avg = card_average(hand)
    avg_first_last = (hand[0] + hand[-1])/2
    avg_median = hand[len(hand) // 2]
    if avg_first_last == actual_avg or avg_median == actual_avg:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_list = hand[1::2]
    odd_avg = sum(odd_list)/len(odd_list)
    even_list = hand[::2]
    even_avg = sum(even_list)/len(even_list)
    if odd_avg == even_avg:
        return True
    else:
        return False
    
def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    else:
        return hand
print(maybe_double_last([5, 9, 10]))