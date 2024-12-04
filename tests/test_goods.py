import json

def test_get_goods_positive_user(uds_client_positive):
    status, response = uds_client_positive.get_goods(max_items=5, offset=0)
    assert status == 200, f"Expected 200, got {status}"
    data = json.loads(response)
    assert "rows" in data, "Response should contain 'rows'"
    assert "total" in data, "Response should contain 'total'"

def test_get_goods_negative_user(uds_client_negative):
    status, response = uds_client_negative.get_goods(max_items=5, offset=0)
    assert status == 401, f"Expected 401, got {status}"

def test_create_category_negative_user(uds_client_negative):
    status, response = uds_client_negative.create_category(name="Одежда", external_id="одежда")
    assert status == 401, f"Expected 401, got {status}"

def test_create_category_positive_user_error(uds_client_positive):
    status, response = uds_client_positive.create_category(name="Одежда", external_id="одежда")
    assert status == 400, f"Expected 400, got {status}"

def test_create_category_positive_user(uds_client_positive):
    status, response = uds_client_positive.create_category(name="Test1", external_id="test1")
    assert status == 200, f"Expected 200, got {status}"
    data = json.loads(response)
    print("Вывод данных:", data.get("id"))
    assert "name" in data, "Response should contain 'name'"
    assert "data" in data, "Response should contain 'data'"
    
def test_create_item_negative_user(uds_client_negative):
    data = {
         "type": "VARYING_ITEM",
        "photos": ["NTQ5NzU1ODIxNDg5L0dPT0RTLzdiYzBlNTU0LWMyNzMtNDc1MC05MjEyLWY0NWJhNWM1ODZiOQ=="],
        "variants": [
            {"name": "Variant A", "price": 10.0, "inventory": {"inStock": 5}},
            {"name": "Variant B", "price": 15.0, "inventory": {"inStock": 3}},],
    }
    status, response = uds_client_negative.create_item(name="Applefsd", external_id="apple_item", data=data)
    assert status == 401, f"Expected 401, got {status}"

def test_create_item_positive_user_photo_error(uds_client_positive):
    data = {
         "type": "VARYING_ITEM",
        "photos": ["NTQ5NzU1ODIxNDg5L0dPT0RTLzdiYzBlNTU0LWMyNzMtNDc1MC05MjEyLWY0NWJhNWM1ODZiOQ=="],
        "variants": [
            {"name": "Variant A", "price": 10.0, "inventory": {"inStock": 5}},
            {"name": "Variant B", "price": 15.0, "inventory": {"inStock": 3}},],
    }
    status, response = uds_client_positive.create_item(name="Applefsd", external_id="apple_item", data=data)
    assert status == 400, f"Expected 400, got {status}"

def test_get_good_by_not_available_id_positive_user(uds_client_positive):
    good_id = 1
    status, response = uds_client_positive.get_good_by_id(good_id)
    assert status == 404, f"Expected 404, got {status}"

def test_get_good_by_available_id_positive_user(uds_client_positive):
    good_id = 8568023
    status, response = uds_client_positive.get_good_by_id(good_id)
    assert status == 200, f"Expected 200, got {status}"
    data = json.loads(response)
    assert "name" in data, "Response should contain 'name'"
    assert "data" in data, "Response should contain 'data'"

def test_get_good_by_available_id_negative_user(uds_client_negative):
    good_id = 8568023
    status, response = uds_client_negative.get_good_by_id(good_id)
    assert status == 401, f"Expected 401, got {status}"

def test_update_category_by_available_id_positive_user(uds_client_positive):
    category_id = "8568023"
    update_data = {
        "name": "Test2",
        "nodeId": None,
        "hidden": None,
        "externalId": "test2",
        "data": {
            "type": "CATEGORY"
        }
    }
    status, response = uds_client_positive.update_category(category_id, update_data)
    assert status == 200, f"Expected 200, got {status}"
    data = json.loads(response)
    assert "name" in data, "Response should contain 'name'"
    assert "data" in data, "Response should contain 'data'"

def test_update_category_by_not_available_id_positive_user(uds_client_positive):
    category_id = "1"
    update_data = {
        "name": "Test2",
        "nodeId": None,
        "hidden": None,
        "externalId": "test2",
        "data": {
            "type": "CATEGORY"
        }
    }
    status, response = uds_client_positive.update_category(category_id, update_data)
    assert status == 404, f"Expected 404, got {status}"

def test_update_category_by_available_id_negative_user(uds_client_negative):
    category_id = "8568023"
    update_data = {
        "name": "Test2",
        "nodeId": None,
        "hidden": None,
        "externalId": "test2",
        "data": {
            "type": "CATEGORY"
        }
    }
    status, response = uds_client_negative.update_category(category_id, update_data)
    assert status == 401, f"Expected 401, got {status}"

def test_delete_category_by_available_id_negative_user(uds_client_negative):
    good_id = 8568316
    status, response = uds_client_negative.delete_category(good_id)
    assert status == 401, f"Expected 401, got {status}"

def test_delete_category_by_available_id_positive_user(uds_client_positive):
    good_id = 8568316
    status, response = uds_client_positive.delete_category(good_id)
    assert status == 204, f"Expected 204, got {status}"
    status, response = uds_client_positive.get_good_by_id(good_id)
    assert status == 404, f"Expected 404, got {status}"

def test_delete_category_by_not_available_id_positive_user(uds_client_positive):
    good_id = 1
    status, response = uds_client_positive.delete_category(good_id)
    assert status == 404, f"Expected 404, got {status}"