from pathlib import Path
from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = Env(
    PYTHON_ENVIRONMENT=(str, "DEVELOPMENT"),
)

Env.read_env(BASE_DIR / ".env", overwrite=True)

if env("PYTHON_ENVIRONMENT") == 'PRODUCTION':
    Env.read_env(BASE_DIR / ".env.production", overwrite=True)
