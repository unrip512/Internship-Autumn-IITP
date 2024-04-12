import uvicorn

from core.app import get_application
from core.system import System

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")


