import difflib
text_A = """
1) Only [text_A] has this line
3) Both has this line.
4) Similar version ! :D Works in middle or in the end. :D
"""

text_B = """
2) Can be found just in [text_B]
3) Both has this line.
4) Similar ! :P Works in middle or in the end as well. :P
"""

delta = difflib.Differ().compare(text_A.splitlines(), text_B.splitlines())
print('\n'.join(delta))

# Output:
#- 1) Only [text_A] has this line
#+ 2) Can be found just in [text_B]
#  3) Both has this line.
#- 4) Similar version ! :D Works in middle or in the end. :D
#?            --------   ^                                 ^
#
#+ 4) Similar ! :P Works in middle or in the end as well. :P
#?               ^                              ++++++++   ^


from difflib import HtmlDiff

delta_html = HtmlDiff().make_file(text_A.splitlines(), text_B.splitlines())
with open('diff.html', 'w') as f:
	f.write(delta_html)