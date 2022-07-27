FROM rasa/rasa:3.2.2-full

USER root
COPY ./ /app
#train rasa
RUN rasa train 

USER 1001 