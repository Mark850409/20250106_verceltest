# 使用 langflow 的最新版本作為基礎映像
FROM langflowai/langflow:latest

# 設置容器啟動命令
CMD ["python", "-m", "langflow", "run", "--host", "0.0.0.0", "--port", "7860"]