# Dockerfile for results-service
FROM openjdk:11-jre-slim

# Set the working directory
WORKDIR /app

# Copy the jar file into the container
COPY target/results-service.jar /app/results-service.jar

# Expose the application port
EXPOSE 8080

# Run the jar file
CMD ["java", "-jar", "results-service.jar"]
