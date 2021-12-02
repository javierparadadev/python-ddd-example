
FROM python:3.9

WORKDIR /code

COPY ./ /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt


CMD ["make", "run"]
