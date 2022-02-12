import random
import sys

{
  "first_name": "string",
  "last_name": "string",
  "public_name": "string",
  "theme": "string",
  "summary": "string",
  "email": "string",
  "phone": "string",
  "designation": "string",
  "skills": [],
  "jobs": [],
  "educations": [],
  "certifications": []
}

def get_random_user():
    username = "SampleUser" + str(random.randint(0,sys.maxsize))
    password = "SamplePassword" + str(random.randint(0,sys.maxsize))
    return {"username": username, "password": password}

def get_sample_skill():
    pass


def get_sample_job():
    pass

def get_sample_education():
    pass

def get_sample_certification():
    pass

def get_sample_profile():
    pass
