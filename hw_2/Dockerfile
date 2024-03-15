FROM python:3.11


RUN apt-get update && \
    apt-get install -y texlive-latex-base

RUN pip install -i https://test.pypi.org/simple/ shushakov_hw_2

CMD python -m hw_2.tex && pdflatex example.tex && mkdir -p output && mv example.pdf /output


