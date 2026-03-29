# Build stage
FROM eclipse-temurin:17-jdk-alpine as builder

WORKDIR /app

COPY build.gradle settings.gradle gradlew ./
COPY gradle gradle/
RUN ./gradlew dependencies

COPY src ./src
RUN ./gradlew clean build -x test

# Run stage(final image)
FROM eclipse-temurin:17-jre-alpine
WORKDIR /usr/app
# Copy only the jar from the build stage
COPY --from=builder /app/build/libs/spring-petclinic-*.jar /usr/app

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "sprint-petclinic-*.jar"]
