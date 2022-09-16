
class DisableCSRFMiddleware(object):

    def init(self, get_response):
        self.get_response = get_response

    def call(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response