#Python Regex Challenge: Enhancing E-Commerce Operations
import re
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
# Tag each product based on keywords in the description
# Your code here

electronics = ""
apparel = ""
home_kitchen = ""

for x in descriptions:
    item_res = re.split(" ", x)
    if 'screen' in item_res or 'screen'.capitalize() in item_res:
        electronics += "Electonic : Smartphone"
    if 'cotton' in item_res or 'cotton'.capitalize() in item_res:
       apparel += "Apparel : T-Shirt"
    if 'knife'.capitalize() in item_res or 'knife' in item_res:
        home_kitchen += "Home and Kitchen : Knife Set"

print(electronics)
print(apparel)
print(home_kitchen)