# 01 - Var - 2
#
# F-Strings and multi-line strings

"""This would be a multi-line
string, i can strech string acros lines
there is no real limit"""

# in case you dont want to use strings like that, you can use "\n"

"1st line\n2nd  line\n..."

# as you know; to merge strings you would usualy do
# str1 + str2

 "te" + "st" == "test" -> True

# but there is much easyer way to do it!
# using F-Strings
# to define one, you would usualy do this
f"this is a f-string"

# why use it?
# because it allows us to directly put variables into it

f"{4 + 8}" == "12"

# as you can see, inside of {} you can put variables and expr.