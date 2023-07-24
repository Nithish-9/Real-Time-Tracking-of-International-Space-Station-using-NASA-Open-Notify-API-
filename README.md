# Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API

## Project Description

The **Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API** project fetches real-time data from NASA about the International Space Station (ISS) using the Open Notify API. The data is provided in JSON format, including the UNIX timestamp, latitude, longitude, and success message. The project utilizes Apache Kafka, Apache Spark (PySpark), and MySQL to process and store the data for further analysis.

## Purpose

The purpose of this project is to **track and monitor the real-time location of the International Space Station**. By leveraging Apache Kafka, the project creates three Kafka topics for acceleration, speed, and the current location of the ISS. Individual tables are then created in the MySQL database to store data for each topic.

---

## How to Run

Install MySQL on your Ubuntu system.

Open the MySQL terminal using the command: mysql -u root -p.

Execute the command to set up the MySQL user password.

Create a database named "spaceStation" using the code provided in the "schema.txt" file.

Start the ZooKeeper server using the command: bin/zookeeper-server-start.sh config/zookeeper.properties.

Start the Kafka server using the command: bin/kafka-server-start.sh config/server.properties.

Run the Apache Spark application using the command: spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 spark_streaming.py.

In the producer code, specify the URL of the Open Notify API **(http://api.open-notify.org/iss-now.json)** and create the Kafka topics to send the data to. The consumer code, written in PySpark, subscribes to the Kafka topics and stores the received data into the specified MySQL tables. The acceleration data is calculated using the Haversian formula, which calculates the distances between two locations based on their latitudes and longitudes, and the same applies to the speed data.

## Data Collected

![image](https://github.com/Nithish-9/Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API-/assets/113118468/39307518-8ea2-464a-929f-e4a7275e219c)

![image](https://github.com/Nithish-9/Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API-/assets/113118468/3b5a3607-4316-4542-821c-965c1b94f560)

![image](https://github.com/Nithish-9/Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API-/assets/113118468/37810b2d-5eeb-4c56-8da4-143aeb540102)

![image](https://github.com/Nithish-9/Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API-/assets/113118468/135ac1c7-b3cf-4385-be23-a21d61d594c6)

![image](https://github.com/Nithish-9/Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API-/assets/113118468/71f54d41-236e-434b-9b54-3837474ed075)

![image](https://github.com/Nithish-9/Real-Time-Tracking-of-International-Space-Station-using-NASA-Open-Notify-API-/assets/113118468/ce6e3f0b-bbfc-4a0a-8982-d92dddf19c9a)

                          
