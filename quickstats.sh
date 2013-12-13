#!/bin/bash
#
#Get the server list from a provided username and password.  Then determine the load and bandwidth on the server.
#....well...this doesn't actually work.  
#It runs too fast and build the temp doc too slowly, I think, for the cats/greps to read the files.

listurl=" https://api.stormondemand.com/v1/Billing/Invoice/list"
loadurl="https://api.stormondemand.com/v1/Monitoring/Load/stats"
bandurl="https://api.stormondemand.com/v1/Monitoring/Bandwidth/stats"



username="$1"
password="$2"
environment="$3"

echo "Identifying server..."
curl -d '{"params":{"category":"Provisioned"}}' -u $username:$password $listurl -k > scriptreturn.temp
uniqid=$(cat scriptreturn.temp | grep -E -o '"uniq_id":.*?[^\\]”')
#if the uniqid is not empty, then we found a server.  Print that out.
cat scriptreturn.temp | grep -E -o '"description":.*?[^\\]"'

curl -d '{"params":{'${uniqid}'}}' -u $username:$password $loadurl -k > scriptreturn.temp
printf "Disk usage for "
cat scriptreturn.temp | grep -E -o '"domain":.*?[^\\]"'
echo
cat scriptreturn.temp | grep -E -o '"disk":.*?[^\\]}'


printf "Bandwidth usage for "
curl -d '{"params":{'${uniqid}'}}' -u $username:$password $bandurl -k > scriptreturn.temp
cat scriptreturn.temp | grep -E -o '"domain":.*?[^\\]"'
echo
cat scriptreturn.temp | grep -E -o '"year":.*?[^\\]}'
rm -f scriptreturn.temp
