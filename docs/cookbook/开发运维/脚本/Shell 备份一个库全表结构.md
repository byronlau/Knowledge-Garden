```shell
#!/bin/bash
# 设置mysql的登录用户名和密码
source /etc/profile
mysql_user="数据库用户名"
mysql_password="数据库密码"
mysql_host="数据库主机地址"
mysql_port="数据库端口号"
mysql_charset="utf8"
mysql_database="数据库名称"
# 是否删除过期数据
expire_backup_delete="OFF"
expire_days=30
backup_date=`date +%Y%m%d`
backup_time=`date +%Y%m%d%H%M`
# 备份文件存放地址(根据实际情况填写)
backup_location=/data/mysql-backup/structure/
backup_dir=$backup_location$mysql_database-$backup_date.sql
welcome_msg="Welcome to use MySQL backup tools!"
# 判断mysql实例是否正常运行
mysql_ps=`ps -ef |grep mysql |wc -l`
mysql_listen=`netstat -an |grep LISTEN |grep $mysql_port|wc -l`
if [ [$mysql_ps == 0] -o [$mysql_listen == 0] ]; then
	echo "ERROR:MySQL is not running! backup stop!"
	exit
else
	echo $welcome_msg
fi

# 如果目录不存在则创建
if [ ! -d "$backup_location" ];then
    echo "$backup_location not exist, start create"
    mkdir -p $backup_locaton
    echo "$backup_location created complet"
else
    echo "$backup_location is exist"
fi    
# 备份指定数据库中数据

mysqldump -h$mysql_host -P$mysql_port -u$mysql_user -p$mysql_password -d $mysql_database > $backup_dir
flag=`echo $?`
if [ $flag == "0" ];then
    echo "$backup_time database $mysql_database success backup to $backup_dir successful"
else
    echo "$backup_time database $mysql_database backup fail!"
fi

# 删除过期数据
if [ "$expire_backup_delete" == "ON" -a  "$backup_location" != "" ];then
	`find $backup_location/ -type f -mtime +$expire_days | xargs rm -rf`
	echo "Expired backup data delete complete!"
fi

```

