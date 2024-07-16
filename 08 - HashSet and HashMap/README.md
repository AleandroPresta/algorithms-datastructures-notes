# HashSets ad HashMaps

## Table of Contents

-   [HashSet](#hashset)
    -   [Operations](#operations)
    -   [Complexities](#complexities)
-   [HashMap](#hashmap)
    -   [Operations](#operations-1)
    -   [Complexities](#complexities-1)
-   [Summary](#summary)

# Overview of HashSets and HashMaps

## HashSet

A `HashSet` is a collection that contains no duplicate elements and has no guaranteed order of iteration.

### Operations

1. **Add (`add(E e)`):** Adds the specified element to this set if it is not already present.
2. **Remove (`remove(Object o)`):** Removes the specified element from this set if it is present.
3. **Contains (`contains(Object o)`):** Returns `true` if this set contains the specified element.
4. **Size (`size()`):** Returns the number of elements in the set.
5. **Is Empty (`isEmpty()`):** Returns `true` if the set contains no elements.
6. **Clear (`clear()`):** Removes all elements from the set.
7. **Iterator (`iterator()`):** Returns an iterator over the elements in the set.

### Complexities

-   **Add:** $O(1)$ average, $O(n)$ worst-case (due to potential rehashing when the underlying array grows).
-   **Remove:** $O(1)$ average, $O(n)$ worst-case.
-   **Contains:** $O(1)$ average, $O(n)$ worst-case.
-   **Size:** $O(1)$.
-   **Is Empty:** $O(1)$.
-   **Clear:** $O(n)$, as it must iterate over the entire set to remove all elements.
-   **Iterator:** $O(h/n)$, where h is the table length and n is the number of elements in the set, assuming a good hash function and load factor.

## HashMap

A `HashMap` is a collection that maps keys to values, with no duplicate keys allowed. Each key can map to at most one value.

### Operations

1. **Put (`put(K key, V value)`):** Associates the specified value with the specified key in this map.
2. **Get (`get(Object key)`):** Returns the value to which the specified key is mapped, or `null` if this map contains no mapping for the key.
3. **Remove (`remove(Object key)`):** Removes the mapping for a key from this map if it is present.
4. **Contains Key (`containsKey(Object key)`):** Returns `true` if this map contains a mapping for the specified key.
5. **Contains Value (`containsValue(Object value)`):** Returns `true` if this map maps one or more keys to the specified value.
6. **Size (`size()`):** Returns the number of key-value mappings in the map.
7. **Is Empty (`isEmpty()`):** Returns `true` if the map contains no key-value mappings.
8. **Clear (`clear()`):** Removes all the mappings from the map.
9. **Key Set (`keySet()`):** Returns a `Set` view of the keys contained in this map.
10. **Values (`values()`):** Returns a `Collection` view of the values contained in this map.
11. **Entry Set (`entrySet()`):** Returns a `Set` view of the mappings contained in this map.

### Complexities

-   **Put:** $O(1)$ average, $O(n)$ worst-case (due to potential rehashing when the underlying array grows).
-   **Get:** $O(1)$ average, $O(n)$ worst-case.
-   **Remove:** $O(1)$ average, $O(n)$ worst-case.
-   **Contains Key:** $O(1)$ average, $O(n)$ worst-case.
-   **Contains Value:** $O(n)$, as it requires a traversal of the map.
-   **Size:** $O(1)$.
-   **Is Empty:** $O(1)$.
-   **Clear:** $O(n)$, as it must iterate over the entire map to remove all mappings.
-   **Key Set:** $O(h/n)$, where h is the table length and n is the number of keys in the map, assuming a good hash function and load factor.
-   **Values:** $O(h/n)$.
-   **Entry Set:** $O(h/n)$.

## Summary

Both `HashSet` and `HashMap` provide efficient average-time complexities for their fundamental operations, thanks to the use of hashing. However, their worst-case scenarios can degrade to O(n) due to hash collisions, which are typically mitigated with good hash functions and appropriate resizing policies.

### HashSet

-   **Advantages:**

    -   Fast average time complexity for basic operations (add, remove, contains).
    -   Ensures uniqueness of elements.
    -   Simple to use and does not allow duplicate elements.

-   **Disadvantages:**
    -   No guaranteed order of iteration.
    -   Worst-case time complexity can degrade to O(n).
    -   Requires a good hash function to maintain efficiency.

### HashMap

-   **Advantages:**

    -   Fast average time complexity for basic operations (put, get, remove).
    -   Allows for association between keys and values.
    -   Provides efficient lookups, inserts, and deletes.

-   **Disadvantages:**
    -   No guaranteed order of keys or values.
    -   Worst-case time complexity can degrade to O(n).
    -   Requires a good hash function to maintain efficiency.
    -   Can consume more memory compared to other data structures like linked lists or trees.
