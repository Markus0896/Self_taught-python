import re
line = "123345$%@привет"
m = re.findall("\d", line, re.IGNORECASE)
print(m)
