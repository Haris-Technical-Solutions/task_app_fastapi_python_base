from fastapi import Request


class RoleMiddleware:
    def __init__(self):
        print('from role middleware')
        pass
    def __call__(self, request: Request, call_next, response):
        pass