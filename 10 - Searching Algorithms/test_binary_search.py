import pytest
from binary_search import BinarySearch

@pytest.fixture
def sample_data():
    return list(range(1, 101))  # Array from 1 to 100

class TestBinarySearch:
    def test_binary_search_found_start(self, sample_data):
        target = 1
        assert BinarySearch.binary_search(sample_data, target) == 0

    def test_binary_search_found_middle(self, sample_data):
        target = 50
        assert BinarySearch.binary_search(sample_data, target) == 49

    def test_binary_search_found_end(self, sample_data):
        target = 100
        assert BinarySearch.binary_search(sample_data, target) == 99

    def test_binary_search_not_found_below_range(self, sample_data):
        target = 65
        assert BinarySearch.binary_search(sample_data, target) == 64

    def test_binary_search_not_found_above_range(self, sample_data):
        target = 101
        assert BinarySearch.binary_search(sample_data, target) == -1

    def test_binary_search_not_found_middle(self, sample_data):
        target = 45
        assert BinarySearch.binary_search(sample_data, target) == 44

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

    def test_binary_search_duplicates(self):
        arr = [1, 2, 2, 2, 3, 4, 5]
        target = 2
        assert BinarySearch.binary_search(arr, target) in [1, 2, 3]

if __name__ == "__main__":
    pytest.main()