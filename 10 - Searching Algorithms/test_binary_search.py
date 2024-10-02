import pytest
from binary_search import BinarySearch

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class TestBinarySearch:
    def test_binary_search_found(self, sample_data):
        target = 5
        assert BinarySearch.binary_search(sample_data, target) == 4

    def test_binary_search_not_found(self, sample_data):
        target = 11
        assert BinarySearch.binary_search(sample_data, target) == -1

    def test_binary_search_empty_list(self):
        arr = []
        target = 1
        assert BinarySearch.binary_search(arr, target) == -1

    def test_binary_search_single_element_found(self):
        arr = [1]
        target = 1
        assert BinarySearch.binary_search(arr, target) == 0

    def test_binary_search_single_element_not_found(self):
        arr = [1]
        target = 2
        assert BinarySearch.binary_search(arr, target) == -1

if __name__ == "__main__":
    pytest.main()