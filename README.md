# Markers to Chapters Converter
A project that allows you to convert DaVinci Resolve marks to YouTube chapters

## Preparing the environment:

To prepare the environment, with Docker installed and running on the host machine, simply run the command below.

```shell
docker run -t -d -p 8080:80 --name markers-to-chapters-converter joaomateusferr/markers-to-chapters-converter:latest
```

If everything goes well, when accessing http://localhost:8080/ in the browser, the product upload page should appear.