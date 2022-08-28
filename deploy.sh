#echo "==========BUILDING THE PRODUCTION FILES ================"
#ng build
echo "============BUILDING THE IMAGE    ================"
sudo ./buildImg.sh
echo "==========RUNNING THE CONATINER ================"
sudo ./createCont.sh
echo "========== DONE ================"
