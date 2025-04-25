# Stage 1: Build Stage (with Maven)
FROM maven:3.8.4-temurin-17 as builder

# Set the working directory in the container
WORKDIR /app

# Copy the pom.xml file to the container
COPY pom.xml .

# Download all the dependencies (this will help Docker cache the dependencies for future builds)
RUN mvn dependency:go-offline

# Copy the rest of the source code to the container
COPY src ./src

# Build the application (the JAR file will be created in the target folder)
RUN mvn clean package -DskipTests

# Stage 2: Runtime Stage (with OpenJDK and Spring Boot)
FROM eclipse-temurin:17-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the built JAR file from the build stage
COPY --from=builder /app/target/results-service-0.0.1-SNAPSHOT.jar /app/results-service.jar

# Expose port 8080 for the application to be accessible externally
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "/app/results-service.jar"]
