"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest
import os
from inflammation.models import daily_mean, daily_max, daily_min
from inflammation.analysis import analyse_data, CSVDataSource


@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
        (np.zeros((3, 5)), np.zeros(5)),
        ([[1, 2, 3]], [1, 2, 3]),
    ],
)
def test_daily_mean(
    test_input, test_result
):  # add input arguments from the parametrize decorator
    """Test that daily_mean function works for an array of zeros and positive integers."""
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_string():
    """Test that daily_mean function fails for an array of strings"""
    with pytest.raises(TypeError):
        error_expected = daily_mean(["hi", "there"])


@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
        ([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]], [1, 5, -2]),
    ],
)
def test_daily_max(test_input, test_result):
    """Test that max function works for an array of positive and negative integers."""
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_max_string():
    """Test that daily_max raises TypeError when passing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_max(["hi", "there"])


def test_daily_max_empty_array():
    """Test that daily_max raises ValueError when given an empty array."""
    with pytest.raises(ValueError):
        daily_max([])


def test_daily_max_nan_propagation():
    """Test that daily_max propagates NaN values"""
    data = np.array([[1, np.nan], [3, 4]])
    result = daily_max(data)
    assert np.isnan(result[1])  # documents current behavior


@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[1, 2, -1], [3, -2, 4], [5, -9, 6]], [1, -9, -1]),
        ([[0, 1, 2], [0, 3, 4]], [0, 1, 2]),
        ([[3, 3, 3], [3, 3, 3], [3, 3, 3]], [3, 3, 3]),
    ],
)
def test_daily_min(test_input, test_result):
    """Test that min function works for multiple inputs"""
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_analyse_data():
    path = os.path.join(os.getcwd(), "data")
    data_source = CSVDataSource(path)
    result = analyse_data(data_source)
    expected_result = [
        0.0,
        0.22510286,
        0.18157299,
        0.1264423,
        0.9495481,
        0.27118211,
        0.25104719,
        0.22330897,
        0.89680503,
        0.21573875,
        1.24235548,
        0.63042094,
        1.57511696,
        2.18850242,
        0.3729574,
        0.69395538,
        2.52365162,
        0.3179312,
        1.22850657,
        1.63149639,
        2.45861227,
        1.55556052,
        2.8214853,
        0.92117578,
        0.76176979,
        2.18346188,
        0.55368435,
        1.78441632,
        0.26549221,
        1.43938417,
        0.78959769,
        0.64913879,
        1.16078544,
        0.42417995,
        0.36019114,
        0.80801707,
        0.50323031,
        0.47574665,
        0.45197398,
        0.22070227,
    ]
    npt.assert_array_almost_equal(result, expected_result)


######## OPTIONAL CHALLENGE #######
def test_daily_min_integers():
    """Test that the min function works for an array of positive and negative integers."""

    test_input = np.array([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]])
    test_result = np.array([-3, 2, -9])

    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_mean_non_iterable():
    """Test that the mean function fails for a non iterable (single integer)"""
    with pytest.raises(IndexError):
        error_expected = daily_mean(9)
