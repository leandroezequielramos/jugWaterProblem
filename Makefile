CLI_IMAGE=water_jug_solver
TEST_IMAGE=wfs_test
API_IMAGE=wjs_api

all: build_api build_cli build_test

build_cli:
	docker build -t ${CLI_IMAGE} -f docker/Dockerfile_cli .

build_api:
	docker build -t ${API_IMAGE} -f docker/Dockerfile_api .

run_api:
	docker run --rm -p 8000:8000 ${API_IMAGE}

run_cli:
	docker run --rm -it water_jug_solver

build_test:
	docker build -t ${TEST_IMAGE} -f docker/Dockerfile_test .

run_test:
	docker run --rm -v $(PWD)/src/wjp_lib:/src -v $(PWD)/test/cli:/test -e PYTHONPATH=/src $TEST_IMAGE py.test  /test

clean:
	docker rmi ${CLI_IMAGE}
	docker rmi ${TEST_IMAGE}
	docker rmi ${API_IMAGE}