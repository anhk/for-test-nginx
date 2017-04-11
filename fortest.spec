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
make install DESTDIR=%{buildroot}

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

%changelog

