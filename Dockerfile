FROM python:3.9

COPY . .

RUN make deps
