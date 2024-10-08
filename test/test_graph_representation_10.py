import subprocess
import re
import pytest


@pytest.fixture
def sample_tree():
    from student_code import SortingTree
    tree = SortingTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.insert(value)
    return tree

def test_traverse_empty(capsys):
    from student_code import SortingTree
    tree = SortingTree()
    tree.traverse()
    captured = capsys.readouterr()
    assert captured.out 