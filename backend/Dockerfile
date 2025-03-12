FROM python:3.10-buster AS py-build

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -

COPY . /app
WORKDIR /app
ENV PATH=/opt/poetry/bin:$PATH
RUN poetry config virtualenvs.in-project true && poetry install


FROM python:3.10-slim-buster

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends bash curl libpq5 postgresql-client

EXPOSE 8000
COPY --from=py-build /app/ /app/
WORKDIR /app/

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "-m", "fastapi", "run", "./app/main.py", "--reload", "--port", "8000"]

# http://localhost:8000/docs