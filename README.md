# python-with-chatGPT
python-with-chatGPT

# Setup
Create a API-KEY from [openai.com](https://platform.openai.com/account/api-keys) website and add/update this to **setup.py** file

# How to use python-chatgpt
```python3 python-chatgpt.py "go through files in Downloads folder , check their dates and if they are older than 30 days, move them to a folder called to_delete" "clean-downloads.py"```

# How to use sql-chatgpt
```python3 sql-chatgpt.py "find the names of all customers who have placed more than 10 orders in the past year" "get-customer-sql.sql"```

or

```python3 sql-chatgpt.py "I have two tables AP_INVOICES and AP_INVOICE_LINES. The tables are connected using a common column called INVOICE_ID. Write a SQL Script to get INVOICE_NUM and SUPPLIER_NUM from AP_INVOICES table, and Sum of INVOICE_LINE_AMOUNT from AP_INVOICE_LINES table, where Sum of INVOICE_LINE_AMOUNT is greater than 1000" "get-sum-sql.sql"```
