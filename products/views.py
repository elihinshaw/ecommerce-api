from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class ProductsView(APIView):
    def get(self, request, format=None):
        url = "https://fakestoreapi.com/products/"

        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response(
                {"error": f"Request failed with status code {response.status_code}"}
            )
