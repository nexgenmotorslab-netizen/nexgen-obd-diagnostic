from fastapi import FastAPI, HTTPExeception, Depends
from fastapi.middleware,cors import  CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAutho