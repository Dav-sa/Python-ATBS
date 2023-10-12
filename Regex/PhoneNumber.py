import pyperclip, re

frenchPhoneRegex = re.compile(r"(^(?:(?:\+|00)33|0)\s*1-9{4}$)")

frenchPhoneNumber = "+33 6 41 52 63 48"

emailRegex = re.compile(
    r"^(?=.{1,256})(?=.{1,64}@.{1,255}$)(?=[^@]*[A-Za-z0-9!#$%&'*+/=?^_`{|}~-])(?=[^@]*[A-Za-z0-9!#$%&'*+/=?^_`{|}~-][^@]*@)(?=[^@]*[A-Za-z0-9!#$%&'*+/=?^_`{|}~-][^@]*\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]{2,})(?:.{1,64}|[^@]+)@(?:[^@]{1,63}\.){1,125}[A-Za-z]{2,63}$"
)

text = str(pyperclip.paste())
result = frenchPhoneRegex.findall(frenchPhoneNumber)

print(result)
