import keyring
keyring.set_password("openAI", "API-KEY", "API-KEY-SECRET") # replace the API-KEY-SECRET with your open AI secret API-KEY
print(keyring.get_password("openAI", "API-KEY"))
