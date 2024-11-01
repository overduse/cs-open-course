#!/bin/sh
echo "#!/bin/sh\ncurl --head --silent https://missing.csail.mit.edu" > /tmp/missing/semester

cat /tmp/missing/semester
