# Stage 1: Build Stage
FROM maven:3.8.4-temurin-17 as builder

# Set the working directory to /app
WORKDIR /app

# Copy pom.xml and install dependencies (to leverage caching)
COPY pom.xml .

# Download dependencies to go offline
RUN mvn dependency:go-offline

# Copy the rest of the source code
COPY src /app/src

# Build the JAR file
RUN mvn clean package -DskipTests

# Stage 2: Runtime Stage
FROM eclipse-temurin:17-jdk-slim

# Set the working directory to /app
WORKDIR /app

# Copy the JAR file from the builder stage
COPY --from=builder /app/target/results-service.jar /app/results-service.jar

# Expose the port your app is running on (default for Spring Boot is 8080)
EXPOSE 8080

# Command to run the JAR file
CMD ["java", "-jar", "/app/results-service.jar"]
