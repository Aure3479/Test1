#bin/bash

YEARNOW=2024
i=0

rm -r "$YEARNOW"

mkdir "$YEARNOW"

for MOIS  in  {"01_janvier","02_fevrier","03_mars","04_avril","05_mai","06_juin","07_juillet","08_aout","09_septembre","10_octobre","11_novembre","12_decembre"}; do
    mkdir "$YEARNOW/$MOIS"

    i=$((i+1))


    d=1

    start_date="$YEARNOW-$i-01"
    end_date=$(date --date "$start_date + 1 month" +"%Y-%m-%d")
    while [[ "$start_date" != "$end_date" ]]; do
        


    

        DAY_OF_WEEK=$(date -d "$start_date" '+%A')
        echo "$start_date is a $DAY_OF_WEEK" > "$YEARNOW/$MOIS/$d.txt"
        start_date=$(date --date "$start_date + 1 day" +"%Y-%m-%d")
        d=$((d+1))
    done


done



