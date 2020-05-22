import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage_dictionary = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dictionary.keys():
            current_node = self.dll.head
            while current_node:
                if key in current_node.value.keys():
                    self.dll.move_to_front(current_node)
                current_node = current_node.next
            return self.storage_dictionary[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage_dictionary.keys():
            current_node = self.dll.head
            while current_node:
                if key in current_node.value.keys():
                    current_node.value[key] = value
                    self.dll.move_to_front(current_node)
                current_node = current_node.next
            self.storage_dictionary.update({key: value})
        elif self.size > self.limit - 1:
            removed_key = list(self.dll.remove_from_tail().keys())[0]
            self.storage_dictionary.pop(removed_key)
            self.dll.add_to_head({key: value})
            self.storage_dictionary.update({key: value})
        else:
            self.dll.add_to_head({key: value})
            self.storage_dictionary.update({key: value})
            self.size +=1
            print(f'SIZE: {self.size}, LIMIT: {self.limit}')
