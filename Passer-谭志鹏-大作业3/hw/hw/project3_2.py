from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
import bsddb

address=[]

@csrf_exempt

def index(request):
    address=[]

    
    database1=bsddb.hashopen('D:\Python2.7\hw\database\main.db','c')
    database2=bsddb.hashopen('D:\Python2.7\hw\database\website.db','c')
    words=[]
    
    if request.POST.has_key('q'):
        key=unicode(request.POST['q'])
        words=key.split()
    else:
        words=[]
    
    for i in range(0,305):
        tmpaddr={}
        f=open('D:\Python2.7\hw\html\\'+str(i)+'.html','r')
        html_content=f.read()
        num=len(words)
        for j in words:
            flag=re.search(j,html_content,re.I)
            if flag:
               num-=1
        if num==0:
            tmpaddr['index']=database1[str(i)]
            tmpaddr['url']=database2[str(i)]
            address.append(tmpaddr
                           )
    database1.close()
    database2.close()
    
    return render_to_response('searchResult.html', {'address': address})



def indexsort(filename,d):
    fin=open(filename)
    txt=fin.read()
    content1=''
    content2=''
    l1=re.findall('http://.+</a|http://.+<br',txt)
    for item in l1:
        #print str(item)
        a=re.findall('http://.+"',item)
        if a==[]:
            continue
        else:
            na=re.findall('http://[^"]+',str(a[0]))
            print na
        b=re.findall(">\w+\s+\w+<",item)
        if b==[]:
            continue
        else:
            nb=re.findall("\w+\s+\w+",str(b[0]))
            print nb
        if na==[] or nb==[]:
            continue
        else:
            d[str(nb[0])]=str(na[0])

