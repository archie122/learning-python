def dna_to_rna(dna):
    return dna.replace('T', 'U')


def sum_array(a):
    return sum(a)


def gimme(input_array):
    x = sorted(input_array)
    middle = x[len(x) // 2]
    return input_array.index(middle)


# print(gimme([1, 5, 7, 4, 2]))

def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[m + i] = nums2[i]
    nums1.sort()


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
