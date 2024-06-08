from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
   return Response({"persin":"priyanshu","age":21})

@api_view(['POST'])
def start_scraping(request):

   return Response("kf")

@api_view(['GET'])
def scraping_status(request):
   request.GET.get("job_id")