#!/bin/bash

# Assign your variables
x=0
y=0
z=0

#basic range in for loop
for x in {1..5}
do
    for y in {1..2}
    do
        # Multiply x and y and assing to z
        z=$(( $x * $y ))

        # Print variable x, y, and z
        echo "x = $x; y = $y; x * y = $z"

        # Print blank line
        echo " "
    done
done

# Print that the script is done
echo "Done!!"
