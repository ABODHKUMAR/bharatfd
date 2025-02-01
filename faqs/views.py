from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from rest_framework import status
from .serializers import FAQSerializer
from django.shortcuts import render

def faq_page(request):
    return render(request, "faq.html")

@api_view(["GET"])
def faq_list(request):
    lang = request.GET.get("lang", "en")
    faqs = FAQ.objects.all()
    
    data = [{"question": faq.get_translation(lang), "answer": faq.get_translation(lang)} for faq in faqs]
    return Response(data)

@api_view(["POST"])  
def create_faq(request):
    serializer = FAQSerializer(data=request.data)
    if serializer.is_valid():
        
        faq = serializer.save()

        return Response(FAQSerializer(faq).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def faq_page(request):
    return render(request, "faq.html")

def add_fag_page(request):
    return render(request, 'add_faq.html')