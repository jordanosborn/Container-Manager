FROM python:3

RUN pip install inflection

CMD [ "python", "./test_script.py" ]