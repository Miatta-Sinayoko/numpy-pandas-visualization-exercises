# Import NumPy
#import numpy as np


# Create a NumPy array
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a


#1.# How many negative numbers are there?


# Get the negative numbers
negative_numbers = a[a < 0]

print(a[a < 0])
len(a[a < 0])


#2.How many positive numbers are there?

# Count the number of positive numbers
print(a[a > 0])

# Print the number of positive numbers
print(a[a > 0].size)




#3.How many even positive numbers are there?
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
# Select the positive numbers
# Select the even positive numbers
print(a[(a > 0) & (a % 2 == 0)])
print(a[(a > 0) & (a % 2 == 0)].shape)


# 4.If you were to add 3 to each data point, how many positive numbers would there be?
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# Add 3 to each data point

# Select the positive numbers
add_three = a + 3
print(add_three[add_three > 0])
add_three[add_three > 0].size






# 5.If you squared each number, what would the new mean and standard deviation be?
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
# Square each number
# Calculate the new mean and standard deviation

squares = a**2

{
    "mean": squares.mean(),
    "standard_deviation": squares.std()
}

#Center the array
centered = a - a.mean()
centered




# 6.A common statistical operation on a dataset is centering.
# This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point.
# Center the data set. See this link for more on centering.

# Calculate the mean of the dataset
mean = np.mean(a)

# Center the dataset by subtracting the mean from each data point
centered_data = a - mean

print("Centered dataset:")
print(centered_data)



# 7.Calculate the z-score for each data point. Recall that the z-score is given by:
# Z=x−μ/σ

# Calculate the mean of the dataset
# Calculate the standard deviation of the dataset
# Calculate the z-score for each data point

zscores = (a - a.mean()) / a.std()
zscores



# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.
