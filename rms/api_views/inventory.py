from ..models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import reverse
from rms import models
from datetime import datetime
from django.utils.timezone import localtime, make_aware


@login_required
def tag_search_view(request):
    if 'search' in request.GET:
        tags = Tag.objects.filter(name__contains=request.GET['search'])
        return_value = []
        for tag in tags:
            return_value.append(tag.name)
        return JsonResponse(return_value, status=200, safe=False)
    return HttpResponse('', 400)


@csrf_exempt
@login_required
def tag_add_view(request):
    if request.method == 'POST' and 'name' in request.POST:
        tag = Tag(name=request.POST['name'])
        tag.save()
        return HttpResponse('', 201)
    return HttpResponse('', 400)


@csrf_exempt
@login_required
def add_reservation_to_device(request, device_id):
    try:
        device = models.Device.objects.get(id=device_id)
        if request.POST and 'reservation' in request.POST and 'amount' in request.POST:
            try:
                reservation = models.Reservation.objects.get(id=request.POST.get('reservation'))
                device.add_to_reservation(reservation, int(request.POST['amount']))
                return HttpResponse('', status=200)
            except models.Reservation.DoesNotExist:
                pass
            except ValueError as error:
                return HttpResponse(str(error), status=400)
        return HttpResponse('', status=400)
    except models.Device.DoesNotExist:
        return HttpResponse('', status=404)


@login_required
def device_reservations_json(request, device_id):
    try:
        device = models.Device.objects.get(id=device_id)
        reservations = []
        reservation_base = device.reservationdevicemembership_set
        if 'start' in request.GET:
            start = datetime.strptime(request.GET['start'], '%Y-%m-%d')
            reservation_base.filter(reservation__end_date__gte=start)
        if 'end' in request.GET:
            end = datetime.strptime(request.GET['end'], '%Y-%m-%d')
            reservation_base.filter(reservation__start_date__lte=end)
        for reservation in reservation_base.all():
            reservations.append({
                'start': localtime(reservation.reservation.start_date).isoformat(),
                'end': localtime(reservation.reservation.end_date).isoformat(),
                'url': reverse('reservation', kwargs={'reservation_id': reservation.reservation.id}),
                'title': '{} {}'.format(reservation.reservation.full_id, reservation.reservation.name),
                'description': 'Anzahl: {}'.format(reservation.amount),
            })
        return JsonResponse(reservations, status=200, safe=False)
    except models.Device.DoesNotExist:
        return HttpResponse('Device not found', status=404)
