import json


def lambda_handler(event, context):
    """
    並不是一個很好的整合範例= =
    總之只是要用來呈現, launch.json 在:
    - direct invoke
    - template-based invoke
    - api gateway invoke

    的情境之下的 event 內容
    """
    print(f"event {event}")
    print(f"context: {context}")

    success, username = login(event)

    if success:
        # (模擬) API Gateway 的 debug 情境
        print(f"username: {username} 成功從 ApiGateway 登入")
        response = {"statusCode": 200, "body": "OK -- ApiGateway to Lambda Login"}
        return response
    else:
        username = event.get("username", None)
        password = event.get("password", None)
        print(f"=== username: {username}, password: {password} ===")

        response = {"statusCode": 200, "body": "hello from lambda"}

        return response


def login(event: dict):
    success = False

    u_name = get_value_from_event(event, "username")
    passwd = get_value_from_event(event, "password")

    # verify u_name && passwd
    if u_name == "TonyChou44" and passwd == "1234z":
        success = True

    return success, u_name


def get_value_from_event(payload: dict, key: str):
    if "body" in payload:
        payload = payload["body"]

    if type(payload) == str:
        try:
            payload = json.loads(payload)
        except Exception as err:
            print(str(err))

    value = payload.get(key, None)
    return value
