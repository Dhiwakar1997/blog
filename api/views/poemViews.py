from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from api.serializers.poemSerializer import PoemSerializer
from api.utils.apiFeatures import APIFeatures
from api.utils.decorators import errorCatch
from api.models.poems.models import Poems

class PoemViews(APIView):
    #@errorCatch #error carching decorator
    def get(self,request,format=None):
        queryset=APIFeatures(Poems,request).filter().sort().paginate().limitFields()
        data=queryset.extract()
        return Response(data=data)

    #@errorCatch
    def post(self,request,format=None):
        obj=Poems(**request.data.dict())
        obj.save()
        return Response('post done')