FROM rasa/rasa-sdk:3.2.0

WORKDIR /app
USER root
COPY ./actions /app/actions

USER 1001