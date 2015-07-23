import json

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from strings_convertions.constants import alphabet_map

class MyRESTView(APIView):

    def string_processing(self, input_string):
        output_directory = {}
        output_directory['input'] = input_string
        if input_string:
            input_list = input_string.split(',')
            numeric_output = []
            sorted_output = []
            for item in input_list:
                temp = []
                for alphabat in item:
                    try:
                        temp.append(alphabet_map[alphabat])
                    except KeyError:
                        pass
                if temp:
                    numeric_output.append(temp)
                    sorted_output.append(sorted(temp, key=int))
        else:
            numeric_output = "no input given"
            sorted_output = "no input given"

        output_directory['numeric'] = numeric_output
        output_directory['sorted'] = sorted_output

        return output_directory

    def get(self, request):
        input_string = request.GET.get('_content', None)
        result = self.string_processing(input_string)
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def post(self, request):
        input_string = request.POST.get('_content', None)
        result = self.string_processing(input_string)
        response = Response(result, status=status.HTTP_200_OK)
        return response

def home(request):

    data = None
    if request.method == "POST":
        input_string = request.POST.get('_content')
        rest_full_obj = MyRESTView()
        data = rest_full_obj.string_processing(input_string)

    context = {
        'data': data
    }
    return render_to_response("index.html", context, context_instance=RequestContext(request))


