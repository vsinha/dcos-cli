#!/bin/bash

# This script expects the following env var:
#   CCM_AUTH_TOKEN
#   CLUSTER_ID

set -e
set -o pipefail
set -x

# wait for cluster to come up
while true; do
    STATUS=$(http --ignore-stdin \
                  https://ccm.mesosphere.com/api/cluster/${CLUSTER_ID}/ \
                  Authorization:"Token ${CCM_AUTH_TOKEN}" | \
                    jq ".status");
    if [ $STATUS -eq 0 ]; then
        break;
    fi;
    sleep 10;
done;

# get dcos_url
CLUSTER_INFO=$(http GET https://ccm.mesosphere.com/api/cluster/${CLUSTER_ID}/ Authorization:"Token ${CCM_AUTH_TOKEN}" | jq ".cluster_info")
eval CLUSTER_INFO=$CLUSTER_INFO  # unescape json

DCOS_URL=$(echo "$CLUSTER_INFO" | jq ".MastersIpAddresses[0]")
DCOS_URL=${DCOS_URL:1:-1} # remove JSON string quotes
echo $DCOS_URL
