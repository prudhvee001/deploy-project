FROM openjdk:11-jdk-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the pom.xml file and install dependencies
COPY pom.xml .

RUN mvn dependency:go-offline

# Copy the rest of the source code
COPY . .

# Build the application (will generate the JAR file)
RUN mvn clean package -DskipTests

# Use a new image to run the application
FROM openjdk:11-jre-slim

WORKDIR /app

# Copy the generated JAR file from the builder image
COPY --from=builder /app/target/results-service.jar /app/results-service.jar

# Expose the port the application will run on
EXPOSE 8080

# Command to run the application
ENTRYPOINT ["java", "-jar", "/app/results-service.jar"]
