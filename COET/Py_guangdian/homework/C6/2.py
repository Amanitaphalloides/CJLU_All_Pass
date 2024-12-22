def has_duplicates(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return True
        seen.add(element)
    return False

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [1, 2, 3, 4, 5, 3]
test_list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
test_list4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a']

print("测试 1:", test_list1, "是否有重复?", has_duplicates(test_list1))
print("测试 2:", test_list2, "是否有重复?", has_duplicates(test_list2))
print("测试 3:", test_list3, "是否有重复?", has_duplicates(test_list3))
print("测试 4:", test_list4, "是否有重复?", has_duplicates(test_list4))
