[This code's documentation lives on the grpc.io site.](https://grpc.io/docs/languages/python/quickstart)


```bash
$ git clone git@github.com:ldynia/grpc-python-helloworld.git hellogrpc/

$ docker run --rm -it -d --name grpc -w /app -v $PWD/hellogrpc:/app python:3.7 bash
$ docker exec grpc pip install grpcio grpcio-tools

$ code hellogrpc/
$ docker exec -it grpc bash

$ python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. greeter.proto
$ python server.py &
$ python client.py
```