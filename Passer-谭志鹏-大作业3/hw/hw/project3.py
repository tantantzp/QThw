from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re

address=[]

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
     

@csrf_exempt

def index(request):
    address=[]
    d={}
    a={}
    indexsort("D:\Python2.7\hw\hw\information.txt",d)
    if request.POST.has_key('q'):
        key=str(request.POST['q'])
        if d.has_key(key):
            a['index']='1'
            a['url']=d[key]
    #a={'index':'1','url':'1.html'}
    #b={'index':'2','url':'2.html'}
    #c={'index':'3','url':'3.html'}
    #d={'index':'4','url':'4.html'}
    address.append(a)
    #address.append(b)
    #address.append(c)
    #address.append(d)
    return render_to_response('searchResult.html', {'address': address})

#indexsort("information")

        



