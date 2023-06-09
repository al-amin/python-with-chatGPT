SELECT AP_INVOICES.INVOICE_NUM, AP_INVOICES.SUPPLIER_NUM, SUM(AP_INVOICE_LINES.INVOICE_LINE_AMOUNT)
FROM AP_INVOICES
JOIN AP_INVOICE_LINES
ON AP_INVOICES.INVOICE_ID = AP_INVOICE_LINES.INVOICE_ID
GROUP BY AP_INVOICES.INVOICE_NUM, AP_INVOICES.SUPPLIER_NUM
HAVING SUM(AP_INVOICE_LINES.INVOICE_LINE_AMOUNT) > 1000;