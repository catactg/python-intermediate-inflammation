"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest
from inflammation.models import daily_mean, daily_min

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean_string():
    """Test that the mean function fails for an array of strings
    """
    with pytest.raises(TypeError):
        error_expected = daily_mean(['hi','there'])

def test_daily_mean_non_iterable():
    """Test that the mean function fails for an array of strings
    """
    with pytest.raises(IndexError):
        error_expected = daily_mean(9)

def test_daily_min_integers():
    """Test that the min function works for an array of positive and negative intergers.
    """

    test_input = np.array([[1, 2, -1],
                           [3, -2, 4],
                           [5, -9, 6]])
    test_result = np.array([1, -9, -1])
    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_string():
    """Test that the min function fails for an array of strings
    """
    with pytest.raises(TypeError):
        error_expected = daily_min(['hi','there'])
