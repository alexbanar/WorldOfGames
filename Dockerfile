FROM python:3-alpine
COPY MainScores.py /
EXPOSE 5000
COPY ./Scores.txt /
COPY ./requirements.txt /
RUN pip install -r ./requirements.txt
CMD ["python3", "./MainScores.py"]