FROM python
RUN pip install pandas
WORKDIR /app
COPY pipeline.py pipeline.py
CMD ["python","pipeline.py"]