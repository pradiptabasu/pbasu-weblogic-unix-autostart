nmConnect('weblogic','welcome1','ip-172-31-122-88.ec2.internal','5556','fmw_12212_domain','/home/ec2-user/Oracle/Middleware12212/Oracle_Home/user_projects/domains/fmw_12212_domain','plain');
nmStart('AdminServer');
nmServerStatus('AdminServer');
nmDisconnect()