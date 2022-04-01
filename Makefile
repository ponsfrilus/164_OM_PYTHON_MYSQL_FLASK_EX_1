up:
	docker-compose up --build --remove-orphans

logs:
	docker-compose logs -f

down:
	docker-compose down

rm:
	docker-compose rm 164_database 164_phpmyadmin 164_adminer
