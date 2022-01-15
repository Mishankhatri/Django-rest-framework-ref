from rest_framework.throttling import UserRateThrottle

class AdminThrottleRate(UserRateThrottle):
    scope = 'admin' #