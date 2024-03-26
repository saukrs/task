all:
	@echo See GNUmakefile for other targets.

clean:
	@\
	 set -x  &&\
	 docker compose down --remove-orphans -v

up:
	@\
	 set -x  &&\
	 docker compose up -d

ps:
	@WIDTH=$$(stty size | cut -d " " -f 2)  ;\
	 set -x  &&\
	 docker compose ps -a | cut -c -$${WIDTH}

cycle:  clean up

index:
	@\
	 set -x  &&\
	 docker compose exec logstash curl --user elastic:changeme -k -X PUT "https://es01:9200/arturas?pretty"

status:
	@\
	 set -x  &&\
	 docker compose exec logstash curl --user elastic:changeme -k -X GET "https://es01:9200/"  &&\
	 docker compose exec logstash curl --user elastic:changeme -k -X GET "https://es01:9200/_cluster/health?pretty"  &&\
	 docker compose exec logstash curl --user elastic:changeme -k -X GET "https://es01:9200/_search?pretty"  &&\
	 docker compose exec logstash curl --user elastic:changeme -k -X GET "https://es01:9200/_cat/indices?v"  &&\
	 docker compose exec logstash curl --user elastic:changeme -k -X GET "https://es01:9200/_cat/shards?v"

explain:
	@\
	 set -x  &&\
	 docker compose exec logstash curl --user elastic:changeme -k -X GET "https://es01:9200/_cluster/allocation/explain?pretty"
