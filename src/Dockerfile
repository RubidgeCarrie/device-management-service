
FROM python:3.13


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt -t  /code


COPY ./app /code/app

# EXPOSE 8000
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]