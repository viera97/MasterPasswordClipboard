import os
import pyperclip as pc
from dotenv import load_dotenv

load_dotenv('pass.env')

Master_Password = os.getenv("Master_Password")

pc.copy(Master_Password)

