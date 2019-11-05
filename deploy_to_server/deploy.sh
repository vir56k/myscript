#!/bin/bash

# 在本机开发，通过 修改hosts文件映射 到 my_rel.com
TheHost=my_rel.com

#CurrentDir=`pwd`
#echo "CurrentDir=${CurrentDir}"
workdir=$(cd $(dirname $0); cd ..; pwd)
echo "workdir=${workdir}"

cd ${workdir}

# 打包
./mvnw clean package -Dmaven.test.skip=true

file="${workdir}/target/managerservice-0.0.1-SNAPSHOT.jar"
# -f 参数判断 $file 是否存在
if [ ! -f "$file" ]; then
  echo "$file is not exist !!!!!"
else
  echo "$file is exist !"
fi

# 发送到远程机器
scp ${file} root@${TheHost}:/root/yunfei

# 发布到远程
ssh root@${TheHost} >/dev/null 2>&1 <<eeooff

echo "welcome !!"

#JAR_NAME=managerservice-0.0.1-SNAPSHOT.jar

cd /root/yunfei
nohup java -jar managerservice-0.0.1-SNAPSHOT.jar --spring.profiles.active=product  > log.file  2>&1 &

exit

eeooff

echo 部署到虚拟机的路径是: /root/yunfei  ,可查看日志 cat /root/yunfei/log.file
echo 查询是否在运行: ps -ef | grep java
echo done!
