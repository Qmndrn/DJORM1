import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


if __name__ == '__main__':
    
    posts = Passcard.objects.all()
    active = Passcard.objects.filter(is_active=True)

    print(f'Имя владельца: {posts[0].owner_name}\n активный: {posts[0].passcode}\n дата создания: {posts[0].created_at}\n статус: {posts[0].is_active}')

    print('\nКоличество пропусков:', Passcard.objects.count())  # noqa: T001

    print('Активные пропуска: ', len(active))

