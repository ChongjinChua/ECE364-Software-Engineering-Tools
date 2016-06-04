#! /bin/bash
A[27]="x"
A[6]="y"
A[86]="z"

for I in ${A[*]}; do
    echo "$I"
done

exit 0
