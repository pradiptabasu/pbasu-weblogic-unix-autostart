nmConnect('weblogic','welcome1','ip-172-31-127-93.ec2.internal','5556','osm73514_domain','/home/ec2-user/Oracle/Middleware/Oracle_Home/user_projects/domains/osm73514_domain','plain');
nmKill('AdminServer');
nmServerStatus('AdminServer');
nmDisconnect()