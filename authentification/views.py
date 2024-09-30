from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from application import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from . tokens import generateToken
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from rest_framework import viewsets
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.http import HttpResponseRedirect

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.views.decorators.csrf import csrf_exempt

from requests.exceptions import RequestException
from time import sleep, timezone
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from django.http import JsonResponse
from geopy.geocoders import Nominatim
import ipdb

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import user_passes_test
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required




@csrf_exempt
def flutter_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            username = request.POST.get('username')
            password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
        else:
            
                token, _ = Token.objects.get_or_create(user=user)  # Get or create token
                # Return a JSON response with the token
                return JsonResponse({'token': token.key, 'message': 'Login successful'}, status=200)
           
    return JsonResponse({'error': 'Invalid request method'}, status=405)

from .models import Alert
from .serializers import AlertSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlertSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_alert(request):
    serializer = AlertSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=request.user)  # Save alert with logged-in user
        
        # Create a message for WebSocket
        alert_message = {
            'user': request.user.username,
            'alert_type': serializer.validated_data['alert_type'],
            'address': serializer.validated_data['address'],
            'created_at': serializer.instance.created_at.isoformat(),
            # Add other necessary fields
        }
        
        # Broadcast to WebSocket global_notify group
        channel_layer = get_channel_layer()
        print( 'get_channel_layer')
        async_to_sync(channel_layer.group_send)(
            'global_notify',  # Send to the global group
            {
                'type': 'send_alert',  # Method name in ChatConsumer
                'message': alert_message
            }
        )
        
        return Response({'message': 'Alert created successfully'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)