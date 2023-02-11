import requests
def getCitations(str):
    # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
    paperId=str
    # print(paperId)
    link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/citations?fields=isInfluential,paperId,title,referenceCount,citationCount'
    res=requests.get(link)
    # print(res.status_code)
    result=res.json()['data']
    offset=100
    flag=1
    
    while flag!=0:
        link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/citations?fields=isInfluential,paperId,title,referenceCount,citationCount&offset={offset}'
        res2=requests.get(link)
        result2=res2.json()['data']
        flag=len(result2)
        result.extend(result2)
        # print(offset,flag)
        offset+=100
        
    
    # print(result[0])
    resultnew=[]
    for ires in result:
        if ires['isInfluential']==True:
            resultnew.append(ires["citingPaper"])
    if len(resultnew)<20:
        for ires in result:
            if ires['isInfluential']==False:
                resultnew.append(ires["citingPaper"])

    return resultnew


def getReferences(str):
    # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
    paperId=str
    link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/references?fields=isInfluential,paperId,title,referenceCount,citationCount'
    res=requests.get(link)
    # print(res.status_code)
    result=res.json()['data']
    offset=100
    flag=1
    
    while flag!=0:
        link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/references?fields=isInfluential,paperId,title,referenceCount,citationCount&offset={offset}'
        res2=requests.get(link)
        result2=res2.json()['data']
        flag=len(result2)
        result.extend(result2)
        # print(offset,flag)
        offset+=100
        
    
    print(len(result))
    resultnew=[]
    for ires in result:
        if ires['isInfluential']==True:
            resultnew.append(ires["citedPaper"])
    if len(resultnew)<20:
        for ires in result:
            if ires['isInfluential']==False:
                resultnew.append(ires["citedPaper"])

    return resultnew

def getCitationsLimited(str):
    # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
    paperId=str
    # print(paperId)
    link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/citations?fields=paperId,title,referenceCount,citationCount&offset=0&limit=5'
    res=requests.get(link)
    # print(res.status_code)
    result=res.json()['data']

    return result


def getReferencesLimited(str):
    # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
    paperId=str
    link=f'https://api.semanticscholar.org/graph/v1/paper/{paperId}/references?fields=paperId,title,referenceCount,citationCount'
    res=requests.get(link)
    # print(res.status_code)
    result=res.json()['data']
       
    return result




def nested_citations(paperId):
    allCitations=getCitationsLimited(paperId)
    level1=[]
    

    for item in allCitations:
        # print(item["paperId"])
        level1.append(getCitationsLimited(paperId))
    return level1

level1=getCitationsLimited('649def34f8be52c8b66281af98ae884c09aef38b')
print(level1)
