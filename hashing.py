from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def hash_password(password):
        return pwd_context.hash(password)
    def verify(password1, password2):
        return pwd_context.verify(password2, password1)