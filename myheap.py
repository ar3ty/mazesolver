class MyMinHeap:
    def __init__(self):
        self.__elements = []

    def is_empty(self):
        return len(self.__elements) == 0

    def push(self, priority, i, j, cost):
        item = (i, j, cost)
        self.__elements.append((priority, item))
        self.__bubble_up(len(self.__elements)-1)

    def __bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.__elements[parent_index][0] > self.__elements[index][0]:
            self.__elements[parent_index], self.__elements[index] = self.__elements[index], self.__elements[parent_index]
            self.__bubble_up(parent_index)

    def pop(self):
        if self.is_empty():
            return None
        if len(self.__elements) == 1:
            return self.__elements.pop()[1]
        root = self.__elements[0]
        self.__elements[0] = self.__elements.pop()
        self.__bubble_down(0)
        return root[1]
    
    def __bubble_down(self, index):
        left_child_idx = 2 * index + 1
        right_child_idx = 2 * index + 2
        min_child_idx = index
        if left_child_idx < len(self.__elements) and self.__elements[index][0] > self.__elements[left_child_idx][0]:
            min_child_idx = left_child_idx
        if right_child_idx < len(self.__elements) and self.__elements[index][0] > self.__elements[right_child_idx][0]:
            min_child_idx = right_child_idx
        if min_child_idx != index:
            self.__elements[index], self.__elements[min_child_idx] = self.__elements[min_child_idx], self.__elements[index]
            self.__bubble_down(min_child_idx)