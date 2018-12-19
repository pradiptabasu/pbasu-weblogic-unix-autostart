#!/bin/sh
#
export DOMAIN_HOME="/home/ec2-user/Oracle/Middleware12212/Oracle_Home/user_projects/domains/fmw_12212_domain"
export MW_HOME="/home/ec2-user/Oracle/Middleware12212/Oracle_Home"
export PYTHON_SCRIPT_DIR="/home/ec2-user/scripts"

/bin/sh $MW_HOME/wlserver/server/bin/setWLSEnv.sh
/bin/sh $MW_HOME/wlserver/common/bin/wlst.sh $PYTHON_SCRIPT_DIR/fmw_12212_domain_stopWeblogic_osb_server1.py