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
Patch0: nginx-tfs.patch

AutoReqProv: no

%description
ChinaCache ForTest

%prep

%setup -q
%patch0 -p1 -d ../nginx-tfs/

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}  \
        --add-module=../nginx-tfs

make %{?_smp_mflags}

%install
mkdir -vp %{buildroot}/%{prefix}/{sbin,logs,html,conf}
mkdir -vp %{buildroot}/usr/lib64/
cp -af objs/nginx %{buildroot}/%{prefix}/sbin/
cp -af chinacache/nginx.conf %{buildroot}/%{prefix}/conf/nginx.conf
cp -af chinacache/libyajl.* %{buildroot}/usr/lib64/

%clean

%pre

%post
mkdir -vp /data/proclog/log/hpc/flexi_rcpt_mansubi/

%preun

%files
%defattr  (-,root,root,0755)
%{prefix}/sbin
%{prefix}/conf
%{prefix}/html
%{prefix}/logs
/usr/lib64/

%changelog

