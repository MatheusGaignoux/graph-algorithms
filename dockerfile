FROM python:3.9

WORKDIR /graph-algorithms

COPY traversal_search traversal_search
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "traversal_search/bfs_2d_grid.py", "-s", "0,0", "-d", "5,5", "-o", "1,1 3,2 2,4", "-e", "4,3"]
