from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router.conversation_api import router as conversation_router

app = FastAPI(
    title="Tech Challenge API",
    description="API for the Tech Challenge",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development purposes
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


app.include_router(conversation_router)

@app.get("/health")
async def health_check():
    """
    Endpoint to check the health of the API.
    Returns a simple message indicating the API is running.
    """
    return {"status": "API is running smoothly."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)