# Use an official Python runtime as a parent image
FROM python:3.11-slim

COPY ./lab45_autogen_extension-0.1.1-py3-none-any.whl lab45_autogen_extension-0.1.1-py3-none-any.whl
RUN pip install lab45_autogen_extension-0.1.1-py3-none-any.whl

COPY ./agents/<agent folder name> /Platform-laip/<agent folder name>

WORKDIR /Platform-laip/<agent folder name>

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]