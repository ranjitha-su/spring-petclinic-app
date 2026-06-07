
## 🛡️ Security Scans

### 🔹 Secrets & Credentials
✅ **Gitleaks** – Scans the full git history and working tree for leaked API keys, tokens, and passwords  
✅ Outputs `gitleaks-report.json` — archived as a pipeline artifact  
✅ Configured with `.gitleaks.toml` for project-specific suppression rules  

### 🔹 Static Application Security Testing (SAST)
✅ **Semgrep** with the `p/java` ruleset – deep static analysis of Java source code  
✅ Catches SQL injection, XSS, insecure deserialization, path traversal  
✅ Outputs `semgrep-report.json` for downstream ingestion  

### 🔹 Software Composition Analysis (SCA)
✅ **OWASP Dependency Check** – audits all Maven/Gradle dependencies against the NIST NVD  
✅ Uses the NVD API for up-to-date CVE data  
✅ NVD database cached between pipeline runs to reduce scan time  

### 🔹 Container Image Scanning
✅ **Trivy** (Aqua Security) – scans built Docker image layers for OS and app-level CVEs  
✅ Targets **HIGH** and **CRITICAL** severity only  
✅ Fails the pipeline (`--exit-code 1`) if critical vulnerabilities are found  

---

## 🏗️ Pipeline Architecture

### 🔹 Test Stage — Shift Left Security
✅ **Gitleaks** – Secrets & credential leak detection  
✅ **Semgrep** – SAST for Java security anti-patterns  
✅ **OWASP Dependency Check** – CVE scan of third-party dependencies  
✅ **Report Upload** – Aggregate all scan artifacts centrally  

### 🔹 Build Stage — Secure Image Delivery
✅ **Docker Build** – BuildKit-powered image build with ECR layer caching  
✅ **AWS ECR Push** – Keyless push via OIDC ID token federation  
✅ **Trivy Scan** – Container vulnerability scan on the exact image that will be deployed  

### 🔹 Infrastructure & Cloud
✅ **GitLab CI** – Pipeline orchestration  
✅ **AWS ECR** – Private container registry  
✅ **OIDC / ID Token Federation** – No static AWS credentials stored anywhere  
✅ **Kubernetes** – Deployment target (`k8s/` manifests included)  

---

## 🔐 Security Architecture Highlights

**No long-lived AWS credentials.** GitLab's native OIDC ID token support authenticates to AWS via a federated IAM role — eliminating the risk of credential leakage entirely.

**Fail fast, fail early.** Gitleaks and Semgrep run in the `test` stage before any build artifact is produced. A secrets leak or critical SAST finding stops the pipeline immediately.

**Defence in depth.** Four independent scanning tools cover different vulnerability classes — no single scanner is relied upon for full coverage.
