## Run the app locally

````bash
docker build -t python-restful-api .
````

````bash
docker run -p 5001:5001 python-restful-api
````

Go to: http://localhost:5001/api/v1/resource

## See application logs

````bash
docker ps
````

````bash
docker logs <container_id>
````