import re

print(" Example 1 ")

text1 = "I love ML and I love DL"

match1 = re.search(r'I.*love', text1)


print("Pattern: I.*love")
print("Output:", match1.group())


print(" Example 2 : Non-Greedy Match ")

match2 = re.search(r'I.*?love', text1)

print("Pattern: I.*?love")
print("Output:", match2.group())


print(" Example 3 : Resume Skills Extraction (Greedy) ")

text2 = """
Name: Vansh Gupta
Email: vansh123@gmail.com
Skills: Python, SQL, Machine Learning, Deep Learning
LinkedIn: https://linkedin.com/in/vanshgupta
Education: BTech
"""

skills_greedy = re.search(r'Skills:(.*)Education', text2)

print("Pattern: Skills:(.*)Education")
print("Output:", skills_greedy.group(1))


print(" Example 4 : Resume Skills Extraction (Non-Greedy) ")

skills_lazy= re.search(r'Skills:(.*?)Education',text2)

print("Pattern: Skills:(.*?)Education")
print("Output:", skills_lazy.group(1))


print("Example 5 : Clean Line Extraction Using Non-Greedy")

skills_line =re.search(r'Skills:\s*(.*?)\n', text2)

print("Pattern: Skills:\\s*(.*?)\\n")
print("Output:", skills_line.group(1))