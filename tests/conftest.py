import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.uds_client import UDSClient

@pytest.fixture
def uds_client_positive():
    company_id = "549756189636"
    api_key = "OTBhZmRmOTctOGIzMS00ZDM5LWE5YjAtZmE2NDNiZjc3Yzky"
    return UDSClient(company_id, api_key)

@pytest.fixture
def uds_client_negative():
    company_id = "549798369636"
    api_key = "OTBhZmRmOTctOGIzMS00ZDM5LKFu2FktZmE2NDNiZjc3Yzky"
    return UDSClient(company_id, api_key)
