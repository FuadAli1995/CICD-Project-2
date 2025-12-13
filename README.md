# Docker Learning

This project demonstrates a simple Flask application connected to a MySQL database, and shows the difference between a **single-stage** Docker build and a **multi-stage** Docker build.

Using a multi-stage build keeps the final image lightweight by compiling dependencies (such as `mysqlclient`) in a temporary build stage. This avoids shipping heavy build tools in the final image.

---

## Single-Stage Image

Building using a single-stage Dockerfile:

```bash
docker build -t single-stage-image .
```

![Image1](Images/Image1.png)


## Multi-Stage Image
By introducing build stages, we compile dependencies in an earlier stage and copy only the necessary runtime files into the final image. This significantly reduces the final image size:

```bash
docker build -t multi-stage-image .
```

![Image2](Images/Image2.png)











# CICD-Project-2
