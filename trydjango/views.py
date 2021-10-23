"""
Purpose of a views.py file = to render HTML webpages 
"""

import random 
from django.http import HttpResponse

def home_view(request):
    """
    Take in a request (Django sends request).
    Return HTML as a response (that we decide).
    """
    number = random.randint(10, 1230981234)
    name = "Rachael"
    HTML_STRING = f"<h1>Hello {name} - #{number}!</h1>"
    
    return HttpResponse(HTML_STRING)  