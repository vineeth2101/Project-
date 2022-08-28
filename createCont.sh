#sudo docker rm -f angcontain
sudo docker rm -f $(sudo docker ps -a -q)
if [ $? -ne 0 ] ; then
        echo "ERROR: Docker delteing buildmmm"
#        exit 1
fi

sudo docker run -d -it --name angcontain -p 9092:80 angularv1:av1
if [ $? -ne 0 ] ; then
        echo "ERROR: Docker build failed"
        exit 1
fi
echo "====CONTAINER IS RUNNING AT PORT = 9092"
