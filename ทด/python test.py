def rotate90(image):
    # Transpose the matrix and reverse each row
    return [''.join(row) for row in zip(*image[::-1])]

def rotate180(image):
    # Reverse the order of rows and each row itself
    return [row[::-1] for row in image[::-1]]

# Read input
h = int(input())  # the number of rows in the image
image = [input() for _ in range(h)]  # read each row of the image
operation = input()  # rotation type (rot90 or rot180)

# Perform the required rotation
if operation == 'rot90':
    rotated_image = rotate90(image)
elif operation == 'rot180':
    rotated_image = rotate180(image)
else:
    print("Invalid operation")
    exit()

# Output the result
for row in rotated_image:
    print(row)


