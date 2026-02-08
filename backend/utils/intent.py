def detect_intent(text):
    text = text.lower()

    if "refund" in text:
        return "REFUND_STATUS"

    if "return" in text:
        return "RETURN_STATUS"

    if "delivery" in text or "where is" in text or "when will" in text:
        return "DELIVERY_STATUS"

    if "order" in text:
        return "ORDER_STATUS"

    return "GENERAL"
