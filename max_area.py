def maxArea(height):
    start, end = 0, len(height)-1
    max_area = 0
    while start < end:
        max_area = max(max_area, min(height[start], height[end]) * (end - start))
        if height[start] < height[end]:
            max_area = max(max_area, start*(end-start))
            start += 1
        else:
            end -= 1
    return max_area



if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))