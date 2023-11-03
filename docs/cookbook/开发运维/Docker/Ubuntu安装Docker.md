### Docker帮助命令

#### 安装Docker

[Docker官方安装文档](https://docs.docker.com/engine/install/ubuntu/)

##### 系统要求

##### 卸载旧版本

```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

##### 使用存储库安装

在新主机上首次安装 Docker Engine 之前，您需要设置 Docker 存储库。之后，您可以从存储库安装和更新 Docker。

##### 设置存储库

1. 更新`apt`包索引并安装包以允许`apt`通过 HTTPS 使用存储库：

   ```
   $ sudo apt-get update
   
   $ sudo apt-get install \
       ca-certificates \
       curl \
       gnupg \
       lsb-release
   ```

2. 添加 Docker 的官方 GPG 密钥：

   ```
   $ sudo mkdir -p /etc/apt/keyrings
   $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   ```

3. 使用以下命令设置存储库：

   ```
   $ echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

##### 安装 Docker 引擎

1. 更新`apt`包索引：

   ```
   $ sudo apt-get update
   ```

   > 运行时收到 GPG 错误`apt-get update`？
   >
   > 您的默认[umask](https://en.wikipedia.org/wiki/Umask)可能配置不正确，导致无法检测存储库公钥文件。在更新包索引之前尝试授予 Docker 公钥文件的读取权限：
   >
   > ```
   > $ sudo chmod a+r /etc/apt/keyrings/docker.gpg
   > $ sudo apt-get update
   > ```

2. 安装 Docker Engine、containerd 和 Docker Compose。

   - 最新的
   - 具体版本

   要安装最新版本，请运行：

   ```
    $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
   ```

   ------

3. `hello-world`通过运行镜像验证 Docker Engine 安装是否成功 ：

   ```
   $ sudo docker run hello-world
   ```

   此命令下载测试图像并在容器中运行它。当容器运行时，它会打印一条确认消息并退出。

您现在已经成功安装并启动了 Docker 引擎。用户组存在但不包含任何用户，这`docker`就是为什么您需要使用它`sudo` 来运行 Docker 命令。继续[Linux 后安装](https://docs.docker.com/engine/install/linux-postinstall/) ，以允许非特权用户运行 Docker 命令和其他可选配置步骤。

#### 查看Docker版本信息

```shell
# docker版本信息
docker version 
root@liuyanbo:/home/mysql# docker -v
Docker version 20.10.21, build baeda1f
```

```shell
root@liuyanbo:/home/mysql# docker -v
Docker version 20.10.21, build baeda1f
------------------------------------------
root@liuyanbo:/home/mysql# docker version
Client: Docker Engine - Community
 Version:           20.10.21
 API version:       1.41
 Go version:        go1.18.7
 Git commit:        baeda1f
 Built:             Tue Oct 25 18:01:58 2022
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.21
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.18.7
  Git commit:       3056208
  Built:            Tue Oct 25 17:59:49 2022
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.9
  GitCommit:        1c90a442489720eec95342e1789ee8a5e1b9536f
 runc:
  Version:          1.1.4
  GitCommit:        v1.1.4-0-g5fd4c4d
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

```

#### 查看Docker系统级别信息

```shell
# 系统级别的信息，包括镜像和容器的数量
docker info
```

```shell
root@liuyanbo:/home/mysql# docker info
Client:
 Context:    default
 Debug Mode: false
 Plugins:
  app: Docker App (Docker Inc., v0.9.1-beta3)
  buildx: Docker Buildx (Docker Inc., v0.9.1-docker)
  compose: Docker Compose (Docker Inc., v2.4.1)

Server:
 Containers: 2
  Running: 2
  Paused: 0
  Stopped: 0
 Images: 3
 Server Version: 20.10.21
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 io.containerd.runtime.v1.linux runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c90a442489720eec95342e1789ee8a5e1b9536f
 runc version: v1.1.4-0-g5fd4c4d
 init version: de40ad0
 Security Options:
  apparmor
  seccomp
   Profile: default
  cgroupns
 Kernel Version: 5.15.0-53-generic
 Operating System: Ubuntu 22.04.1 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 2
 Total Memory: 3.799GiB
 Name: liuyanbo
 ID: GJKU:GG6K:AN7I:VEAC:GPP6:C5QT:DNMC:6CEG:ZFP3:3OP2:YBHT:HQDK
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Registry: https://index.docker.io/v1/
 Labels:
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Registry Mirrors:
  https://60e2y77h.mirror.aliyuncs.com/
 Live Restore Enabled: false

```

#### 帮助命令

```shell
# 帮助命令
docker 命令 --help
```

***[Docker命令帮助文档](https://docs.docker.com/engine/reference/commandline/docker/)***

#### Docker启动与停止命令

```shell
# 启动docker服务：
systemctl start docker
# 停止docker服务：
systemctl stop docker
# 重启docker服务：
systemctl restart docker
# 查看docker服务状态：
systemctl status docker
# 设置开机启动docker服务：
systemctl enable docker
```

### 镜像命令

#### 查看本地主机上的镜像

```shell
# 查看所有本地主机上的镜像
docker images

root@liuyanbo:/home/mysql# docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
redis        latest    3358aea34e8c   3 days ago      117MB
nginx        latest    605c77e624dd   10 months ago   141MB
mysql        5.7       c20987f18b13   11 months ago   448MB

# 解释
REPOSITORY # 镜像仓库
TAG		   # 镜像标签
IMAGE ID   # 镜像ID
CREATED    # 镜像创建的时间
SIZE	   # 镜像的大小	

# 可选项
--all, -a         # 查看所有镜像
--quiet, -q        # 查看镜像ID

```

#### 从远程仓库查找镜像

```shell
docker search 镜像名称

root@liuyanbo:/home/mysql# docker search mysql
NAME                            DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
mysql                           MySQL is a widely used, open-source relation…   13489     [OK]       
mariadb                         MariaDB Server is a high performing open sou…   5145      [OK]       

# 可选项
--filter=STARS=3000 	# 查找STARS大于3000的

root@liuyanbo:/home/mysql# docker search mysql --filter=STARS=5000
NAME      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
mysql     MySQL is a widely used, open-source relation…   13489     [OK]       
mariadb   MariaDB Server is a high performing open sou…   5145      [OK]  

```

#### 下载镜像

```shell
docker pull 镜像名称[:tag]

root@liuyanbo:/home/mysql# docker pull ubuntu:20.04
20.04: Pulling from library/ubuntu		# 如果不指定tag,则默认就是latest
7b1a6ab2e44d: Pull complete 			# 分层下载，docker images的核心，联合文件系统
Digest: sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322		# 签名
Status: Downloaded newer image for ubuntu:20.04
docker.io/library/ubuntu:20.04		# 镜像的真实地址

```

#### 删除镜像

```shell
root@liuyanbo:/home/mysql# docker rmi -f IMAGE ID                        # 删除指定镜像
root@liuyanbo:/home/mysql# docker rmi -f IMAGE ID1 IMAGE ID2 IMAGE ID3   # 删除多个镜像
root@liuyanbo:/home/mysql#  docker rmi -f $(docker images -aq)           # 删除所有镜像
```

###  容器命令

#### 查看容器

```shell
docker ps
			# 列出当前正在运行的容器
-a			# 列出列出正在运行的容器包括历史容器
-n=?		# 显示最近创建的容器
-q			# 只显示当前容器的编号

root@liuyanbo:~# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS        PORTS                                                  NAMES
9b1917bd32ba   ubuntu:20.04   "bash"                   16 hours ago   Up 16 hours                                                          ubuntu20.04
d586d243603f   mysql:5.7      "docker-entrypoint.s…"   19 hours ago   Up 19 hours   33060/tcp, 0.0.0.0:3344->3306/tcp, :::3344->3306/tcp   mysql5.7
319c827a40c9   redis          "docker-entrypoint.s…"   46 hours ago   Up 24 hours   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp              redis


root@liuyanbo:~# docker ps -qa
9b1917bd32ba
d603ded6e961
e747f051261d
d586d243603f
319c827a40c9
```



**说明：容器来自于镜像**

#### 新建容器并启动

```shell
docker run [可选参数] image

# 参数说明
--name="设置的容器名称" 
-d      # 后台方式运行
-it 	# 交互式方式运行，进入容器查看状态
-p 		# 指定容器的端口  -p 书主机端口:容器端口
        # -p ip:主机端口：容器端口
        # -p 主机端口：容器端口（常用）
        # -p 容器端口
   
		# -p 随机指定端口

```

##### 交互式容器

> 以交互式方式创建并启动容器，启动完成后，直接进入当前容器。使用exit命令退出容器。需要注意的是以此种方式
> 启动容器，如果退出容器，则容器会进入停止状态。

```shell
#创建并启动名称为 mycentos7 的交互式容器；下面指令中的镜像名称 ubuntu:20.04 也可以使用镜像id
docker run -it --name=ubuntu ubuntu:20.04 /bin/bash
```

##### 守护式容器

> 创建一个守护式容器；如果对于一个需要长期运行的容器来说，我们可以创建一个守护式容器。命令如下（容器名称不能重复）

```shell
#创建并启动守护式容器
docker run -di --name=ubuntu ubuntu:20.04
#登录进入容器命令为：docker exec -it container_name (或者 container_id) /bin/bash（exit退出时，容器不会停止）
docker exec -it ubuntu /bin/bash
```

#### 退出容器

```shell
exit            # 直接退出容器并关闭
Ctrl + P + Q    # 容器不关闭退出
```

#### 启动和停止容器

```shell
docker start 容器id           # 启动容器
docker restart 容器id         # 重启容器
docker stop 容器id            # 停止当前正在运行的容器
docker kill 容器id            # 强制停止当前的容器
```

#### 删除容器

```shell
docker rm -f 容器id                       # 删除指定容器
docker rm -f $(docker ps -aq)       # 删除所有容器
docker ps -a -q|xargs docker rm -f  # 删除所有的容器
```

#### 设置容器开机自启动

```shell
docker ps -qa 
docker  update --restart=always 容器ID/容器名

docker  update --restart=always 56f0b18af626

```

#### 查看日志

```shell
docker logs -tf --tail number 容器ID
```

#### 查看容器中的进程信息

```shell
docker top 容器ID
```

#### 查看镜像的元数据

```shell
docker inspect 容器ID

root@liuyanbo:~# docker inspect d586d243603f
[
    {
        "Id": "d586d243603fdb446dfa5f6dfdd3ed785d85b87ab6e281aafe35872f37a89d59",
        "Created": "2022-11-19T10:18:42.02744616Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "mysqld"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 17398,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-11-19T10:18:42.345175206Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:c20987f18b130f9d144c9828df630417e2a9523148930dc3963e9d0dab302a76",
        "ResolvConfPath": "/var/lib/docker/containers/d586d243603fdb446dfa5f6dfdd3ed785d85b87ab6e281aafe35872f37a89d59/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/d586d243603fdb446dfa5f6dfdd3ed785d85b87ab6e281aafe35872f37a89d59/hostname",
        "HostsPath": "/var/lib/docker/containers/d586d243603fdb446dfa5f6dfdd3ed785d85b87ab6e281aafe35872f37a89d59/hosts",
        "LogPath": "/var/lib/docker/containers/d586d243603fdb446dfa5f6dfdd3ed785d85b87ab6e281aafe35872f37a89d59/d586d243603fdb446dfa5f6dfdd3ed785d85b87ab6e281aafe35872f37a89d59-json.log",
        "Name": "/mysql5.7",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": [
                "/home/mysql/conf:/etc/mysql/conf.d",
                "/home/mysql/data:/var/lib/mysql"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "3306/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "3344"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/4a071dd28aebec27e67dd5dff29b2dc03c14418f24b5d0a163e23a8518e8763b-init/diff:/var/lib/docker/overlay2/cbab91d22142dd13e845717ff19cd68ad0c199956e14a6751dfb05a202a1b01c/diff:/var/lib/docker/overlay2/8c63a5a61ae4a62ea33f9cbc25ba4e95714360b6055bc4c7330e67e74491714d/diff:/var/lib/docker/overlay2/d74ced919c9c40d96c02db59f0a268ef8fefa445623af79bd65f6b512e4e0f9c/diff:/var/lib/docker/overlay2/9f1615d18e7850ebea6d859e86d25853d0fee09e1807f308bfb2d88392087730/diff:/var/lib/docker/overlay2/1ff6db9c40f0fde0e25869e949dbef00cdb1a7f022baf3cdf2567c2aaa2715a3/diff:/var/lib/docker/overlay2/74f40eab985bca71437ab6e7fda39f77fc8cfa126fc781c53f74a555cb5383b4/diff:/var/lib/docker/overlay2/3030cee4db8bcfd3a5c99e6e3ae58ae3c165b14946d7bfde425f39e51aeadf3d/diff:/var/lib/docker/overlay2/7ad647497c2a3642d0be442101ca08d68eee664788a10c0b71fc10d67197e8e1/diff:/var/lib/docker/overlay2/c4f81185076887c8fbf597f3581355025f54106223888fead1285fbc23adc345/diff:/var/lib/docker/overlay2/80893daeadf2d5eac58fb99e27ffd538f7afcadfb5961de40b5dbc2cee3f8ece/diff:/var/lib/docker/overlay2/799bcca41703cb21add92fba82eafae0945f91b30d7fb6cecd54ef558f9da508/diff",
                "MergedDir": "/var/lib/docker/overlay2/4a071dd28aebec27e67dd5dff29b2dc03c14418f24b5d0a163e23a8518e8763b/merged",
                "UpperDir": "/var/lib/docker/overlay2/4a071dd28aebec27e67dd5dff29b2dc03c14418f24b5d0a163e23a8518e8763b/diff",
                "WorkDir": "/var/lib/docker/overlay2/4a071dd28aebec27e67dd5dff29b2dc03c14418f24b5d0a163e23a8518e8763b/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "bind",
                "Source": "/home/mysql/conf",
                "Destination": "/etc/mysql/conf.d",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            },
            {
                "Type": "bind",
                "Source": "/home/mysql/data",
                "Destination": "/var/lib/mysql",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "d586d243603f",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "3306/tcp": {},
                "33060/tcp": {}
            },
            "Tty": false,
            "OpenStdin": true,
            "StdinOnce": false,
            "Env": [
                "MYSQL_ROOT_PASSWORD=123456",
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "GOSU_VERSION=1.12",
                "MYSQL_MAJOR=5.7",
                "MYSQL_VERSION=5.7.36-1debian10"
            ],
            "Cmd": [
                "mysqld"
            ],
            "Image": "mysql:5.7",
            "Volumes": {
                "/var/lib/mysql": {}
            },
            "WorkingDir": "",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "941d14e9248e994cd4dc61cff5cea512a12205f2f206742a1ca28fad95de00c0",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "3306/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "3344"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "3344"
                    }
                ],
                "33060/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/941d14e9248e",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "d54f97786d2c451dbca46f3040a315e1c373d492d607a753f5b5d85a7d1ea834",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "15089f30dc5e0896bc887996921774b1819c2225348d04dab6edf746d166510d",
                    "EndpointID": "d54f97786d2c451dbca46f3040a315e1c373d492d607a753f5b5d85a7d1ea834",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]

```

#### 进入当前正在运行的容器

```shell
# 我们通常进入容器使用后台方式运行的，需要修改一些配置

# 命令

# 方式一
docker exec -it 容器ID /bin/bash

# 方式二
docker attach 容器ID


# docker exec       # 进入容器后开启一个新的终端，可以在里面操作
# docker attach     # 进入容器正在执行的终端，不会启动新的进程
```

#### 从容器中拷贝文件到主机 

```shell
# 将文件从容器拷贝到宿主机
docker cp 容器ID:容器内路径 目的地主机路径

# 将主机的文件拷贝到容器
docker cp 目的地主机路径 容器ID:容器内路径
```

#### 将容器打包成镜像

>Docker镜像都只是只读的，当容器启动时，一个新的可写层被加载到镜像的顶部
>
>这一层就是我们通常说的容器层，容器之下的都叫做镜像层

```shell
docker commit 提交容器成为一个新的版本
# 命令和git原理类似
docker commit -m="提交的描述信息" -a="作者" 容器ID 目标镜像名:[TAG]
```

### 容器数据卷

>容器之间可以有一个数据共享技术！ Docker容器中产生的数据，同步到本地！
>
>这就是卷技术，目录的挂载，将我们容器内的的目录挂载到Linux目录上面！
>
>***总结** 容器的持久化和同步操作！容器间数据也是可以共享的！

#### 目录挂载

> 方式一：直接使用命令来挂载 -v

##### 指定目录挂载

```shell
docker run -it -v 主机目录:容器目录

# 验证方式
# 一、直接同步文件
# 二、使用docker inspect 容器ID 
"Mounts": [
            {
                "Type": "bind",
                "Source": "/home/mysql/conf",
                "Destination": "/etc/mysql/conf.d",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            },
            {
                "Type": "bind",
                "Source": "/home/mysql/data",    # 主机目录
                "Destination": "/var/lib/mysql", # 容器目录
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],      
```

==**注意**== 容器停止也不影响同步



##### 匿名挂载

```shell
# 匿名挂载
-v 容器内路径
docker run -d -P --name niming_nginx -v /etc/nginx nginx     # -P 随机指定端口 (P大写)
 
# 查看所有volume的情况
[root@liuyanbo ~]# docker volume ls
DRIVER              VOLUME NAME
local               561b81a03506f31d45ada3f9fb7bd8d7c9b5e0f826c877221a17e45d4c80e096
local               36083fb6ca083005094cbd49572a0bffeec6daadfbc5ce772909bb00be760882
 
# 这里发现，这种情况就是匿名挂载，我们在-v 后面只写了容器内的路径，没有写容器外的路径！
 
```

##### 具名挂载

```shell
# 具名挂载
[root@liuyanbo ~]# docker run -d -P --name juming_nginx -v juming-nginx:/etc/nginx nginx
26da1ec7d4994c76e80134d24d82403a254a4e1d84ec65d5f286000105c3da17
# 查看所有的卷信息
docker volume ls 
[root@liuyanbo ~]# docker volume ls
DRIVER              VOLUME NAME
local               561b81a03506f31d45ada3f9fb7bd8d7c9b5e0f826c877221a17e45d4c80e096
local               36083fb6ca083005094cbd49572a0bffeec6daadfbc5ce772909bb00be760882
local               juming-nginx
 
# 通过-v 卷名：容器内的路径
# 查看一下这个卷
docker volume inspect 卷名

[root@liuyanbo ~]# docker volume inspect juming-nginx
[
  {
      "CreatedAt": "2020-08-12T18:15:21+08:00",
      "Driver": "local",
      "Labels": null,
      "Mountpoint": "/var/lib/docker/volumes/juming-nginx/_data", # 宿主机同步目录 
      "Name": "juming-nginx",
      "Options": null,
      "Scope": "local"
  }
]
```

> ==**所有docker容器内的卷，没有指定目录的情况下都是在`/var/lib/docker/volumes/xxxxx/_data`**==



> ==**我们通过具名挂载可以方便的找到我们的一个卷，大多数情况下使用的是`具名挂载`**==

```shell
# 如何确定是具名挂载还是匿名挂载，还是指定路径挂载！
-v  容器内路径                   # 匿名挂载
-v  卷名:容器内路径               # 具名挂载
-v /主机路径:容器内路径            # 指定路径挂载
```

##### 扩展

```shell
# 通过 -v 容器内容路径 ro rw 改变读写权限
ro  readonly    # 只读
rw  readwrite   # 可读可写
 
docker run -d -P --name juming-nginx -v juming-nginx:/etc/nginx:ro nginx
docker run -d -P --name juming-nginx -v juming-nginx:/etc/nginx:rw nginx
 
# ro 只要看到ro就说明这个路径只能通过宿主机来操作，容器内容无法操作
```

>方式二：使用Dockerfile 

##### Dockerfile初体验

> Dockerfile 是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明。



> 通过这个脚本可以生成镜像，镜像是一层一层的，脚本一个个的命令，每个命令都是一层！

```shell
# 创建一个Dockerfile文件， 名字可以随机
# 文件的内容 指定（大写） 参数
FROM ubuntu
 
VOLUME ["volume01", "volume02"]
 
CMD echo "----end----"

CMD /bin/bash
 
# 这里的每一个命令都是镜像的一层！
```

```shell
root@liuyanbo:~# docker build -f Dockerfile -t liuyanbo/ubuntu:1.0 .
Sending build context to Docker daemon   12.8kB
Error response from daemon: no build stage in current context
root@liuyanbo:/tmp# vim Dockerfile 
root@liuyanbo:/tmp# docker build -f Dockerfile -t liuyanbo/ubuntu:1.0 .
Sending build context to Docker daemon   12.8kB
Step 1/4 : FROM ubuntu
latest: Pulling from library/ubuntu
Digest: sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322
Status: Downloaded newer image for ubuntu:latest
 ---> ba6acccedd29
 # 匿名挂载
Step 2/4 : VOLUME ["volume01", "volume02"]
 ---> Running in 6c8d4447304b
Removing intermediate container 6c8d4447304b
 ---> d31fe796d8ee
Step 3/4 : CMD echo "----end----"
 ---> Running in 9b3ec117ec4b
Removing intermediate container 9b3ec117ec4b
 ---> 73a6aab2a922
Step 4/4 : CMD /bin/bash
 ---> Running in 0a9afd866668
Removing intermediate container 0a9afd866668
 ---> ae9afffa4bf1
Successfully built ae9afffa4bf1
Successfully tagged liuyanbo/ubuntu:1.0


root@liuyanbo:~# docker images
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
liuyanbo/ubuntu   1.0       ae9afffa4bf1   2 minutes ago   72.8MB
```

```shell
# 查看容器的元数据信息
docker inspect 容器ID

"Mounts": [
            {
                "Type": "volume",
                "Name": "916dd588f0c3046fe71cd4cd23355efa751bf1bcab6c9b12debe0d7b36b307d6",
                "Source": "/var/lib/docker/volumes/916dd588f0c3046fe71cd4cd23355efa751bf1bcab6c9b12debe0d7b36b307d6/_data",
                "Destination": "volume01",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            },
            {
                "Type": "volume",
                "Name": "6ba2664035f7e8db0019d3f695c9890b57b9b97f56f42a8bdea3513cac42fde3",
                "Source": "/var/lib/docker/volumes/6ba2664035f7e8db0019d3f695c9890b57b9b97f56f42a8bdea3513cac42fde3/_data",
                "Destination": "volume02",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],

```

**这种方式我们未来使用的十分多， 因为我们通常会构建自己的镜像！**

**假设构建镜像时候没有挂载卷，要手动镜像挂载 -v 卷名:容器内路径**

##### 数据卷容器

```shell
docker run -it --name docker01 --volumes-from docker01(数据卷容器) 镜像[TAG]


[root@liuyanbo ~]# docker run -d -p 3344:3306 -v /etc/mysql/conf.d -v /var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql01 mysql:5.7
 
[root@liuyanbo ~]# docker run -d -p 3344:3306 -v /etc/mysql/conf.d -v /var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql02 --volumes-from mysql01 mysql:5.7
```



==**结论**==

**容器之间配置信息的传递， 数据卷容器的声明周期一直持续到没有容器使用为止。但是一旦你持久化到了本地，这个时候，本地的数据是不会删除的！**

### Dockerfile

>Dockerfile是用来构建docker镜像的文件！

####     参数命令构建步骤

1. 编写一个Dockerfie文件
2. docker build 构建成为一个镜像
3. docker run 运行镜像
4. docker push 发布镜像（Docker Hub、阿里云镜像）



**看一下ubuntu官方是怎么制作镜像的**

![](http://img.mgd2008.com/static/img/1669004768271.png)

```shell
FROM scratch
ADD ubuntu-focal-oci-amd64-root.tar.gz /
CMD ["bash"]
```

#### Dockefile的构建过程

**基础知识：**

1. 每个保留关键字（指令）都是必须大写字母
2. 执行从上到下顺序执行
3. #表示注释
4. 每个指令都会创建提交一个新的镜像层，并提交！



![](http://img.mgd2008.com/static/img/126043b38ed9817b306c87c58e8b8a43_watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2ZhbmppYW5oYWk=,size_16,color_FFFFFF,t_70#pic_center.png)

**Docker 三剑客**

1. DockerFile： 构建文件， 定义了一切的步骤，源代码

2. DockerImages： 通过DockerFile构建生成的镜像， 最终发布和运行的产品！

3. Docker容器：容器就是镜像运行起来提供服务器


#### Dockerfile指令说明

![](http://img.mgd2008.com/static/img/20221121123957.png)

```shell
FROM            # 基础镜像，一切从这里开始构建
MAINTAINER      # 镜像是谁写的， 姓名+邮箱
RUN             # 镜像构建的时候需要运行的命令
ADD             # 步骤， tomcat镜像， 这个tomcat压缩包！添加内容
WORKDIR         # 镜像的工作目录
VOLUME          # 挂载的目录
EXPOSE          # 保留端口配置
CMD             # 指定这个容器启动的时候要运行的命令，只有最后一个会生效可被替代
ENTRYPOINT      # 指定这个容器启动的时候要运行的命令， 可以追加命令
ONBUILD         # 当构建一个被继承Dockerfile 这个时候就会运行 ONBUILD 的指令，触发指令
COPY            # 类似ADD, 将我们文件拷贝到镜像中
ENV             # 构建的时候设置环境变量！
```

#### 自定义一个tomcat容器

> Dockerfile文件如下

```shell
root@liuyanbo:/usr/local/diy_tomcat# vim Dockerfile 
FROM ubuntu
# 作者
MAINTAINER liuyanbo<1538527834@qq.com>

COPY readme.txt  /usr/local

ADD apache-tomcat-9.0.69.tar.gz /usr/local
ADD jdk-8u261-linux-x64.tar.gz /usr/local

ENV MYPATH /usr/local

WORKDIR $MYPATH

ENV JAVA_HOME $MYPATH/jdk1.8.0_261
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME $MYPATH/apache-tomcat-9.0.69
ENV CATALINA_BASH $MYPATH/apache-tomcat-9.0.69
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin

EXPOSE 8080

CMD $CATALINA_HOME/bin/startup.sh && tail -f $CATALINA_HOME/logs/catalina.out
```

#### 构建镜像

```shell
root@liuyanbo:/usr/local/diy_tomcat# docker build  -t diytomcat .
Sending build context to Docker daemon  525.2MB
Step 1/14 : FROM ubuntu
 ---> ba6acccedd29
Step 2/14 : MAINTAINER liuyanbo<1538527834@qq.com>
 ---> Using cache
 ---> cd886ac434fe
Step 3/14 : COPY readme.txt  /usr/local/diy_tomcat/
 ---> 950df6d8ab28
Step 4/14 : ADD apache-tomcat-9.0.69.zip /usr/local/
 ---> 2441861d2f1b
Step 5/14 : ADD jdk-8u261-linux-x64.tar.gz /usr/local
 ---> 5d2a5e94b1f0
Step 6/14 : ENV MYPATH /usr/local
 ---> Running in ad08d6eb4cd8
Removing intermediate container ad08d6eb4cd8
 ---> 7d7e6f75f190
Step 7/14 : WORKDIR $MYPATH
 ---> Running in 1ca5f08a5b79
Removing intermediate container 1ca5f08a5b79
 ---> 86b57b03c2c2
Step 8/14 : ENV JAVA_HOME /usr/local/jdk1.8.0_261
 ---> Running in 0e6a8b291c2a
Removing intermediate container 0e6a8b291c2a
 ---> 51a9bb5c9433
Step 9/14 : ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
 ---> Running in bbe8eee2f65c
Removing intermediate container bbe8eee2f65c
 ---> b8c1adac29d7
Step 10/14 : ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.69
 ---> Running in 4b016b1edf7f
Removing intermediate container 4b016b1edf7f
 ---> 6fb35f768a1a
Step 11/14 : ENV CATALINA_BASH /usr/local/apache-tomcat-9.0.69
 ---> Running in 368232992bea
Removing intermediate container 368232992bea
 ---> 81e774fc0e18
Step 12/14 : ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin
 ---> Running in 3131aa66fbb9
Removing intermediate container 3131aa66fbb9
 ---> 54b596118d60
Step 13/14 : EXPOSE 8080
 ---> Running in 3d6bac83af85
Removing intermediate container 3d6bac83af85
 ---> 9f006a8951fc
Step 14/14 : CMD /usr/local/apache-tomcat-9.0.69/bin/startup.sh && tail -f /usr/local/apache-tomcat-9.0.69/logs/catalina.out
 ---> Running in 5fb121ce8953
Removing intermediate container 5fb121ce8953
 ---> 8e3550e12335
Successfully built 8e3550e12335
Successfully tagged diytomcat:latest
```

#### 启动镜像

```shell
docker run -id --name diytomcat  -p 8080:8080 -v /usr/local/diy_tomcat/logs/:/usr/local/apache-tomcat-9.0.69/logs/ -v /usr/local/diy_tomcat/webapps/:/usr/local/apache-tomcat-9.0.69/webapps/ diytomcat
```

==**注意**==

1. 目录映射覆盖
2. tomcat端口映射后，主机访问不通

#### 发布自己的镜像

##### Docker Hub

##### 阿里云镜像仓库



### 总结

![](http://img.mgd2008.com/static/img/cc6561fc8b4de802b65b4140a5228335_watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2ZhbmppYW5oYWk=,size_16,color_FFFFFF,t_70#pic_center.png)

![](http://img.mgd2008.com/static/img/fa8a5f4aa8aa798c3d90abd9322f6da7_watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2ZhbmppYW5oYWk=,size_16,color_FFFFFF,t_70#pic_center.png)

### Docker网络