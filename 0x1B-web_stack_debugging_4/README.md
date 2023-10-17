# Web Stack Debugging 4
This project involves making Nginx perform well under  multiple load
Specifically, the apache bench is used to apply multiple loads to the nginx
```
ab -c 100 -n 2000
```
this benchmarking result shows that the system cannot  withstand enough loads as some requests results into failure.

After the Nginx configuration is adjusted, the server now performs well and handles all requests.
