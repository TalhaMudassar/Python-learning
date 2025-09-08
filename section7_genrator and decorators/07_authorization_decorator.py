from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied! Admin only")
            return None
        else:
            return func(user_role)
    return wrapper
    
@require_admin
def access_tea_invertery(role):
    print("Access granted to tea inventery")
    
access_tea_invertery("admin")
access_tea_invertery("user")
    