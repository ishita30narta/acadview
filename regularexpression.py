#1
import re
emails="zuck26@facebook.com"\
        "page33@google.com"\
        "jeff42@amazon.com"
ids=re.findall(r'([\w]{1,20}[\w]{1,20})[@]([\w]{1,9})[.]([\w]{1,3})',emails)
print(ids)


#2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
name=re.findall(r'[Bb]\w*',text)
print(name)

#3
import re
sentence = "A, very very; irregular_sentence"
sen=re.sub(r'[,;_\s]',' ',sentence)
print(sen)