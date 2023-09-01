#! /bin/bash
docker build -t wfs_test -f docker/Dockerfile_test .
docker run --rm -v $(pwd)/src/wjp_lib:/src -v $(pwd)/test/cli:/test -e PYTHONPATH=/src wfs_test py.test  /test