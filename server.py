from concurrent import futures

import grpc

import greeter_pb2
import greeter_pb2_grpc


class Greeter(greeter_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return greeter_pb2.HelloResponse(message='Hello, %s!' % request.name)

    # def SayHelloAgain(self, request, context):
    #     return greeter_pb2.HelloResponse(message='Hello again, %s!' % request.name)


# Run Server
if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
