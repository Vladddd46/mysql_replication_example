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


Ensure /etc/my.cnf have enough permissions on both master,slave hosts.<br>
</p>