from django.shortcuts import redirect
from http.client import HTTPResponse
import requests,json
from django.http import JsonResponse
from graph import methods as grm


def getCitations(req):
    if req.method=='GET':
        paperId=req.GET.get('paperId')
        # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        return JsonResponse({"data":grm.getCitations(paperId)},safe=False)
    
def getReferences(req):
    if req.method=='GET':
        paperId=req.GET.get('paperId')
        # paperId='649def34f8be52c8b66281af98ae884c09aef38b'
        return JsonResponse({"data":grm.getReferences(paperId)},safe=False)
# def getFirstOrderresultnew