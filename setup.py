import keyring
keyring.set_password("openAI", "API-KEY", "API-KEY-SECRET")
print(keyring.get_password("openAI", "API-KEY"))
