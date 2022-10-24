FROM python:3.7
ADD pipeline_executor.py /pipeline_executor.py
ADD requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python","/pipeline_executor.py"]