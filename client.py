import grpc

import greeter_pb2
import greeter_pb2_grpc


# Run Client
if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        # Read server stub
        stub = greeter_pb2_grpc.GreeterStub(channel)

        # Make a gRPC call/request to SayHello function
        response = stub.SayHello(greeter_pb2.HelloRequest(name='Lukasz'))
        print("Greeter client received: " + response.message)

        # # Make a gRPC call/request to SayHelloAgain function
        # response = stub.SayHelloAgain(greeter_pb2.HelloRequest(name='Lukasz'))
        # print("Greeter client received: " + response.message)
