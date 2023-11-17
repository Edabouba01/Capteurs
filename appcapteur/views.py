from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
import psycopg2

# Create your views here.

class MesurApi(APIView):
    def get(self, request):
        conn = psycopg2.connect(
            database="temphum",
            user="postgres",
            password="Marikoben10",
            host="localhost"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mesures")
        mesures = cursor.fetchall()
        print(mesures)  # Ajoutez cette ligne pour afficher les données dans la console

        total_mesures = len(mesures)  # Total mesures
        data = {'mesures': mesures, 'total_mesures': total_mesures}
        return Response(data)
    
class temperaturApi(APIView):
    def get(self, request):
         conn = psycopg2.connect(
            database="temphum",
            user="postgres",
            password="Marikoben10",
            host="localhost"
        )
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM temperature")
         temperatures = cursor.fetchall()
         print(temperatures)  # Ajoutez cette ligne pour afficher les données dans la console

         total_temperatures = len(temperatures)  # Total mesures
         temp = {'temperatures': temperatures, 'total_temperatures': total_temperatures}
         return Response(temp)
    
class pressionApi(APIView):
    def get(self, request):
         conn = psycopg2.connect(
            database="temphum",
            user="postgres",
            password="Marikoben10",
            host="localhost"
        )
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM pression")
         pressions = cursor.fetchall()
         print(pressions)  # Ajoutez cette ligne pour afficher les données dans la console

         total_pressions = len(pressions)  # Total mesures
         press = {'pressions': pressions, 'total_pressions': total_pressions}
         return Response(press)
     
     
     