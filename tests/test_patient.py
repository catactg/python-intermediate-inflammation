"""Tests for the Patient model."""

from inflammation.models import Patient

def test_create_patient():
    name = 'Alice'
    w = 50
    h = 1.8
    p = Patient(name=name, weight=w, height=h) # with this we fix the test

    assert p.name == name
    assert p.weight == w        # good practice: test the new properties
    assert p.height == h        # good practice: test the new properties
