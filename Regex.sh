#!/usr/bin/env bash
echo "Here is a list of data types you can get from your messy API responses:"
sleep 2
echo "Restaurant names"
sleep 1
echo "Cuisines"
sleep 1
echo "Ingredient lists"
sleep 1
echo "RGB colors"
sleep 1
echo "Social media usernames"
sleep 1
echo "Product codes"
sleep 1
echo "News headlines"
sleep 1
echo "Event dates/times"
sleep 1
echo "Email addresses"
sleep 2
read -p "Enter one of the options above: " -r OPTION
while true
do
	case "$OPTION" in
		"Restaurant names")
			python3 "regexpackage/Restaurant_Regex.py" "$1"
			;;
		"Cuisines")
			python3 "regexpackage/Cuisine_Regex.py" "$1"
			;;
		"Ingredient lists")
			python3 "regexpackage/Ingredients_Regex.py" "$1"
			;;
		"RGB colors")
			python3 "regexpackage/RGBA_Regex.py" "$1"
			;;
		"Social media usernames")
			python3 "regexpackage/Username_Regex.py" "$1"
			;;
		"Product codes")
			python3 "regexpackage/Product_code_Regex.py" "$1"
			;;
		"News headlines")
			python3 "regexpackage/News_headline_Regex.py" "$1"
			;;
		"Event dates/times")
			python3 "regexpackage/Event_date_time_Regex.py" "$1"
			;;
		"Email addresses")
			python3 "regexpackage/Email_address_Regex.py" "$1"
			;;
		*)
			echo "Incorrect option!!!"
			read -p "Enter one of the options above: " -r OPTION
			continue
			;;
	esac
	read -p "Do you want to exit? Enter 0 for No and 1 for yes: " -r CHOICE
	if [ "$CHOICE" -eq 0 ]
	then
		read -p "Enter one of the options above: " -r OPTION
	elif [ "$CHOICE" -eq 1 ]
	then
		echo "exiting app..."
		sleep 2
		exit
	else
		echo "exiting app..."
		sleep 2
		exit
	fi
done
