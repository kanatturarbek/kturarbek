import re
file = open('row.txt',encoding='utf8')
text=file.read()
name_of_company=r"\nФилиал.*(?P<name>\b[A-Z]+)"
bin=r"\nБИН.*(?P<bin>\b[0-9]+)"
tytle=r"(?P<item_name>.*)\n{1}(?P<count>.*)x(?P<unit_price>.*)\n{1}.*\n{1}Стоимость\n{1}(?P<total_price>.*)"
# print(text)*
# x=re.search(name_of_company,text).group("name")
x=re.search(name_of_company,text)
y=re.search(bin,text)
z=re.compile(tytle)
print(x.group(1))
print(y.group(1))
for match in re.finditer(z,text):
    print(match.group("item_name"))
    print(match.group("count"))
    print(match.group("unit_price"))
    print(match.group("total_price"))
# itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
# itemPattern = re.compile(itemPatternText)
# for m in re.finditer(itemPattern, text):
#     print(m.group("name") + "\n" + " " + m.group("count")+ "\n" + m.group("price") + "\n"+ m.group("total1"))
Date_adress=r"\nВремя: (?P<date>.*)\n(?P<adress>.*)"
dater=re.search(Date_adress,text).group("date")
addd=re.search(Date_adress,text).group("adress")
print(dater)
print(addd)
file.close()