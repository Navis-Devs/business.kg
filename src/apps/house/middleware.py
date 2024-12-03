from django.utils import translation

class LocaleHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.headers.get('locale')
        if language:
            translation.activate(language)
            request.LANGUAGE_CODE = language
        else:
            translation.activate('ru')  
        
        response = self.get_response(request)
        translation.deactivate()
        return response