"""Tests for the Patient model."""

from inflammation.models import Patient

def test_create_patient():

    name = 'Alice'
    w = 50
    h = 1.8
    p = Patient(name=name, weight=w, height=h)

    assert p.name == name
