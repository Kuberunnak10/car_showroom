import redis

redis_host = 'localhost'
redis_port = 6379
redis_db = 0

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

all_keys = redis_client.scan_iter(match='*')

for key in all_keys:
    print(f"Ключ: {key}, Значение: {redis_client.get(key)}")
