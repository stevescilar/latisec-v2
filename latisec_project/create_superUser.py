#!/usr/bin/env python
import os
import sys
import django

# Add project to path
sys.path.insert(0, '/home/latisecc/test.latisec.com/latisec_project')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'latisec_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Change these values to what you want
username = 'admin'
email = 'admin@latisec.com'
password = 'SecurePassword123!'  # Change this!

try:
    if User.objects.filter(username=username).exists():
        print(f'User "{username}" already exists.')
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Superuser "{username}" created successfully!')
        print(f'Username: {username}')
        print(f'Email: {email}')
        print('You can now login at: https://test.latisec.com/admin/')
except Exception as e:
    print(f'Error creating superuser: {e}')