from django.http import HttpResponseForbidden


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        raise Exception("Request stopped")
            # print("custom middleware before next middleware/vie w")
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each response after the view is called
        #
        print("custom middleware after response or previous middleware")

        return response



# class RejectSpambotRequestsMiddleware(object):
#
#     def process_request(self, request):
#         referer = request.META.get('HTTP_REFERER')
#         if referer == 'spambot_site_referer':
#             return HttpResponseForbidden() # reject the request and return 403 forbidden response
#
#         return # return None in case of a valid request