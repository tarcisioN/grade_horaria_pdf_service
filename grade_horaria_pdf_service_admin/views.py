from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import grade_horaria_pdf_service_admin.phantomjs.phantomjs as phantomjs


def index(request, grade_oid):

    url ='https://www.siga.ufrj.br/sira/repositorio-curriculo/distribuicoes/' + grade_oid + '.html'

    pdf = phantomjs.get_pdf(url)

    return HttpResponse(pdf.read(), content_type='application/pdf')


@api_view(['GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
@never_cache
def clear_cache(request):

    from django.core.cache import cache

    try:
        cache.clear()
    except AttributeError:
        pass

    return Response('Cache cleared')