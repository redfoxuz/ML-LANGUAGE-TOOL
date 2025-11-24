import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def fix_grammar(text):

    matches = tool.check(text)

    corrected = language_tool_python.utils.correct(text, matches)
    return corrected

matn = "This is a smple text with some erors in the sentnce."
tuzatilgan = fix_grammar(matn)

print("Asl matn:", matn)
print("Tuzatilgan matn:", tuzatilgan)
