%define major 0
%define oname fakekey
%define libname %mklibname %{oname} %{major}
%define devname %mklibname -d %{oname}

Summary:		Converting characters to X key-presses
Name:			libfakekey
Version:		0.3
Release:		2
Group:			System/Libraries
License:		LGPLv2+
URL:			https://www.yoctoproject.org/tools-resources/projects/matchbox
Source0:		https://github.com/veyon/libfakekey/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
#Patch0:			libfakekey-0.1-ac.patch
BuildRequires:		pkgconfig(xtst)
BuildRequires:		pkgconfig(x11)
BuildRequires:		pkgconfig(xi)
BuildRequires:		pkgconfig(xfixes)

%description
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package -n %{libname}
Summary:		Converting characters to X key-presses
Group:			System/Libraries

%description -n %{libname}
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package -n %{devname}
Summary:		Development files for %{name}
Group:			Development/C
Requires:		%{libname} = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
#patch0 -p0

%build
sed -i -e 's/^fakekey_test_LDADD=/fakekey_test_LDADD=-lX11 /' tests/Makefile.am
sed -e "s/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/" -i configure.ac

autoreconf -fiv

%configure \
	--with-x

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libfakekey.so.%{major}*

%files -n %{devname}
%doc COPYING
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc

