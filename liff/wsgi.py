import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'liff.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "liff.settings")