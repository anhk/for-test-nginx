#!/bin/bash

version=0.0.1
name='NGX-Lua'

if [ $# -ge 1 ]; then
    version=$1
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
LUAJIT_DIR=LuaJIT-2.1.0-beta2
NDK_DIR=ngx_devel_kit-0.3.0
LUA_DIR=lua-nginx-module-0.10.8

SOURCES=${BUILD_DIR}/SOURCES/

rm -fr ${BUILD_DIR}

echo "%_topdir ${BUILD_DIR}" > ~/.rpmmacros
mkdir -vp ${BUILD_DIR}/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
cp -af $NGINX_DIR $SOURCES/$name-$version
cp -af $LUAJIT_DIR $SOURCES/LuaJIT
cp -af $NDK_DIR $SOURCES/NDK
cp -af $LUA_DIR $SOURCES/LUA
mkdir -vp $SOURCES/$name-$version/chinacache
find nginx-lua-config/ \( -name *.diff -o -name *.patch \) -exec cp {} $SOURCES/ \;
cp -af nginx-lua-config/fortest.spec $SOURCES/fortest.spec
cp -af nginx-lua-config/nginx.conf $SOURCES/$name-$version/chinacache

sed -i "s@^Name:.*@Name: $name@" $SOURCES/fortest.spec
sed -i "s@^Version:.*@Version: $version@" $SOURCES/fortest.spec

cd $SOURCES && tar zcfp $name-${version}.tar.gz $(ls)

QA_SKIP_BUILD_ROOT=1 rpmbuild -bb fortest.spec && mv $BUILD_DIR/RPMS/x86_64/*.rpm $CUR_DIR

