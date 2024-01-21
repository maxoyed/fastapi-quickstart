# FastAPI Quick Start

## 一、环境变量

创建 `.env` 文件，填入以下配置：

```shell
IMAGE_NAME=fastapi-quickstart # 将用做构建镜像名称
PORT=8001 # Docker 容器暴露端口
```

## 二、启动容器

```shell
docker compose up -d --build
```