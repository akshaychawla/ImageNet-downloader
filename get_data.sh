echo "Downloading Fall 2011 Urls"
wget -c --no-check-certificate http://image-net.org/imagenet_data/urls/imagenet_fall11_urls.tgz
echo "Inflating.."
tar xzvf imagenet_fall11_urls.tgz 

echo "Done.. Please proceed with browsing classes using 'browse_class.py' and downloading data with 'download_images.py'"

