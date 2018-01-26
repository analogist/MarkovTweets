#!/bin/bash

queuefile="/home/kjvbot/kjvblockchain/tweet_queue"
postfile="/home/kjvbot/kjvblockchain/post_tweet"
if [ -s $queuefile ]; then
	# Obtain tweet from first line of tweet_queue
	tweetdata=$(head -n 1 $queuefile)

	# Retry tweet every 60 seconds until network succeeds
	until twurl -d "status=${tweetdata}" /1.1/statuses/update.json; do
		echo "Retrying tweet..."
		sleep 30
	done

	# Finished; rotate tweet queue over
	head -n 1 $queuefile >> $postfile
	sed -i "1d" $queuefile
else
	echo "Error: empty queue!"
fi
