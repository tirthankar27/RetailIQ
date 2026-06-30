FROM jenkins/jenkins:lts

USER root

# Base packages
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    python3 \
    python3-pip \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release

# ---------------- Docker CLI ----------------
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | \
gpg --dearmor -o /usr/share/keyrings/docker.gpg

RUN echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] https://download.docker.com/linux/debian \
$(. /etc/os-release && echo $VERSION_CODENAME) stable" \
> /etc/apt/sources.list.d/docker.list

# ---------------- Hashicorp ----------------
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor -o /usr/share/keyrings/hashicorp.gpg

RUN echo \
"deb [signed-by=/usr/share/keyrings/hashicorp.gpg] https://apt.releases.hashicorp.com \
$(lsb_release -cs) main" \
> /etc/apt/sources.list.d/hashicorp.list

# ---------------- Kubernetes ----------------
RUN curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.34/deb/Release.key | \
gpg --dearmor -o /usr/share/keyrings/kubernetes.gpg

RUN echo \
'deb [signed-by=/usr/share/keyrings/kubernetes.gpg] https://pkgs.k8s.io/core:/stable:/v1.34/deb/ /' \
> /etc/apt/sources.list.d/kubernetes.list

RUN apt-get update && apt-get install -y \
    docker-ce-cli \
    terraform \
    kubectl \
    ansible

USER jenkins