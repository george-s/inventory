from django.shortcuts import render
from django.http import HttpResponse, Http404
from Inventory.models import Item
import Inventory.targetProcess
import requests
import json



def index(request):
	items = Item.objects.exclude(amount=0)
	#return HttpResponse('<p>In index view </p>')
	return render(request, 'Inventory/index.html', {
		'items':items,
		})

def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
        #return HttpResponse('<p>In item_detial with id {0}</p>'.format(id))
        return render(request, 'Inventory/item_detail.html',{
        		'item': item,
        	})

def tprequests(request):
	    tp = Inventory.targetProcess.Target_Process('http://unmarkedtek.tpondemand.com/api/v1/','MTp6bDlMT3R6NS9mMEpqMDBLRkhoVFBWSXZMa2hLMktUYWRzTkNYc3IxYm0wPQ==')
	    result = tp.get_objects_as_et('Requests')
	    return render(request, 'Inventory/tprequests.html',{
        	'result': result,	
        	})

def countdownjs(request):
	    return render(request, 'Inventory/countdownjs.html',{
        		
        	})



