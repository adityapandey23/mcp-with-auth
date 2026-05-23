from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Here, you should the run operation to make sure the tables are created if not already created
  yield
  # Here, make sure that you close the database connection if it's open

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def api_key_auth(request: Request, call_next):
  """
  This middleware should do the following thing:- 
  - It shouldn't work on the route `/admin/generate-key` as 
    it'll be used to generate an api key

  - It should look for the `X-API-Key` in the headers of the 
    request (If not found, reject the request with apt error)

  - In case it is found, then cross check it with the database 
    that whether the given API key is valid or not, if not,
    reject the request with apt error. If everthing works fine,
    then do add the user details to the request state too.
  """
  return await call_next(request)

# Mount the route from admin and mcp