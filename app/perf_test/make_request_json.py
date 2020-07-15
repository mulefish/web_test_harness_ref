import json

class CreateBinderRequest():

    def get_dummy_binder_request(self):
        payload = {
            "one":1,
            "two":"a",
            "jwt": "pretend token",
            "amountToPay":10.1
        }
        return payload


if __name__ == "__main__":
    cbr = CreateBinderRequest()
    data = cbr.get_dummy_binder_request()
    json_formatted_str = json.dumps(data, indent=2)
    print(json_formatted_str)