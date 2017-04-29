# closetracing

## Prequire
* Python 2.7 or later(I use 2.7 in this example)
* pip 

## Installing guide for ubuntu (I have no money for mac so no guide for mac. As my experience the step in ubuntu are quite the same with ubuntu)
1. Install package in setup.py by: sudo python setup.py install
2. Download zipkin by running the command: 
  ```wget -O zipkin.jar 'https://search.maven.org/remote_content?g=io.zipkin.java&a=zipkin-server&v=LATEST&c=exec'```
3. zipkin.jar will be download, feel free to put it anywhere. Go to the folder that you locate zipkin.jar and run it by command: java -jar zipkin.jar
4. Running server by: python server.py
5. Running client by: python client.py

## Important
 You should run zipkin.jar before you run the server and client.
