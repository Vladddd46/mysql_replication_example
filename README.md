<h1>Step-by-step guide how to set up MySql replication</h1>
<p>In this repo I show how to set up master-slave replication in MySql.<br>
I run 2 MySql servers: first in MacOs, the second in docker container </p>
<br>
<p>
Run slave in docker container: <br>
docker run -it --name=<name_of_docker_container> -e MYSQL_ROOT_PASSWORD=<mysql_password> -p 6603:3306 mysql/mysql-server  <br>
docker exec -it <name_of_docker_container> bash  <br>

Edit /etc/my.cnf file in docker container: <br>
[mysqld]<br>
server-id=2 # define server id <br>
enforce-gtid-consistency = 1 # enabling gtid function <br>
gtid-mode = ON # enabling gtid function <br>

Edit  /etc/my.cnf file in (master)MacOs host: <br>
[mysqld]<br>
server-id = 1<br>
log_bin = /var/log/mysql/mysql-bin.log # path to folder with logs<br>
binlog_format = ROW<br>
enforce-gtid-consistency = 1<br>
gtid-mode = ON<br>


Ensure /etc/my.cnf have enough permissions on both master, slave hosts.<br>
Also after editing /etc/my.cnf files restart mysql servers on both hosts (MacOs and docker)<br>

Login in mysql server on master host(MacOs):<br>
mysql -u [user] -p [password]<br>
Create user for slave replication:<br>
CREATE USER 'slave'@'%' IDENTIFIED BY 'create_slave_password';<br>
GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%';<br>
FLUSH PRIVILEGES;<br>


</p>