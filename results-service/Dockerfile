# Stage 1: Build stage using Maven and Eclipse Temurin JDK 17
FROM maven:3.8.4-eclipse-temurin-17 AS builder

WORKDIR /app

# Copy pom.xml and dependencies to the container
COPY pom.xml .

# Download dependencies in offline mode
RUN mvn dependency:go-offline

# Copy all the source files
COPY src /app/src

# Package the application
RUN mvn clean package -DskipTests

# Stage 2: Runtime stage using Eclipse Temurin JDK 17 (lightweight version)
FROM eclipse-temurin:17-jdk

WORKDIR /app

# Copy the JAR file from the builder stage
COPY --from=builder /app/target/results-service.jar /app/results-service.jar

EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "/app/results-service.jar"]
