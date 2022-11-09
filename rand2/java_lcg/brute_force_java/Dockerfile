FROM openjdk:17
COPY Main.java /tmp/Main.java
WORKDIR /tmp
RUN javac Main.java
ENTRYPOINT ["java","Main"]