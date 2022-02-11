# Resume Maker Portal App

The Resume Maker Portal App is an Open Source tool that helps you create a modern :fire: and professional resume!

- [x] Add your information once :sparkles:

- [x] Choose from our professional, elegant, creative, or modern resume templates :sparkles:

- [x] Get a personalize shareable link and showcase your hard-earned skills :smirk: and experience to potencial employers and clients :sparkles:

## Backend Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Frontend Requirements

- [Node.js](https://nodejs.org/en/)

## How to run the app:

1. Clone this repository:
   `git clone https://github.com/miguelalb/resume-portal-fastapi.git`
2. Add a `.env` file to the root of the project as shown in `example.env`
3. Start the stack with Docker Compose:
   `docker-compose up -d`

4. Use [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) to create the tables and run migrations:

   - If you made changes to the models: `docker-compose exec backend alembic revision --autogenerate -m "First migration"`
   - Otherwise just run: `docker-compose exec backend alembic upgrade head`

5. Run the tests using pytest:
   `docker-compose exec backend python -m pytest`

**Now you can open your browser and interact with these URLs:**

- Backend, JSON based web API based on OpenAPI: [http://localhost:6055](http://localhost:6055)

- Automatic interactive documentation with Swagger UI (from the OpenAPI backend): [http://localhost:6055/docs](http://localhost:6055/docs)

- Alternative automatic documentation with ReDoc (from the OpenAPI backend): [http://localhost:6055/redoc](http://localhost:6055/redoc)

- PGAdmin, PostgreSQL web administration: [http://localhost:6051](http://localhost:6051)

- VueJS Frontend: [http://localhost:6056](http://localhost:6056)
