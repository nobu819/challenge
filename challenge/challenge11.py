import re
text = "The ghost that says boo haunts the loo"

a = re.findall(".oo", text, re.IGNORECASE)
print(a)