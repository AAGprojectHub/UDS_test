import base64
import uuid
from datetime import datetime
from http.client import HTTPSConnection
import json

class UDSClient:
    BASE_URL = "api.uds.app"

    def __init__(self, company_id, api_key):
        self.company_id = company_id
        self.api_key = api_key

    def _get_headers(self):
        auth_string = base64.b64encode(f"{self.company_id}:{self.api_key}".encode()).decode()
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {auth_string}",
            "X-Origin-Request-Id": str(uuid.uuid4()),
            "X-Timestamp": datetime.now().isoformat(),
        }

    def _make_request(self, method, url, body=None):
        connection = HTTPSConnection(self.BASE_URL)
        headers = self._get_headers()
        connection.request(method, url, body=json.dumps(body) if body else None, headers=headers)
        response = connection.getresponse()
        return response.status, response.read()

    def get_goods(self, max_items=10, offset=0, node_id=None):
        url = f"/partner/v2/goods?max={max_items}&offset={offset}"
        if node_id:
            url += f"&nodeId={node_id}"
        return self._make_request("GET", url)

    def create_category(self, name, external_id):
        body = {
            "name": name,
            "nodeId": None,
            "externalId": external_id,
            "data": {"type": "CATEGORY"},
        }
        return self._make_request("POST", "/partner/v2/goods", body)

    def create_item(self, name, external_id, node_id=None, data=None):
        body = {
            "name": name,
            "nodeId": node_id,
            "externalId": external_id,
            "data": data,
        }
        return self._make_request("POST", "/partner/v2/goods", body)

    def get_good_by_id(self, good_id):
        url = f"/partner/v2/goods/{good_id}"
        return self._make_request("GET", url)

    def update_category(self, category_id, data):
        url = f"/partner/v2/goods/{category_id}"
        return self._make_request("PUT", url, data)

    def delete_category(self, category_id):
        return self._make_request(method="DELETE",url=f"/partner/v2/goods/{category_id}")
