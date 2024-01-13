import os
import pyperclip as pc
from dotenv import load_dotenv

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "pass.env")

load_dotenv(file_path)

Master_Password = os.getenv("Master_Password")

pc.copy(Master_Password)

