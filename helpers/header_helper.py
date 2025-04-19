import uuid

def get_header():
    return {
        "x-correlationid": "Insider Load Test" + str(uuid.uuid1()),
        "x-agentname": "Insider Load Test",
        "x-executor-user": "Insider Load Test"
    }