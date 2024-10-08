import subprocess
import re
import pytest


@pytest.fixture
def sample_tree():
    from student_code import SortingTree
    tree = SortingTree(5)
    values = [3, 7, 2, 4, 6, 8]
    for value in values:
        tree.insert(value)
    return tree

def test_traverse(capsys, sample_tree):
    sample_tree.traverse()
    captured = capsys.readouterr()
    assert captured.out == "2 3 4 5 6 7 8 "
