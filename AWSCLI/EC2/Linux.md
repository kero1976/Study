EC2のAmazon Linuxの操作について

# 1. OS

## 1-1.ユーザーの追加

### 1-1-1.ユーザの作成
sudo useradd -m hoge

### 1-1-2.認証用に.sshをコピー
自分(ec2-user)のhomeディレクトリで、
sudo cp -r .ssh /home/hoge/
sudo chown -R hoge:hoge /home/hoge/.ssh/

### 1-1-3.sudo権限の追加
sudo visudo
コマンドを実行し、root行の下に追加する。
root    ALL=(ALL)       ALL
hoge ALL=(ALL)       NOPASSWD:ALL
書いたら、ctrl+Sで保存して、ctrl+Xで抜ける

# 2.ミドルウェア

## 2-1.CTFdの環境構築

### 2-1-1.入手
wget https://github.com/CTFd/CTFd/archive/refs/tags/3.6.0.zip

### 2-1-2.展開
unzip 3.6.0.zip
cd CTFd-3.6.0/

## 2-2.Dockerのインストール
Amazon Linux2023だと以下
sudo dnf update
sudo dnf install  docker

## 2-3.docker-compose
https://densan-hoshigumi.com/aws/amzn2023-docker-install

sudo systemctl enable --now docker
sudo usermod -aG docker hoge

$ DOCKER_CONFIG=${DOCKER_CONFIG:-/usr/local/lib/docker}
$ sudo mkdir -p $DOCKER_CONFIG/cli-plugins
$ sudo curl -SL https://github.com/docker/compose/releases/download/v2.17.0/docker-compose-linux-aarch64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
$ sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

aarch64はx86_64など必用に応じて変更する
