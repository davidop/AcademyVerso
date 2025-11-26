import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'examples'))

from process_fixed import process


def test_process_normal():
    assert process([2, 5]) == [5.0, 2.0]


def test_process_zero():
    assert process([0]) == [None]


def test_process_empty():
    assert process([]) == []
