#! /bin/bash
#
#$Author: ee364g13 $
#$Date: 2016-02-03 13:06:44 -0500 (Wed, 03 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Lab02/hangman.bash $
#$Revision: 87638 $
#$Id: hangman.bash 87638 2016-02-03 18:06:44Z ee364g13 $

word=(banana parsimonious sesquipedalian)
(( rand_num=$RANDOM % 3 ))

(( word_len=$(echo ${word[rand_num]} | wc -c)-1 ))
echo "Your word is $word_len letters long."

user_array=""
for (( i = 0; i < $word_len; i++ )); do
    comp_array=$comp_array${word[rand_num]:$i:1}
    user_array=$user_array'.'
    comp_array=$comp_array' '
    user_array=$user_array' '
done
comp_array=($comp_array)
user_array=($user_array)

echo "Word is: ${user_array[*]}"

let won_switch=0
let skip_compare_flag=0
let good_flag=0
guessed_array=""

while (( won_switch == 0 )); do
    read -p "  Make a guess: " guess

    for (( i = 0; i < ${#guessed_array[*]}; i++ )); do
	if [[ "$guess" == "${guessed_array[i]}" ]]; then
	    skip_compare_flag=1
	fi
    done

    if (( skip_compare_flag == 0 )); then
	for (( i = 0; i < $word_len; i=i+1 )); do
	    if [[ "$guess" == "${comp_array[i]}" ]]; then
		user_array[i]=$guess
		good_flag=1
	    fi
	done
	(( good_flag==1 )) && guessed_array=(${guessed_array[*]} $guess)
    fi

    if (( good_flag == 1 )); then
	echo "  Good going!"
    else
	echo "  Sorry, try again."
    fi

    echo

    if [[ ${comp_array[*]} == ${user_array[*]} ]]; then
	won_switch=1
    else
	echo "Word is: ${user_array[*]}"
    fi
    skip_compare_flag=0
    good_flag=0

done

echo "Congratulations! You guessed the word: ${word[rand_num]}"

exit 0
