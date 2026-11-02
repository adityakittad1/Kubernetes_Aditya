# Flask and Express on Minikube

## Prerequisites
Install Docker Desktop, Minikube, kubectl, Node.js, and Python 3.12. Start Docker Desktop before starting Minikube.

## Build and deploy (PowerShell, from this folder)
```powershell
minikube start --driver=docker
minikube image build -t kubernetes-assignment-backend:1.0 .\backend
minikube image build -t kubernetes-assignment-frontend:1.0 .\frontend
kubectl apply -f .\k8s\backend.yaml
kubectl apply -f .\k8s\frontend.yaml
kubectl rollout status deployment/backend
kubectl rollout status deployment/frontend
kubectl get pods,services
minikube service frontend
```
The browser page should show “Backend: online”. The frontend Service is NodePort; backend stays internal as ClusterIP. The Flask app proxies `/api/status` to the in-cluster DNS name `backend`.

## Verify and collect screenshots
Open PowerShell in this folder and capture the actual running cluster output:
```powershell
kubectl get pods -o wide
kubectl get services
kubectl get deployments
kubectl port-forward service/frontend 8080:5000
```
In a second terminal, use `curl.exe http://127.0.0.1:8080/healthz` and `curl.exe http://127.0.0.1:8080/api/status`, and take screenshots showing the successful responses and the page. Save them under `evidence/` and replace the environment-check image in the report with real Minikube evidence before submission.

## GitHub link
GitHub repository: https://github.com/adityakittad1/Kubernetes_Aditya

## Cleanup
```powershell
kubectl delete -f .\k8s\frontend.yaml
kubectl delete -f .\k8s\backend.yaml
minikube stop
```


