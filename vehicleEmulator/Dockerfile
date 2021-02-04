FROM golang:latest
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN go get "github.com/gorilla/websocket"
RUN go get "github.com/icrowley/fake"
RUN go build -o main .
ENTRYPOINT /app/main
EXPOSE 8080
