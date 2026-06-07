# Build stage
FROM gradle:9.2.1-jdk17-alpine AS builder

WORKDIR /app

COPY build.gradle settings.gradle ./
COPY gradle gradle/
RUN gradle dependencies --no-daemon

COPY src ./src
RUN gradle clean build -x test --no-daemon

# Run stage (final image)
FROM eclipse-temurin:17-jre-alpine
WORKDIR /usr/app
# Copy only the jar from the build stage
COPY --from=builder /app/build/libs/spring-petclinic-*.jar /usr/app/app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/usr/app/app.jar"]
