FROM python:3.14-slim

WORKDIR /app

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# copy project files
COPY pyproject.toml .
COPY README.md .
COPY core/ core/
COPY cli/ cli/
COPY utils/ utils/

# install package
RUN uv pip install --system -e .

# create directories for data
RUN mkdir -p data/raw data/processed index

# default: interactive search mode
CMD ["python", "-m", "cli.search"]
