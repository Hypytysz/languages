1. komendą '$ mkdir languages' tworzymy folder pod nasz projekt
wchodzimy do folderu projektu cd languages
2. tworzymy wirtualne środowisko '$ python -m venv venv'
3. aktywujemy wirtualne środowisko '$ source venv/Scripts/activate'
4. tworzymy plik requirements.txt, w którym umieszczamy wszystkie potrzebne rozszerzennia
5. instalujemy wszystkie potrzebne rozszerzenia'$ pip install -r requirements.txt'
6. tworzymy folder projektu '$ django-admin startproject languages .'
7. w folderze głównym (nie utworzonego w kroku 4!) languages tworzymy folder templates
8. w settings.py w miejscu templates ustawiamy 'DIRS': [BASE_DIR / 'templates'],
9. komendą '$ python manage.py startapp menu' dodajemy aplikację menu
10. rejestrujemy ją w settingsach
11. dodajemy tam także:
Installed Apps:
'django_extensions',
'debug_toolbar',
'crispy_forms',
'crispy_bootstrap5',
    
'menu.apps.AppsConfig'

Middleware:
'debug_toolbar.middleware.DebugToolbarMiddleware',

SHELL_PLUS_PRINT_SQL = True
LOGIN_REDIRECT_URL = "homepage"
LOGOUT_REDIRECT_URL = "homepage"
PASSWORD_REDIRECT_URL = "homepage"
CRISPY_ALLOWED_TEMPLATE_PACKS = 'Bootstrap5'
CRISPY_TEMPLATE_PACK = 'Bootstrap5'
12. wykonujemy migrację
13. dodajemy     path('__debug__/', include('debug_toolbar.urls')), do naszych urlsów projektu
14. 