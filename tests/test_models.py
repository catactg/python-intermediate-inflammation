"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest
from inflammation.models import daily_mean, daily_max, daily_min

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
            ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
            (np.zeros((3, 5)), np.zeros(5)),
            ([[1, 2, 3]], [1, 2, 3]),
        ])
def test_daily_mean(test_input, test_result): # add input arguments from the parametrize decorator
    """Test that mean function works for an array of zeros and positive integers."""
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean_string():
    """Test that the mean function fails for an array of strings
    """
    with pytest.raises(TypeError):
        error_expected = daily_mean(['hi','there'])

def test_daily_max_integers():
    """Test that the max function works for an array of positive integers.
    """

    test_input = np.array([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]])
    test_result = np.array([1, 5, -2])              

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_string():
    """Test for TypeError when passing strings""" 

    with pytest.raises(TypeError):
        error_expected = daily_max(['hi', 'there'])   

######## OPTIONAL CHALLENGE #######
def test_daily_min_integers():
    """Test that the min function works for an array of positive integers.
    """

    test_input = np.array([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]])
    test_result = np.array([-3, 2, -9])              

    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_mean_non_iterable():
    """Test that the mean function fails for a non iterable (single integer)
    """
    with pytest.raises(IndexError):
        error_expected = daily_mean(9)