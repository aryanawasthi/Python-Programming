import re

# Using the compile and match for finding the regex expresisions
regex_expr=re.compile(r"fo+")
#print(regex_expr.match("for your life "))


# Using the only match expressions

#print(re.match(r'<HTML>',"<HTML>")) #<re.Match object; span=(0, 6), match='<HTML>'>`

# Searching : When we have to seach for patttern in the string

# Note Python offers two operation one is match and other other is search

# Let us try to find the differences between match and search

match_Regex=re.compile("Hello")
results=match_Regex.match(" Hello")
#print(results)          #None
# Here since we have given a blank and match checks from the beginning therefore it return None


# Using the pos parameter to specify where we have to start looking.
results=match_Regex.match(" Hello",1)
#print(results)          # <re.Match object; span=(1, 6), match='Hello'>

# Using the Post String
results=re.compile(r"^<HTML>")
#print(results.match(" <HTML>",1))    #None which means it is checking for the string in the beginning of the string.

# Using the Slice Operators

regex_expr=re.compile(r"^<HTML>")
res=regex_expr.match("  <HTML>"[2:])
#print(res)          #<re.Match object; span=(0, 6), match='<HTML>'> 
# Here Slicing creates a new string and then try to compare the new string.

# Using the Multiline Tag, will seatch for the regex after every new line tag.
res=regex_expr.match(" <HTML>",re.MULTILINE)
#print(res)  # None
res=regex_expr.match("  <HTML",re.MULTILINE)
#print(res)          # None
regex_expr=re.compile(r"^<HTML>")
res=regex_expr.search('  \n<HTML>',re.MULTILINE)
print(res)

# FINDALL: Using the findall function to find all the matches
reg_exp=re.compile(r"\w+")
results=reg_exp.findall("Hello World")
# print(results)   # ['Hello', 'World']

# Using the findall to seperate groups 
expr=re.compile(r"(\w+) (\w+)")
#print(expr.findall("Hello World Hello Hula find You"))

# Finditer works very similary with the findall but it return an iterator

res=expr.finditer("""Hello How are you What you are 
doing to help you find later""",re.MULTILINE)
#print(results.groups)
# 

new_res=expr.finditer("Hello How are yiou")
for i in new_res:
    print(i.group())






