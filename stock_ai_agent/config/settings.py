import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model Settings
MODEL_NAME = os.getenv("MODEL_NAME", "llama3-70b-8192")

# Data Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data")

# Database
DB_PATH = os.path.join(DATA_PATH, "database.db")
