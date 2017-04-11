#!/bin/bash

version=0.0.1
name='fortest'

if [ $# -ge 1 ]; then
    name=$1
fi

if [ $# -ge 2 ]; then
    version=$2
fi


echo -e "\nCommand: \n\t\033[0;34m$0 <version>\033[0m\t\tdefault version is 0.0.1"

echo -ne "\nBuild \033[0;32m$name-$version\033[0m (y/N) "
read answer

if [ "$answer" != "y" ]; then
    exit -1;
fi

CUR_DIR=$(pwd)
BUILD_DIR=${CUR_DIR}/rpmbuild

NGINX_DIR=nginx-1.11.13

SOURCES=${BUILD_DIR}/SOURCES/

rm -fr ${BUILD_DIR}

echo "%_topdir ${BUILD_DIR}" > ~/.rpmmacros
mkdir -vp ${BUILD_DIR}/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp -af $NGINX_DIR $SOURCES/$name-$version
cp -af fortest.spec $SOURCES/fortest.spec

sed -i "s@^Name:.*@Name: $name@" $SOURCES/fortest.spec
sed -i "s@^Version:.*@Version: $version@" $SOURCES/fortest.spec

cd $SOURCES && tar zcfp $name-${version}.tar.gz $name-$version

rpmbuild -bb fortest.spec && mv $BUILD_DIR/RPMS/x86_64/*.rpm $CUR_DIR

