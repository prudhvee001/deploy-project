FROM openjdk:11-jre-slim
WORKDIR /app
COPY target/results-service.jar /app/results-service.jar
EXPOSE 3003
CMD ["java", "-jar", "results-service.jar"]
