#!/bin/bash

smoke_info=$1
echo smoke_info

present_date=$(date +"%m-%d-%y")
echo $present_date

present_time=$(date +"%T")
echo $present_time

smoke_detect_mail () {
message2=$(cat <<EOF
{
   "Subject": {
       "Data": "from smoke detecting system",
       "Charset": "UTF-8"
   },
   "Body": {
       "Text": {
           "Data": "smoke detected Date is $1, Time is $2",
           "Charset": "UTF-8"
       }
   }
}
EOF
)

echo "$message2" > smoke_info.json

aws ses send-email --from "saurabh.rao2000@gmail.com" --destination "ToAddresses=saurabh.rao2000@gmail.com" --region ap-south-1 --profile default --message file://smoke_info.json

}

if [ True ]
then
    echo "Smoke is detected"
    smoke_detect_mail $present_date $present_time
else
    echo "unkown error.. check it"
fi
