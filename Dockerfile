FROM python:3.11
COPY app.py /app.py
RUN apt update -y
RUN apt install pip -y
RUN pip install flet
CMD ["/app.py"]
ENTRYPOINT ["python3"]