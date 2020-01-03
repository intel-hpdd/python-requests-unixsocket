BUILDROOT:=$(shell [ -d "/build" ] && echo "/build" || echo ".")
TMPDIR:=$(shell mktemp -d)

srpm:
	python2 --version || yum -y install python2-setuptools
	yum install -y spectool yum-utils
	mkdir -p ${TMPDIR}/_topdir/{SOURCES,SPECS}
	rm -rf ${BUILDROOT}/_topdir
	cp -r python-requests-unixsocket.spec ${TMPDIR}/_topdir/SPECS

	yum-builddep -y ${TMPDIR}/_topdir/SPECS/python-requests-unixsocket.spec --disablerepo=epel-source
	spectool -g -R ${TMPDIR}/_topdir/SPECS/python-requests-unixsocket.spec -C ${TMPDIR}/_topdir/SOURCES
	rpmbuild -bs -D "_topdir ${TMPDIR}/_topdir" ${TMPDIR}/_topdir/SPECS/python-requests-unixsocket.spec
	cp -r ${TMPDIR}/_topdir/SRPMS/* $(outdir)
	cp -rf ${TMPDIR}/_topdir ${BUILDROOT}/_topdir
	rm -rf ${TMPDIR}