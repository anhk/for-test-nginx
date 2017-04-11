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

AutoReqProv: no

%description
ChinaCache ForTest

%prep

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make %{?_smp_mflags}

%install
mkdir -vp %{buildroot}/%{prefix}/{sbin,logs,html,conf}
cp -af objs/nginx %{buildroot}/%{prefix}/sbin/
cp -af chinacache/nginx.conf %{buildroot}/%{prefix}/conf/nginx.conf

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

%changelog

