from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader

# Create your views here.
from booking.forms import BookingForm


def createbooking(request):

    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = BookingForm()
        args ={}
        args['form'] = form

    return render_to_response('booking/booking.html',args)