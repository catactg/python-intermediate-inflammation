"""Tests for the Patient model."""

from inflammation.models import Patient, compute_bmi
import numpy.testing as npt
import pytest

def test_create_patient():
    name = 'Alice'
    w = 50
    h = 1.8
    p = Patient(name=name, weight=w, height=h) # with this we fix the test

    assert p.name == name
    assert p.weight == w        # good practice: test the new properties
    assert p.height == h        # good practice: test the new properties

def test_compute_bmi():
    maria = Patient(name='maria',  height=1.6, weight=60)
    expected_bmi = 23.4375
    npt.assert_almost_equal(maria.get_body_mass_index(), expected_bmi)

@pytest.mark.parametrize("name, weight, height, expected", [
    ("Alice",  80, 1.7,  True),   # BMI ≈ 27.7 → overweight
    ("Bob",    60, 1.8,  False),  # BMI ≈ 18.5 → not overweight
    ("Carol",  68, 1.65, False),   # BMI ≈ 25.0 → not overweight (boundary)
    ("David",  67, 1.65, False),  # BMI ≈ 24.6 → not overweight
])
def test_is_overweight(name, weight, height, expected):
    """Test that is_overweight returns the correct boolean for various BMI values."""
    patient = Patient(name=name, weight=weight, height=height)
    assert patient.is_overweight() == expected

def test_patient_negative_weight():
    """Test that creating a patient with non-positive weight raises ValueError."""
    with pytest.raises(ValueError):
        Patient(name="Invalid", weight=-5, height=1.7)


def test_patient_zero_height():
    """Test that creating a patient with zero height raises ValueError."""
    with pytest.raises(ValueError):
        Patient(name="Invalid", weight=70, height=0)


@pytest.mark.parametrize("weight, height, expected_bmi", [
    (70,  1.75, 22.857142857142858),
    (90,  1.80, 27.777777777777779),
    (50,  1.60, 19.531250),
])
def test_compute_bmi_pure(weight, height, expected_bmi):
    """Test that compute_bmi returns the correct value for various inputs."""
    npt.assert_almost_equal(compute_bmi(weight, height), expected_bmi)