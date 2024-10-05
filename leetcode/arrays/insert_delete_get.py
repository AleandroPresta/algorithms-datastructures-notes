from typing import Set
import random


class RandomizedSet:
    
    data: Set[int]

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        list_set = list(self.data)
        if len(list_set) == 1:
            return list_set[0]
        i_random = random.randint(0, len(list_set)-1)
        return list_set[i_random]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class Test:
    def test_basic(self):
        obj = RandomizedSet()
        assert obj.insert(1) == True
        assert obj.insert(2) == True
        assert obj.insert(1) == False
        assert obj.remove(1) == True
        assert obj.remove(1) == False
        assert obj.getRandom() in [2]

    def test_advanced(self):
        obj = RandomizedSet()
        obj.insert(1)
        obj.insert(10)
        obj.insert(20)
        obj.insert(30)
        assert obj.getRandom() in [1, 10, 20, 30]

    def test_edge_cases(self):
        obj = RandomizedSet()
        assert obj.insert(0) == True
        assert obj.insert(-1) == True
        assert obj.insert(1) == True
        assert obj.remove(0) == True
        assert obj.remove(-1) == True
        assert obj.remove(1) == True
        assert obj.insert(0) == True
        assert obj.getRandom() == 0

def main() -> None:
    tester = Test()
    
    tester.test_basic()
    print('Basic tests passed')
    
    tester.test_advanced()
    print('Advanced tests passed')
    
    tester.test_edge_cases()
    print('Edge case tests passed')
    

if __name__ == '__main__':
    main()