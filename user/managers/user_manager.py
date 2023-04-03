from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, identification=None, is_active=False, password=None):
        print('why')
        if not email:
            print('why1')
            raise ValueError('아이디가 입력되지 않았습니다.')
        print('why2')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_active=is_active,
        )
        print('why3')
        user.set_password(password)
        print('why5')
        user.is_admin = False
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)
        print('why4')
        return user

    def create_superuser(self, email, identification=None, is_active=True, password=None):
        user = self.create_user(
            identification=identification,
            email=email
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

