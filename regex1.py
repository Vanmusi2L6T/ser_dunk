import re

text2 = """
Name: Vansh Gupta
Email: vansh123@gmail.com
Skills: Python, SQL, Machine Learning, Deep Learning
LinkedIn: https://linkedin.com/in/vanshgupta
Education: BTech
"""

#  Extract Name
name = re.search(r'Name:\s*(.*)', text2)
print("Name:", name.group(1))


#  Extract Email
email = re.search(r'[\w\.-]+@[\w\.-]+', text2)
print("Email:", email.group())


#  Extract Skills 
skills = re.search(r'Skills:\s*(.*?)\n', text2)
skills_list = skills.group(1).split(', ')
print("Skills:", skills_list)


#  Extract LinkedIn URL
linkedin = re.search(r'https?://\S+', text2)
print("LinkedIn:", linkedin.group())


#  Extract Education
education = re.search(r'Education:\s*(.*)', text2)
print("Education:", education.group(1))