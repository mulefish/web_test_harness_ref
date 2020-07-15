"""Send a binder request and time it. Concurrent perf test"""

import concurrent.futures
import json
import logging
import requests
import time
from make_request_json import CreateBinderRequest

cbr = CreateBinderRequest() # Factory to create realistic JSON 'binder' requests
loop_number = 0 
total_time = 0

def thread_function(thread_id):
    # How come loop_number and total_time need to be declared 'global' but cbr does not?
    global loop_number 
    global total_time

    try:
        raw = cbr.get_dummy_binder_request()
        raw
        headers = {
            "accept":"application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(raw["jwt"])
        }
        data = json.dumps(raw)
        response = requests.post(url, headers=headers, data=data)
        the_time = response.elapsed.total_seconds()
        the_status = response.status_code
        logging.info("|{}|{}|{}|{}|{}{}|".format(loop_number, thread_id, "make_binder_payment", the_time, the_status, raw["amountToPay"]))
        loop_number += 1
        total_time += the_time
    except Exception as boom:
        print("Failure {}".format(boom))

if __name__ == "__main__":
    url = "https:// <REDACTED> /binder_payments"
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    print("when|loop|id|test|time|status|amount_to_pay|")
    max_workers = 10 # max concurrent threads
    max_loops = 100 # number of requests to make 
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(thread_function, range(max_loops))
    ave = total_time / loop_number

    """meta info"""
    print("URL | {}".format(url))
    print("WORKERS | {}".format(max_workers))
    print("LOOPS | {}".format(max_loops))
    print("AVERAGE | {}".format(ave, total_time, loop_number))
    print("The end")
