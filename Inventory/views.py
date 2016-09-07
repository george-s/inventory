from django.shortcuts import render
from django.http import HttpResponse, Http404

from Inventory.models import Item
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

def countdown(request):
	    return render(request, 'Inventory/countdown.html',{
        		
        	})

def countdownjs(request):
	    return render(request, 'Inventory/countdownjs.html',{
        		
        	})



