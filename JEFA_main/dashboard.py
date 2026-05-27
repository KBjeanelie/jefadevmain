from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from jet.dashboard.modules import DashboardModule, AppList

class CustomIndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        self.children.append(AppList(
            title='Applications',
            exclude=['django.contrib.*']
        ))
        self.children.append(AppList(
            title='Administration',
            models=['django.contrib.*'],
        ))

class CustomAppIndexDashboard(AppIndexDashboard):
    columns = 2
