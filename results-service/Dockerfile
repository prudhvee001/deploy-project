# Use Maven image to build the Java application
FROM maven:3.8.4-openjdk-17-slim as builder

WORKDIR /app

# Copy the pom.xml file to the container
COPY pom.xml .

# Download the dependencies
RUN mvn dependency:go-offline

# Copy the source code to the container
COPY src /app/src

# Build the application
RUN mvn clean package -DskipTests

# Use a smaller openjdk image to run the application
FROM openjdk:17-slim

WORKDIR /app

# Copy the packaged jar from the builder stage
COPY --from=builder /app/target/results-service.jar /app/results-service.jar

# Expose the application's port
EXPOSE 8080

# Command to run the application
ENTRYPOINT ["java", "-jar", "results-service.jar"]
