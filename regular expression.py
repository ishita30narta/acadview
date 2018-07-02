import re
'''nameage ="ABc is 18 year old"\
          "Cde is 15 year old"
names=re.findall(r'[A-Z][a-z]*',nameage)
print(names)

ages=re.findall('\d{1,3}',nameage)
print(ages)'''


emails="Ishitanarta@gmail.com" \
       "abc@gmail.com" \
       "xyz@gmail.com"


match=re.findall("[\w.+$%_+-]{1,20}[@][\w]{1,20}[.][\w]{1,3}",emails)
print(match)

a="hat cat rat mat"
regrex=re.compile("[l-z]at")
strr=regrex.sub("strr",a)
print(strr)


