from django.shortcuts import redirect
from http.client import HTTPResponse
import requests,json
from django.http import JsonResponse
from graph import methods as grm


def getCitations(req):
    if req.method=='GET':
        paperId=req.GET.get('paperId')
        print(paperId)
        # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        data=grm.getReferences(paperId)
        return JsonResponse({"data":data},safe=False)
    
def getReferences(req):
    if req.method=='GET':
        paperId=req.GET.get('paperId')
        # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        data=grm.getReferences(paperId)
        return JsonResponse({"data":data},safe=False)
# def getFirstOrderresultnew

def nested_citations(req):
    if req.method=='GET':
        # paperId=req.GET.get('paperId')
        paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        return JsonResponse({"data":grm.nested_citations(paperId)},safe=False)
