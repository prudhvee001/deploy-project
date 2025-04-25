# Stage 1: Build the application using Maven
FROM maven:3.8.4-openjdk-17-slim as builder

WORKDIR /app

# Copy the pom.xml and dependencies to the container
COPY pom.xml .

# Download dependencies (this speeds up the build if we don't change dependencies)
RUN mvn dependency:go-offline

# Copy the rest of the source code
COPY src /app/src

# Build the application
RUN mvn clean package -DskipTests

# Stage 2: Run the application
FROM eclipse-temurin:17-jdk-slim

WORKDIR /app

# Copy the built jar file from the builder stage
COPY --from=builder /app/target/results-service.jar /app/results-service.jar

# Expose the application port
EXPOSE 8080

# Run the jar file
ENTRYPOINT ["java", "-jar", "/app/results-service.jar"]
