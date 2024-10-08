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

def test_insert_existing_value():
    from student_code import SortingTree
    tree = SortingTree(5)
    tree.insert(5)
    assert tree.get_node_value(tree.get_node_right("Root")) == 5
