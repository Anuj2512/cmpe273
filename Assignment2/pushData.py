'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2
import datastore_pb2_grpc

class DatastoreClient():
    '''
    '''

    def __init__(self, host='0.0.0.0', port=3000):
        '''
        '''
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2_grpc.DatastoreStub(self.channel)
        print("Client is running...")

    def put(self, key, value):
        '''
        '''
        response = self.stub.putData(datastore_pb2.PutRequest(key=key, value=value))
        return response

    def get(self, key):
        '''
        '''
        response = self.stub.getData(datastore_pb2.GetRequest(key=key))
        return response

client = DatastoreClient()


response = client.get("1")
print(response.key, response.value)

response = client.put("1", "Data20")
print(response.key, response.value)

response = client.get("1")
print(response.key, response.value)

