import pickle
from pathlib import Path

import streamlit_authenticator as stauth 



names =["SPS","MSPS"]
usernames = ["SPS","MSPS"]
passwords = ["xxxxxx","xxxxxxx"]

hash_password = stauth.Hasher(passwords).generate()

file_p=Path(__file__).parent/"password_key.pk1"
with file_p.open("wb") as file :
    pickle.dump(hash_password, file)
