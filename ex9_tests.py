import unittest
import ex9_code


class TestIsEmpty(unittest.TestCase):

    def test_is_empty_true(self):
        heap = ex9_code.Heap()
        self.assertTrue(heap.is_empty())

    def test_is_empty_false(self):
        heap = ex9_code.Heap([4])
        self.assertFalse(heap.is_empty())


class TestInit(unittest.TestCase):

    def test_init_blank(self):
        heap = ex9_code.Heap()
        self.assertEqual(heap._heap, [])

    def test_init_one_element(self):
        heap = ex9_code.Heap([5])
        self.assertEqual(heap._heap, [5])

    def test_init_preset(self):
        heap = ex9_code.Heap([1, 2, 3, 4, 5])
        self.assertEqual(heap._heap, [5, 4, 2, 1, 3])

    def test_init_no_fixing(self):
        heap = ex9_code.Heap([5, 4, 2, 1, 3])
        self.assertEqual(heap._heap, [5, 4, 2, 1, 3])


class TestBubbleUp(unittest.TestCase):

    def test_bubble_up_doing_nothing(self):
        heap = ex9_code.Heap([3, 2])
        heap._bubble_up(1)
        self.assertEqual(heap._heap, [3, 2])

    def test_bubble_up(self):
        heap = ex9_code.Heap()
        heap._heap = [2, 3]
        heap._bubble_up(1)
        self.assertEqual(heap._heap, [3, 2])

    def test_double_bubble_up(self):
        heap = ex9_code.Heap()
        heap._heap = [3, 1, 2, 4]
        heap._bubble_up(3)
        self.assertEqual(heap._heap, [4, 3, 2, 1])

    def test_bubble_up_deep_left_node(self):
        heap = ex9_code.Heap()
        heap._heap = [10, 9, 8, 7, 6, 5, 4, 11]
        heap._bubble_up(7)
        self.assertEqual(heap._heap, [11, 10, 8, 9, 6, 5, 4, 7])

    def test_bubble_up_deep_right_node(self):
        heap = ex9_code.Heap()
        heap._heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, 11]
        heap._bubble_up(14)
        self.assertEqual(
            heap._heap, [11, 9, 10, 7, 6, 5, 8, 3, 2, 1, 0, -1, -2, -3, 4])


class TestViolates(unittest.TestCase):

    def test_violates_true(self):
        heap = ex9_code.Heap()
        heap._heap = [2, 3]
        self.assertTrue(heap._violates(0))

    def test_violates_false(self):
        heap = ex9_code.Heap([6, 43, 7, 2, 5, 7])
        self.assertFalse(heap._violates(2))

    def test_one_element_violates(self):
        heap = ex9_code.Heap([5])
        self.assertFalse(heap._violates(0))


class TestRemoveTop(unittest.TestCase):

    def test_remove_top(self):
        heap = ex9_code.Heap([4, 3, 2, 1])
        heap.remove_top()
        self.assertEqual(heap._heap, [3, 1, 2])

    def test_remove_top_big_tree(self):
        heap = ex9_code.Heap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        heap.remove_top()
        self.assertEqual(heap._heap, [9, 7, 8, 3, 6, 5, 4, 1, 2])

    def test_remove_top_one_element(self):
        heap = ex9_code.Heap([5])
        heap.remove_top()
        self.assertEqual(heap._heap, [])

    def test_remove_top_empty(self):
        heap = ex9_code.Heap()
        with self.assertRaises(ex9_code.HeapEmptyError):
            heap.remove_top()

    def test_remove_top_with_left_bubble(self):
        heap = ex9_code.Heap([3, 2, 1])
        heap.remove_top()
        self.assertEqual(heap._heap, [2, 1])

    def test_remove_top_with_right_bubble(self):
        heap = ex9_code.Heap([4, 1, 2])
        heap.remove_top()
        self.assertEqual(heap._heap, [2, 1])
        
    def test_remove_top_return(self):
        heap = ex9_code.Heap([8,7,6,5,4,3])
        self.assertEqual(8,heap.remove_top())


class TestInsert(unittest.TestCase):

    def test_insert_blank(self):
        heap = ex9_code.Heap()
        heap.insert(5)
        self.assertEqual(heap._heap, [5])

    def test_insert_larger(self):
        heap = ex9_code.Heap([4, 3, 2, 1, 0])
        heap.insert(5)
        self.assertEqual(heap._heap, [5, 3, 4, 1, 0, 2])

    def test_insert_smaller(self):
        heap = ex9_code.Heap([4])
        heap.insert(3)
        self.assertEqual(heap._heap, [4, 3])

    def test_insert_deep_list_max_value(self):
        heap = ex9_code.Heap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        heap.insert(11)
        self.assertEqual(heap._heap, [11, 10, 8, 7, 9, 5, 4, 3, 2, 1, 6])


class TestSwap(unittest.TestCase):

    def test_swap_other_way(self):
        heap = ex9_code.Heap()
        heap._heap = [3, 2]
        heap._swap(1, 0)
        self.assertEqual(heap._heap, [2, 3])

    def test_swap_big_heap(self):
        heap = ex9_code.Heap([10, 9, 8, 7, 6, 5, 4, 3, 1])
        heap._swap(0, 8)
        self.assertEqual(heap._heap, [1, 9, 8, 7, 6, 5, 4, 3, 10])

    def test_swap_small_heap(self):
        heap = ex9_code.Heap()
        heap._heap = [3, 2]
        heap._swap(0, 1)
        self.assertEqual(heap._heap, [2, 3])


class TestBubbleDown(unittest.TestCase):

    def test_small_bubble_down(self):
        heap = ex9_code.Heap()
        heap._heap = [1, 3]
        heap._bubble_down(0)
        self.assertEqual(heap._heap, [3, 1])

    def test_bubble_down_large_left(self):
        heap = ex9_code.Heap()
        heap._heap = [1, 9, 8, 7, 6, 5, 4, 3]
        heap._bubble_down(0)
        self.assertEqual(heap._heap, [9, 7, 8, 3, 6, 5, 4, 1])

    def test_bubble_down_large_right(self):
        heap = ex9_code.Heap()
        heap._heap = [0, 9, 8, 7, 6, 4, 2, 1, 3]
        heap._bubble_down(0)
        self.assertEqual(heap._heap, [9, 7, 8, 3, 6, 4, 2, 1, 0])

if __name__ == "__main__":
    unittest.main(exit=False)
