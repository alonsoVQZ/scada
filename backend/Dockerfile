FROM python:3.10.13
WORKDIR .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src:create_app()"]
