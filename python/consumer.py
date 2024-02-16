import random
import time
import redis


STEAM_KEY = "jobs"

JOB_TYPES = [
  "cleaning",
  "room_service",
  "taxi",
  "extra_towels",
  "extra_pillows"
]

r = redis.Redis(decode_responses=True)

last_job_id = 0

while True:
  print("Checking for jobs...")
  response = r.xread(streams={STEAM_KEY: last_job_id}, count=1, block= 5000)

  if len(response) == 0:
    print("Nothing to do right now, sleeping...")
    time.sleep(5)
  else: 
    job = response[0]
    print(job)
    current_job_id = job[1][0][0]
    current_job_details = job[1][0][1]
    print(f"Performing job {current_job_id}: {current_job_details}")
    time.sleep(random.randint(2,6))
    last_job_id = current_job_id
