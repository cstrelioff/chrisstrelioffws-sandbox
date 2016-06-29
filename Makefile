all:
	tinker --build

deploy:
	rsync -av --delete --rsh=ssh blog/html/ chrisstrelioff.ws:sandbox
	ssh -t chrisstrelioff.ws "sudo rm -r /var/www/chrisstrelioff.ws/html/sandbox/*;sudo cp -r sandbox/* /var/www/chrisstrelioff.ws/html/sandbox/"
