from rapidfuzz import process
import re

def normalize_column(column: str):
    return re.sub(
        r'[^a-z0-9]',
        '',
        column.lower()
    )

COLUMN_PATTERNS = {
    "customer": [
        "customerid",
        "customer_id",
        "cust_id",
        "customer",
        "client_id"
    ],

    "date": [
        "invoicedate",
        "order_date",
        "purchase_date",
        "transaction_date",
        "date"
    ],

    "quantity": [
        "quantity",
        "qty",
        "units"
    ],

    "price": [
        "unitprice",
        "price",
        "amount",
        "sales"
    ],

    "product": [
        "description",
        "product",
        "product_name",
        "item",
        "item_name",
        "sku"
    ]
}

def detect_columns(columns):
    detected = {}
    print("Columns received:", columns)
    for target, aliases in COLUMN_PATTERNS.items():

        # Exact match first
        for column in columns:

            normalized_column = normalize_column(
                column
            )

            print(
                "PRODUCT CHECK:",
                column,
                normalized_column
            )

            if normalized_column in aliases:
                print(
                    "EXACT MATCH FOUND:",
                    column
                )

                detected[target] = column
                break

        if target in detected:
            continue

        best_match = None
        best_score = 0

        for column in columns:

            normalized_column = normalize_column(
                column
            )

            match = process.extractOne(
                normalized_column,
                aliases
            )

            if match and match[1] > best_score:
                best_match = column
                best_score = match[1]

        if best_score >= 70:
            detected[target] = best_match

    return detected