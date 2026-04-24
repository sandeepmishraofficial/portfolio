import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.models import VisitorLog

logs = VisitorLog.objects.all()
for log in logs:
    print(f"[{log.timestamp}] IP: {log.ip_address}, Path: {log.path}, Method: {log.method}, UA: {log.user_agent}")
print(f"Total Logs: {logs.count()}")
