%global __os_install_post %{nil}
Name: ForTest
Summary: ChinaCache ForTest
Version: 0.1
Release: R
Vendor: IRD
License: TBD
Group: Enterprise/ChinaCache
BuildRoot: %{_topdir}/BUILDROOT
Prefix: /usr/local/%{name}

Source0: %{name}-%{version}.tar.gz
Patch0: patch-src-ngx_http_lua_headers.c.diff

AutoReqProv: no

%description
ChinaCache ForTest

%prep

%setup -q

%patch0 -p1 -d ../LUA

%build

# Build LuaJIT
cd ../LuaJIT
sed -i "s@export PREFIX= /usr/local\$@export PREFIX= %{prefix}/LuaJIT/@" Makefile
make PREFIX=/usr/ || exit -1
cd -

export LUAJIT_LIB=%{prefix}/LuaJIT/lib && export LUAJIT_INC=%{prefix}/LuaJIT/include/luajit-2.1
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} \
        --add-module=../NDK \
        --add-module=../LUA \
        --with-ld-opt="-Wl,-rpath,%{prefix}/LuaJIT/lib"

make %{?_smp_mflags}

%install
cd ../LuaJIT && make install PREFIX=%{buildroot}%{prefix}/LuaJIT
cd -
mkdir -vp %{buildroot}%{prefix}/{sbin,logs,html,conf}
cp -af objs/nginx %{buildroot}%{prefix}/sbin/
cp -af chinacache/nginx.conf %{buildroot}%{prefix}/conf/nginx.conf

%clean

%pre

%post

%preun

%files
%defattr  (-,root,root,0755)
%{prefix}/sbin
%{prefix}/conf
%{prefix}/html
%{prefix}/logs
%{prefix}/LuaJIT

%changelog

