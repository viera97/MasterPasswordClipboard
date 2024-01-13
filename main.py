import os
from dotenv import load_dotenv
import pynput

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "pass.env")

load_dotenv(file_path)

Master_Password = os.getenv("Master_Password")

keyboard = pynput.keyboard.Controller()

keyboard.type(Master_Password)