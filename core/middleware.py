from .models import VisitorLog

class TrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # We only want to track successful page views to avoid bot spam of 404s, but to be comprehensive, we'll log it before the response.
        # However, ignoring admin paths and static/media files is a good idea.
        path = request.path
        if not path.startswith('/admin/') and not path.startswith('/secure-admin-portal/') and not path.startswith('/static/') and not path.startswith('/media/'):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            user_agent = request.META.get('HTTP_USER_AGENT', '')
            method = request.method

            # We can choose to ignore superusers
            if not request.user.is_superuser:
                VisitorLog.objects.create(
                    ip_address=ip,
                    user_agent=user_agent,
                    path=path,
                    method=method
                )

        response = self.get_response(request)
        return response
