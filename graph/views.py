from django.shortcuts import redirect
from http.client import HTTPResponse
import requests,json
from django.http import JsonResponse
from graph import methods as grm

def findAuthorDetails(req):
    if req.method=='GET':
        author=req.GET.get("author")
        print(author)
        link=f'https://api.semanticscholar.org/graph/v1/author/search?query={author}'
        res=requests.get(link).json()['data']
        authors=[]
        for i in res:
            authors.append(i['authorId'])
        headers = {'content-type': 'application/json'}
        data={"ids": authors}
        link='https://api.semanticscholar.org/graph/v1/author/batch?fields=url,name,paperCount,papers,papers.title,papers.openAccessPdf'
        result = requests.post(link,data=json.dumps(data), headers=headers).json()
        return JsonResponse(result,safe=False)
        

# 
# def getCitations(req):
    # if req.method=='GET':
        paperID=req.GET.get('paperId')   
        # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        # link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/citations?fields=isInfluential,paperId,title'
        # res=requests.get(link)
        print(res.status_code)
        # result=res.json()['data']
        # offset=100
        # flag=1
        # 
        # while flag!=0:
            # link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/citations?fields=isInfluential,paperId,title&offset={offset}'
            # res2=requests.get(link)
            # result2=res2.json()['data']
            # flag=len(result2)
            # result.extend(result2)
            ## print(offset,flag)
            # offset+=100
            # 
        # 
        ##print(result[0])
        # resultnew=[]
        # for ires in result:
            # if ires['isInfluential']==True:
                # resultnew.append(ires["citingPaper"])
        # if len(resultnew)<20:
            # for ires in result:
                # if ires['isInfluential']==False:
                    # resultnew.append(ires["citingPaper"])
    # 
        # return JsonResponse({"data":resultnew},safe=False)
# 
# 
# def getReferences(req):
    # if req.method=='GET':
        ##paperID=req.GET.get('paperId')   
        # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        # link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/references?fields=isInfluential,paperId,title'
        # res=requests.get(link)
        ##print(res.status_code)
        # result=res.json()['data']
        # offset=100
        # flag=1
        # 
        # while flag!=0:
            # link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/references?fields=isInfluential,paperId,title&offset={offset}'
            # res2=requests.get(link)
            # result2=res2.json()['data']
            # flag=len(result2)
            # result.extend(result2)
            ##print(offset,flag)
            # offset+=100
            # 
        # 
        # print(len(result))
        # resultnew=[]
        # for ires in result:
            # if ires['isInfluential']==True:
                # resultnew.append(ires["citedPaper"])
        # if len(resultnew)<20:
            # for ires in result:
                # if ires['isInfluential']==False:
                    # resultnew.append(ires["citedPaper"])
    # 
        # return JsonResponse({"data":resultnew},safe=False)
# 
def getCitations(req):
    if req.method=='GET':
        # paperId=req.GET.get('paperId')
        paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        return JsonResponse({"data":grm.getCitations(paperId)},safe=False)
    
def getReferences(req):
    if req.method=='GET':
        # paperId=req.GET.get('paperId')
        paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        return JsonResponse({"data":grm.getReferences(paperId)},safe=False)
# def getFirstOrderresultnew