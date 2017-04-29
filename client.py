#!/usr/bin/python           # This is client.py file
# coding=utf-8
import socket             
import opentracing
import zipkin_ot.tracer
import json
import sys

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))

if __name__ == '__main__':

    with zipkin_ot.Tracer(service_name = 'Weather-client', # config opentracing to zipkin server
        collector_host = 'localhost',
        collector_port =9411,
        verbosity = 1) as tracer:
        opentracing.tracer = tracer

    while True:
        with opentracing.tracer.start_span('Weather information') as parent_span:
            text_carrier = {}
            opentracing.tracer.inject(parent_span.context, opentracing.Format.TEXT_MAP, text_carrier)
            with opentracing.start_child_span(parent_span, 'Client process') as client_span:
                with opentracing.start_child_span(client_span, 'Get location') as getLocation_span:
                    address = raw_input("Enter the address: ")
                with opentracing.start_child_span(client_span, 'Send location') as sendLocation_span:
                    message = json.dumps(text_carrier)
                    s.send(message)
                s.send(address)
        weatherInfor = s.recv(1024)
        print weatherInfor            
        parent_span.finish()
    s.close()
