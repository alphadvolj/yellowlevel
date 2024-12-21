def product_except_self(nums):
    n = len(nums)
    output = [1] * n

    prefix_product = 1
    for i in range(n):
        output[i] = prefix_product
        prefix_product *= nums[i]

    suffix_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= nums[i]

    return output

nums1 = [1, 2, 3, 4]
print(product_except_self(nums1))

nums2 = [-1, 1, 0, -3, 3]
print(product_except_self(nums2))