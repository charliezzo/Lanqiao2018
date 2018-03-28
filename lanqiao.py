import requests 
import re

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', 'Cookie': '这里从网页复制cookie'}    #自己填写cookie

for i in range(1,496):
    txtcode = requests.get('http://lx.lanqiao.cn/problem.page?gpid=T'+str(i), headers = headers)
    r = r'tit">&nbsp; (.*?) &nbsp'
    a =  re.findall(r,txtcode.content)

    with open(str(i)+a[0]+'.html', 'wb') as f:
        f.write(txtcode.content)
    print i

