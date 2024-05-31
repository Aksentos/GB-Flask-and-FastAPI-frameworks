import logging
from fastapi import APIRouter, HTTPException
from models import Task, TaskIn
from db import db, tasks
from typing import List



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


task_router = APIRouter()


