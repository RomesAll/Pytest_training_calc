FROM python:3.12-slim
RUN groupadd -r g_python && useradd -r -g g_python roman
RUN pip install --upgrade pip
RUN pip install pytest
WORKDIR /src
COPY . .
USER roman
EXPOSE 8000
CMD [ "python", "src/main.py"]