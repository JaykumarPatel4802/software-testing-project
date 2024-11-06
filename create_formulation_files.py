# cd problem_formulation
# python ..\create_formulation_files.py


problems = [
    "Two Sum", "Valid Anagram", "Product of Array Except Self", "Top K Frequent Elements", "Longest Consecutive Suquence", "Valid Palindrome", "Best Time to Buy and Sell Stock", "Container with Most Water", "Two Sum II INput Array Is Sorted", "3Sum", "Trapping Rain Water", "Invert Binary Tree", "Diameter of Binary Tree", "Binary Tree Right Side View", "Lowest Common Ancestor of a Binary Search Tree", "Binary tree Maximum Path Sum", "Serialize and Deserialize Binary Tree", "Number of Islands", "Course Schedule", "Rotting Oranges", "Word Search", "Combination Sum", "Word Ladder", "N Queens", "Climbing Stairs", "Min Cost Climbing Stairs", "House Robber", "Coin Change", "Palindromic Substrings", "Maximum Product Subarray"
] 

for idx, problem in enumerate(problems):
    filename = f"{idx + 1} - {problem}"
    with open(filename, "w") as file:
        pass  # This creates an empty file