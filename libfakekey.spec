%define major     0
%define raw_name  fakekey
%define libname   %mklibname %raw_name 0
%define develname %mklibname -d %raw_name

Name:           libfakekey
Version:        0.1
Release:        %mkrel 3.5.2
Summary:        Converting characters to X key-presses

Group:          System/Libraries
License:        LGPLv2+
URL:            http://projects.o-hand.com/matchbox/
Source0:        http://matchbox-project.org/sources/libfakekey/0.1/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libxtst-devel
BuildRequires:  X11-devel
BuildRequires:  libx11-devel
BuildRequires:  libxi-devel

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
%configure --disable-static
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_libdir}/libfakekey.la

%clean
rm -rf $RPM_BUILD_ROOT


%files -n %libname
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libfakekey.so.%{major}*


%files -n %develname
%defattr(-,root,root,-)
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc

