import random
import time
import redis


# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# r.set('foo', 'bar')

STEAM_KEY = "jobs"

JOB_TYPES = [
  "cleaning",
  "room_service",
  "taxi",
  "extra_towels",
  "extra_pillows"
]

r = redis.Redis(decode_responses=True)

while True:
  job = {
    "room": random.randint(100,500),
    "job": random.choice(JOB_TYPES)
  }

  job_id = r.xadd(STEAM_KEY, job)
  print(f"Created job {job_id}:")
  print(job)

  time.sleep(random.randint(5,15))