from fastapi import FastAPI
import model
from routes import router
from database import engine
from debug_toolbar.middleware import DebugToolbarMiddleware

# model.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.include_router(router, prefix="/book", tags=["book"])
app.add_middleware(
    DebugToolbarMiddleware,
    )