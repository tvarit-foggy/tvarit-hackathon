while true 
do
timestamp=$(date +"%Y-%m-%d-%T")
machineId=$((RANDOM%10))
temperature=$((RANDOM%100))
voltage=$((RANDOM%1000))
current=$((RANDOM%100))
speed=$((RANDOM%1000))
pressure=$((RANDOM%1000))
humidity=$((RANDOM%100))
echo "$machineId,$temperature,$voltage,$current,$speed,$pressure,$humidity"


aws kinesis put-record --stream-name shu_stream --data "$timestamp,$machineId,$temperature,$voltage,$current,$speed,$pressure,$humidity"$'\n' --partition-key $machineId --region eu-west-1

sleep 1
done


##don't forget to give AWS kinesis permission to the IAM user.
