import random
import sys
from datetime import datetime

from faker import Faker

fake = Faker()
#TODO Move on to Faker

def get_sample_template():
    name = "Sample" + str(random.randint(0, sys.maxsize))
    content = "SampleContent" + str(random.randint(0, sys.maxsize))
    premium = random.choice([True, False])
    return {"name": name, "content": content, "premium": premium}


def get_sample_skill():
    return {
        "name": "SampleSkill" + str(random.randint(0, sys.maxsize)),
        "learning": random.choice([True, False]),
    }


def get_sample_job():
    return {
        "company": "SampleCompany" + str(random.randint(0, sys.maxsize)),
        "designation": "SampleDesignation" + str(random.randint(0, sys.maxsize)),
        "description": "SampleDescription" + str(random.randint(0, sys.maxsize)),
        "startdate": str(datetime.now().timestamp()),
        "current": random.choice([True, False]),
        "enddate": str(datetime.now().timestamp()),
    }


def get_sample_education():
    return {
        "college": "SampleCollege" + str(random.randint(0, sys.maxsize)),
        "designation": "SampleDesignation" + str(random.randint(0, sys.maxsize)),
        "description": "SampleDescription" + str(random.randint(0, sys.maxsize)),
        "startdate": str(datetime.now().timestamp()),
        "current": random.choice([True, False]),
        "enddate": str(datetime.now().timestamp()),
    }


def get_sample_certification():
    return {
        "name": "SampleName" + str(random.randint(0, sys.maxsize)),
        "issuing_organization": "SampleOrg" + str(random.randint(0, sys.maxsize)),
        "issue_date": str(datetime.now().timestamp()),
        "current": random.choice([True, False]),
        "expiration_date": str(datetime.now().timestamp()),
        "credential_id": "SampleID" + str(random.randint(0, sys.maxsize)),
        "credential_url": "https://sample.com/" + str(random.randint(0, sys.maxsize)),
    }


def get_sample_profile():
    return {
        "first_name": "SampleFirst" + str(random.randint(0, sys.maxsize)),
        "last_name": "SampleLast" + str(random.randint(0, sys.maxsize)),
        "public_name": "SamplePublic" + str(random.randint(0, sys.maxsize)),
        "summary": "SampleSummary" + str(random.randint(0, sys.maxsize)),
        "email": str(random.randint(0, sys.maxsize)) + "@email.com",
        "phone": str(random.randint(0, sys.maxsize)),
        "designation": "SampleDesignation" + str(random.randint(0, sys.maxsize)),
        "skills": [get_sample_skill() for i in range(5)],
        "jobs": [get_sample_job() for i in range(5)],
        "educations": [get_sample_education() for i in range(5)],
        "certifications": [get_sample_certification() for i in range(5)],
    }
