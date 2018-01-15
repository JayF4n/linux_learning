#!/bin/bash

Cap_used=$(df -h / | sed '1d' | awk '{printf("%.2f",$3/$2)}') 

Mem_used=$(free | sed -n '2p' | awk '{printf("%.2f",$3/$2)}') 

Load_min=$(uptime | sed 's/,//g' |  awk '{printf("%.2f",$10/4)}')

echo $Cap_used 0.85 | awk '{\
    if($1<$2) {\
        print("Disk-Root:          is OK,use:",$1*100"%")}\
    else {\
        print("Disk-Root:          need notice,use:",$1*100"%")}\
    }'

echo $Mem_used 0.90 | awk '{\
    if($1<$2) {\
        print("Memory:             is OK,use:",$1*100"%")}\
    else {\
        print("Memory:             need notice,use:",$1*100"%")}\
    }'

echo $Load_min 0.70 | awk '{\
    if($1<$2) {\
        print("Loadaverage:        is OK,use:",$1)}\
    else {\
        print("Loadaverage:        need notice,use:",$1)}\
    }'

