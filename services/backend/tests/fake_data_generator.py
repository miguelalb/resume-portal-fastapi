import random
import sys
from datetime import datetime

from faker import Faker

#TODO Move on to Faker
fake = Faker()


def get_sample_template():
    name = "Sample" + str(random.randint(0, sys.maxsize))
    content = "SampleContent" + str(random.randint(0, sys.maxsize))
    premium = random.choice([True, False])
    return {"name": name, "content": content, "premium": premium}


def get_sample_skill():
    return {
        "name": random.choice(["Python", "Go", "Kubernetes", "Java", "Javascript", "Docker", "AWS", "GCP", "Azure", "Machine learning"]),
        "learning": random.choice([True, False]),
    }


def get_sample_job():
    return {
        "company": fake.company(),
        "designation": fake.job(),
        "description": fake.catch_phrase(),
        "startdate": str(datetime.now().timestamp()),
        "current": random.choice([True, False]),
        "enddate": str(datetime.now().timestamp()),
    }


def get_sample_education():
    return {
        "college": fake.company(),
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
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "public_name": fake.color_name().lower() + fake.last_name().lower(),
        "summary": fake.paragraph(nb_sentences=6),
        "email": fake.ascii_email(),
        "phone": fake.phone_number(),
        "designation": fake.job(),
        "website": "https://www."+fake.domain_name(),
        "skills": [get_sample_skill() for i in range(5)],
        "jobs": [get_sample_job() for i in range(5)],
        "educations": [get_sample_education() for i in range(5)],
        "certifications": [get_sample_certification() for i in range(5)],
    }
