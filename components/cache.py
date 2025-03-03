import redis
import os
import pickle
from dotenv import load_dotenv

load_dotenv()

try:
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        password=os.getenv("REDIS_PASSWORD"),
        decode_responses=False
    )
    redis_client.ping()
except Exception as e:
    print("Redis não disponível:", e)
    redis_client = None

def set_cache(key, value, expire=600):
    if redis_client:
        try:
            redis_client.setex(key, expire, pickle.dumps(value))
        except Exception as e:
            print("Erro ao setar cache:", e)

def get_cache(key):
    if redis_client:
        try:
            data = redis_client.get(key)
            return pickle.loads(data) if data else None
        except Exception as e:
            print("Erro ao obter cache:", e)
            return None
    return None
