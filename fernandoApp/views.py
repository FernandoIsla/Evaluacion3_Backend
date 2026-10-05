from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Paciente
from .serializers import PacienteSerializer


class PacienteListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        apellido = request.query_params.get('apellido', None)
        
        if apellido:
            pacientes = Paciente.objects.filter(apellido__icontains=apellido)
        else:
            pacientes = Paciente.objects.all()

        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PacienteDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def _get_object(self, run):
        try:
            return Paciente.objects.get(run=run)
        except Paciente.DoesNotExist:
            return None

    def get(self, request, run):
        paciente = self._get_object(run)
        if not paciente:
            return Response(
                {"error": f"Paciente con RUN {run} no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, run):
        paciente = self._get_object(run)
        if not paciente:
            return Response(
                {"error": f"Paciente con RUN {run} no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, run):
        paciente = self._get_object(run)
        if not paciente:
            return Response(
                {"error": f"Paciente con RUN {run} no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)