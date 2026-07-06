import requests
import time

from utils import generate_sale
from config import API_URL, DELAY

print("Generating Sales...")

while True:

    sale = generate_sale()

    response = requests.post(API_URL, json=sale)

    print("Sent:", sale)

    time.sleep(DELAY)