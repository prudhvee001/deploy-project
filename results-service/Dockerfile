# Use Maven image to build the Java application
FROM maven:3.8.4-openjdk-17-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the pom.xml and the source code to the container
COPY pom.xml ./
COPY src ./src

# Install dependencies and build the application
RUN mvn clean install -DskipTests

# Use an OpenJDK image to run the Spring Boot application
FROM openjdk:17-jdk-slim

# Set the working directory
WORKDIR /app

# Copy the built JAR file from the builder stage
COPY --from=builder /app/target/results-service.jar /app/results-service.jar

# Expose the port the app runs on
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "/app/results-service.jar"]
