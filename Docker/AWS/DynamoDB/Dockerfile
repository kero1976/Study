FROM openjdk:11

COPY . .

ENV PORT 8000

EXPOSE $PORT

CMD exec java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -port $PORT