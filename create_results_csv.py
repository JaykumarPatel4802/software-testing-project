import pandas as pd

problems = [
    "Two Sum", "Valid Anagram", "Product of Array Except Self", "Top K Frequent Elements", "Longest Consecutive Suquence", "Valid Palindrome", "Best Time to Buy and Sell Stock", "Container with Most Water", "Two Sum II Input Array Is Sorted", "3Sum", "Trapping Rain Water", "Invert Binary Tree", "Diameter of Binary Tree", "Binary Tree Right Side View", "Lowest Common Ancestor of a Binary Search Tree", "Binary tree Maximum Path Sum", "Serialize and Deserialize Binary Tree", "Number of Islands", "Course Schedule", "Rotting Oranges", "Word Search", "Combination Sum", "Word Ladder", "N Queens", "Climbing Stairs", "Min Cost Climbing Stairs", "House Robber", "Coin Change", "Palindromic Substrings", "Maximum Product Subarray"
]

categories = [
    "Arrays and Hashing", "Arrays and Hashing", "Arrays and Hashing", "Arrays and Hashing", "Arrays and Hashing", "Two Pointer", "Two Pointer", "Two Pointer", "Two Pointer", "Two Pointer", "Two Pointer", "Trees", "Trees", "Trees", "Trees", "Trees", "Trees", "Graphs", "Graphs", "Graphs", "Graphs", "Graphs", "Graphs", "Graphs", "DP", "DP", "DP", "DP", "DP", "DP"
]

additional_details = [
    "NA", "NA", "NA", "NA", "NA", "NA", "Sliding Window", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "Backtracking", "Backtracking", "NA", "Backtracking", "NA", "NA", "NA", "NA", "NA", "NA"
]

difficulties = [
    "Easy", "Easy", "Medium", "Medium", "Medium", "Easy", "Easy", "Medium", "Medium", "Medium", "Hard", "Easy", "Easy", "Medium", "Medium", "Hard", "Hard", "Medium", "Medium", "Medium", "Medium", "Medium", "Hard", "Hard", "Easy", "Easy", "Medium", "Medium", "Medium", "Medium"
]


# Initialize DataFrame
data = {
    "ID": range(1, len(problems) + 1),
    "Problem": problems,
    "Category": categories,
    "Additional Details": additional_details,
    "Difficulty": difficulties,
    "ChatGPT (1)": [pd.NA] * len(problems),
    "Gemeni (2)": [pd.NA] * len(problems),
    "Claude (3)": [pd.NA] * len(problems),
    "Perplexity (4)": [pd.NA] * len(problems)
}

# Create the DataFrame
df = pd.DataFrame(data).astype({
    "ChatGPT (1)": "Int64",
    "Gemeni (2)": "Int64",
    "Claude (3)": "Int64",
    "Perplexity (4)": "Int64"
})

df.to_csv("results.csv", index=False)
