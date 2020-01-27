from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import InventoryForm, ClientForm
from .models import Item, Client


def inventory_list(request):
    items = Item.objects.all()
    data = {
        'items': items,
    }
    return render(request, 'inventory/inventory_list.html', data)


def inventory_new(request, item=None):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()

    return render(request, 'inventory/inventory_form.html', {
        'form': form,
    })


def inventory_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'inventory/inventory_detail.html', {
        'item': item
    })


def inventory_edit(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            item.title = form.cleaned_data['title']
            item.photo = form.cleaned_data['photo']
            item.desc = form.cleaned_data['desc']
            item.price = form.cleaned_data['price']
            item.amount = form.cleaned_data['amount']
            item.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=item)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
        }
        return render(request, 'inventory/inventory_form.html', context)


def inventory_delete(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('inventory_list')

def num_plus(request,pk):
    item = Item.objects.get(pk=pk)
    item.amount= item.amount+1
    item.save()
    return redirect('inventory_list')

def num_minus(request,pk):
    item = Item.objects.get(pk=pk)
    item.amount= item.amount-1
    item.save()
    return redirect('inventory_list')

def client_list(request):
    clients = Client.objects.all()
    data = {
        'clients': clients
    }
    return render(request, 'inventory/client_list.html', data)


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'inventory/client_detail.html', {
        'client': client
    })


def client_new(request, client=None):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    return render(request, 'inventory/client_form.html', {
        'form': form,
    })


def client_edit(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            client.tel = form.cleaned_data['tel']
            client.name = form.cleaned_data['name']
            client.address = form.cleaned_data['address']
            client.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
        }
        return render(request, 'inventory/client_form.html', context)


def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('client_list')
