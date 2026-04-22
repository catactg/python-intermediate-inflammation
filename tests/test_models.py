"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest
from inflammation.models import daily_mean, daily_min

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
            ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
            (np.zeros((3, 5)), np.zeros(5)),
            ([[1, 2, 3]], [1, 2, 3]),
        ])

def test_daily_mean(test_input, test_result):
    """Test that mean function works for an array of zeros and positive integers."""
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

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
            ([ [1, 2, -1],[3, -2, 4],[5, -9, 6]], [1,-9,-1]),
        ])
def test_daily_min(test_input, test_result):
    """Test that min function works for an array of positive and negative integers."""
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_min_string():
    """Test that the min function fails for an array of strings
    """
    with pytest.raises(TypeError):
        error_expected = daily_min(['hi','there'])
