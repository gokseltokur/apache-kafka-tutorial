# Kafka

**Why one should be using Kafka?**

Simplify the backend architecture.

1. Universal pipeline of data across multiple applications and services. Data integration
2. Simplify the backend architecture.
3. Connects to existing systems
4. Processing data in real-time

Kafka works on the publish-subscribe pattern. It allows some of the applications to act as producers and publish the records to Kafka topics. Similarly, it allows some of the applications to act as consumers and subscribe to Kafka topics and process the records produced by it

Each of these brokers has partitions which are leaders and those that are replicas. This allows for an incredible level of fault tolerance through your system. When the system is functioning normally, all reads and writes to a topic go through the leader and the leader makes sure that all the other brokers are updated.

**Installation - Windows ( You need to run shell as administrator.)**

- Step 1) Install Java SDK

```bash
choco install jdk8
```

- Step 2) Download Apache Kafka Binaries from the link (Scala): [https://kafka.apache.org/downloads](https://kafka.apache.org/downloads)
- Step 3) Extract files to C:/ directory
- Step 4) Create data folder and /kafka and /zookeeper directories inside of it.
- Step 5) Update config/zookeper.properties configuration file.

```bash
dataDir = C:/kafka/data/zookeper
```

- Step 6) Update config/server.properties configuration file.

```bash
log.dirs = C:/kafka/data/kafka
```

- Step 7) Go to bin/windows directory inside of the kafka.

```bash
cd C:/{kafka - You need to write your directory name here}/bin/windows
```

- Step 8) Start the zookeeper

```bash
.\zookeeper-server-start.bat ../../config/zookeper.properties
```

- Step 9) Start the Apache Kafka

```bash
.\kafka-server-start.bat ../../config/server.properties
```

**Creating & Examining Kafka topics**

```bash
.\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sample

.\kafka-topics.bat --list --zookeeper localhost:2181

.\kafka-topics.bat --describe --zookeeper localhost:2181 --topic sample
```

**Install kafka-python**

```bash
pip install kafka-python
```

Firstly, start the kafka-consumer

kafka-consumer.py

```python
from kafka import KafkaConsumer
consumer = KafkaConsumer('sample', auto_offset_reset='earliest', group_id=None)
for message in consumer:
    print (message)
```

Then, run kafka-producer

kafka-producer.py

```python
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
print('sended')
producer.flush()
producer.close()
```

kafka-producer sends message to the kafka-consumer. Consumer receives the message and it will show it.


**Kafka-CLI Producer and Consumer**

```
.\kafka-console-producer.bat --broker-list localhost:9092 --topic test_topic
```
Keep running, then

```
.\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test_topic --from-beginning
```

Send some messages from the producer terminal then you will see it on the consumer's terminal.

