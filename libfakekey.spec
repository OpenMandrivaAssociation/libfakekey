%define major     0
%define raw_name  fakekey
%define libname   %mklibname %raw_name 0
%define develname %mklibname -d %raw_name

Name:           libfakekey
Version:        0.1
Release:        4
Summary:        Converting characters to X key-presses

Group:          System/Libraries
License:        LGPLv2+
URL:            http://projects.o-hand.com/matchbox/
Source0:        http://matchbox-project.org/sources/libfakekey/0.1/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)

%description
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package        -n %libname
Summary:        Converting characters to X key-presses
Group:          System/Libraries

%description    -n %libname
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package        -n %develname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %libname
Requires:       pkgconfig

%description    -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
export LDFLAGS="-lX11 -lXtst -lXi"
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %libname
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libfakekey.so.%{major}*


%files -n %develname
%defattr(-,root,root,-)
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-3.5.3mdv2011.0
+ Revision: 609744
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.1-3.5.2mdv2010.1
+ Revision: 508566
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Oct 16 2008 Thierry Vignaud <tv@mandriva.org> 0.1-3.5.1mdv2009.1
+ Revision: 294373
- fix group of devel package
- import libfakekey


* Thu Oct 16 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-3.5mdv2009.1
- adapt for Mandriva

* Tue Sep 23 2008 Vivian zhang <vivian.zhang@intel.com> 0.1
- Add BuildRequires: libXi-devel
* Mon Sep 22 2008 Anas Nashif <anas.nashif@intel.com> 0.1
- fixed Build Requires
* Thu Sep 18 2008 Vivian zhang <vivian.zhang@intel.com> 0.1
- Add BR libX11-devel
- Add comments "specfile originally created for..." at the top of the spec file
* Mon May 19 2008 Jon McCann <jmccann@redhat.com> 0.1-1
- Initial package
