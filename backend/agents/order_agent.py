from backend.memory.mongodb import orders_col, payments_col


def handle_order_query(order_id, user_id, intent_hint=None):

    order = orders_col.find_one({
        "order_id": order_id,
        "user_id": user_id
    })

    if not order:
        return "I couldn’t find this order under your account."

    delivery_status = order.get("delivery_status")
    expected_delivery = order.get("expected_delivery_date")
    return_status = order.get("return_status")
    refund_status = order.get("refund_status")

    if intent_hint in ["DELIVERY_STATUS", "ORDER_STATUS"]:
        if delivery_status == "OUT_FOR_DELIVERY":
            return f"Your order {order_id} is out for delivery and expected by {expected_delivery}."
        if delivery_status == "SHIPPED":
            return f"Your order {order_id} has been shipped."
        if delivery_status == "DELIVERED":
            return f"Your order {order_id} has been delivered."
        return f"Your order {order_id} is currently in '{delivery_status}' status."

    if intent_hint in ["RETURN_STATUS", "REFUND_STATUS"]:
        if refund_status == "REFUND_PROCESSED":
            payment = payments_col.find_one({"order_id": order_id})
            return (
                f"Your refund has been processed. "
                f"It may take {payment['expected_credit_days']} to reflect in your account."
            )
        if return_status:
            return f"Return status is '{return_status}'. Refund status is '{refund_status}'."
        return "This order has not been returned."

    return f"Order {order_id} status: delivery='{delivery_status}'."
