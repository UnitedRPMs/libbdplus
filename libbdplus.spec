%global gitdate 20170426
%global commit0 795a9e43d904f948c096dbe34a8e647177b5bb2a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libbdplus
Version:        0.1.2
Release:        3%{?gver}%{?dist}
Summary:        Open implementation of BD+ protocol
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libbdplus.html
Source1:	libbdplus-snapshot

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:	git

BuildRequires:  libgcrypt-devel
BuildRequires:  libaacs-devel >= 0.7.0


%description
libbdplus is a research project to implement the BD+ System Specifications.
This research project provides, through an open-source library, a way to
understand how the BD+ protocol works.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{S:1} -c %{commit0}
%setup -T -D -n %{name}-%{shortcommit0}

./bootstrap    

%build

autoreconf -vif

%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING ChangeLog README.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog

* Wed Apr 26 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.2-3.git795a9e4
- Updated to 0.1.2-3.git795a9e4

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 27 2015 Xavier Bachelot <xavier@bachelot.org> - 0.1.2-1
- Update to 0.1.2.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 04 2014 Xavier Bachelot <xavier@bachelot.org> - 0.1.1-1
- Update to 0.1.1.

* Sat Apr 26 2014 Xavier Bachelot <xavier@bachelot.org> - 0.1.0-4
- Add patch for libgcrypt 1.6 support.

* Sat Apr 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-3
- Rebuilt for libgcrypt

* Wed Jan 08 2014 Xavier Bachelot <xavier@bachelot.org> 0.1.0-2
- Add version to libaacs BuildRequires:.
- Remove Group: tags.
- Use %%make_install macro.
- Minor specfile fixes.

* Fri Dec 27 2013 Xavier Bachelot <xavier@bachelot.org> 0.1.0-1
- Initial release.
